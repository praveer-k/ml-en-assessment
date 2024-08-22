import pandas as pd
import numpy as np
from typing import Generator, Tuple

from vanilla_steel.task_organizer.task_organizer import TaskOrganizer

class InputSource2(TaskOrganizer):
   def __init__(self, source: str) -> None:
      self.source: str = source

   def read_data(self) -> Generator[Tuple[str, pd.DataFrame], None, None]:
      xls = pd.ExcelFile(self.source)
      for sheet_name in xls.sheet_names:
         df = pd.read_excel(xls, sheet_name=sheet_name)
         yield sheet_name, df
   
   def restructure(self, sheet_name: str, df: pd.DataFrame) -> pd.DataFrame:
      match sheet_name.strip():
         case 'First choice':
            return self.sheet1(sheet_name, df)
         case '2nd choice':
            return self.sheet2(sheet_name, df)
         
   def sheet1(self, sheet_name: str, df: pd.DataFrame) -> pd.DataFrame:
      # df1
      df1 = df.iloc[1:12]
      df1.columns = df.iloc[0].tolist()
      df1.reset_index(drop=True, inplace=True)
      # df2
      df2 = df.iloc[15:23]
      df2.columns = df.iloc[14].tolist()
      df2.reset_index(drop=True, inplace=True)
      # df3
      df3 = df.iloc[26:]
      df3.columns = df.iloc[25].tolist()
      df3.reset_index(drop=True, inplace=True)
      df3 = df3.dropna(axis=1, how='all')
      # cleaning
      df = pd.concat([df1, df2, df3])
      # rename columns
      df.columns = [col.lower().strip().replace(" ","_") for col in df.columns]
      df.rename(columns={"article_id": "material_id", "material": "properties", "description": "other_description", "opmerking": "description", "weight": "weight_amount"}, inplace=True)
      # fill empty values
      df["description"] = df["description"].where(df["description"].notna(), None)
      # move values to properties from other description
      df["properties"] = df.apply(lambda row: row["properties"] + " Oiled" if str(row["other_description"]).strip()=="Material is Oiled" else row["properties"], axis=1)
      df.drop(columns=["other_description"], inplace=True)
      # parse dimensions from the excel sheets
      df["properties"] = df["properties"].str.replace(r'(\d)x', r'\1 x ', regex=True)
      df = df.join(df["properties"].apply(self.extract_dimensions).apply(pd.Series))
      df["dimension_unit"] = df["dimension_unit"].fillna("mm")
      df["length"] = df["length"].str.replace(",", ".").where(df["length"].notna(), None)
      df["breadth"] = df["breadth"].str.replace(",", ".").where(df["breadth"].notna(), None)
      df["height"] = df["height"].str.replace(",", ".").where(df["height"].notna(), None)
      # clean properties column
      df["properties"] = df["properties"].str.replace(r'(\w)\+', r'\1 +', regex=True)
      df["properties"] = df["properties"].str.replace(r'(\d)mm', r'\1 mm', regex=True)
      df["properties"] = df["properties"].str.replace(self.pattern, '', regex=True)
      df["properties"] = df["properties"].apply(lambda x: x.replace("geolied", "Oiled"))
      # defaults found using from column names and its values
      df["quantity_unit"] = "piece"
      df["choice"] = 1
      # not defined
      df["material_name"] = None
      df["total_price"] = None
      df["price_per_unit"] = None
      df["supplier"] = None
      df["weighing_unit"] = None
      # cast material id as str
      df["material_id"] = df["material_id"].where(df["material_id"].notna(), None)
      df["material_name"] = df["material_name"].where(df["material_name"].notna(), None)
      df["reserved"] = df["reserved"].where(df["reserved"].notna(), None)
      df["quantity"] = df["quantity"].where(df["quantity"].notna(), None)
      # re-order columns
      df = df.reindex(columns=['material_id', 'material_name', 'quantity', 'quantity_unit', 'price_per_unit', 'supplier', 'length', 'breadth', 'height', 'dimension_unit', 'weight_amount', 'weighing_unit', 'properties', 'description', 'choice', 'reserved'])
      # add additional columns
      df["file_path"] = self.source.replace('\\', '/')
      df["sheet_name"] = sheet_name.strip()
      return df
   
   def sheet2(self, sheet_name: str, df: pd.DataFrame) -> pd.DataFrame:
      # reorganize sub-tables
      material_name1 = str(df.columns[0]).strip()
      material_name2 = str(df.iloc[15, 0]).strip()
      material_name3 = str(df.iloc[27, 0]).strip()
      df.columns = df.iloc[0].tolist()
      df = df.drop(index=0)
      df["material_name"] = None
      df.loc[0:12, "material_name"] = material_name1
      df.loc[17:25, "material_name"] = material_name2
      df.loc[29:, "material_name"] = material_name3
      df = df.dropna(axis=0, how='all')
      df.drop(index=[12, 15, 16, 27, 28], inplace=True)
      # rename columns
      df.columns = [col.lower().strip().replace(" ","_") for col in df.columns]
      df.rename(columns={"article_id": "material_id", "material": "properties", "defect_description": "description", "weight": "weight_amount"}, inplace=True)
      # parse dimensions from the excel sheets
      df["properties"] = df["properties"].str.replace('*', 'x')
      df["properties"] = df["properties"].str.replace(r'(\d)x', r'\1 x ', regex=True)
      df = df.join(df["properties"].apply(self.extract_dimensions).apply(pd.Series))
      df["dimension_unit"] = df["dimension_unit"].fillna("mm")
      df["length"] = df["length"].str.replace(",", ".").where(df["length"].notna(), None)
      df["breadth"] = df["breadth"].str.replace(",", ".").where(df["breadth"].notna(), None)
      df["height"] = df["height"].str.replace(",", ".").where(df["height"].notna(), None)
      # fix descriptions
      df["description"] = df.apply(lambda row: row["description"] if "ongeb/ ongeol traan" not in row["properties"] else row["description"] + " ongeb/ ongeol traan", axis=1)
      df["description"] = df["description"].where(df["description"].notna(), None)
      # clean properties column
      df["properties"] = df["properties"].str.replace(r'(\w)\+', r'\1 +', regex=True)
      df["properties"] = df["properties"].str.replace(r'(\d)mm', r'\1 mm', regex=True)
      df["properties"] = df["properties"].str.replace(self.pattern, '', regex=True)
      df["properties"] = df["properties"].apply(lambda x: x.replace("licht geolied", "Little-Oiled"))
      df["properties"] = df["properties"].apply(lambda x: x.replace("geolied", "Oiled"))
      df["properties"] = df["properties"].apply(lambda x: x.replace("ongeb/ ongeol traan", ""))
      df["properties"] = df["properties"].apply(lambda x: x.replace("MAC", "Ma-C"))
      # defaults found using from column names and its values
      df["quantity_unit"] = "piece"
      df["choice"] = 2
      # not defined
      df["total_price"] = None
      df["price_per_unit"] = None
      df["supplier"] = None
      df["weighing_unit"] = None
      df["reserved"] = None
      # cast material id as str
      df["material_id"] = df["material_id"].where(df["material_id"].notna(), None)
      df["reserved"] = df["reserved"].where(df["reserved"].notna(), None)
      df["quantity"] = df["quantity"].where(df["quantity"].notna(), None)
      # re-order columns
      df = df.reindex(columns=['material_id', 'material_name', 'quantity', 'quantity_unit', 'price_per_unit', 'supplier', 'length', 'breadth', 'height', 'dimension_unit', 'weight_amount', 'weighing_unit', 'properties', 'description', 'choice', 'reserved'])
      # add additional columns
      df["file_path"] = self.source.replace('\\', '/')
      df["sheet_name"] = sheet_name.strip()
      return df
