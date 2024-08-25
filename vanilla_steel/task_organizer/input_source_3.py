import pandas as pd
from typing import Generator, Tuple

from vanilla_steel.task_organizer.task_organizer import TaskOrganizer

class InputSource3(TaskOrganizer):
   def __init__(self, source: str) -> None:
      self.source: str = source

   def read_data(self) -> Generator[Tuple[str, pd.DataFrame], None, None]:
      xls = pd.ExcelFile(self.source)
      for sheet_name in xls.sheet_names:
         df = pd.read_excel(xls, sheet_name=sheet_name)
         yield sheet_name, df
      
   def restructure(self, sheet_name: str, df: pd.DataFrame) -> pd.DataFrame:
      # rename columns
      df.columns = [col.lower().strip().replace(" ","_") for col in df.columns]
      df.rename(columns={"numéro_de": "manufacturer_id", "article": "material_name", "matériel_desc#": "properties", "unité": "weighing_unit", "libre": "weight_amount"}, inplace=True)
      # parse dimensions from the excel sheets
      df["properties"] = df["properties"].str.replace('*', 'x')
      df["properties"] = df["properties"].str.replace(r'(\d)x', r'\1 x ', regex=True)
      df = df.join(df["properties"].apply(self.extract_dimensions).apply(pd.Series))
      # clean properties column
      df["properties"] = df["properties"].str.replace(r'(\w)\+', r'\1 +', regex=True)
      df["properties"] = df["properties"].str.replace(r'(\d)mm', r'\1 mm', regex=True)
      df["properties"] = df["properties"].str.replace('+Z 140', '+Z140')
      df["properties"] = df["properties"].str.replace(self.pattern, '', regex=True)
      # defaults found using from column names and its values
      df["dimension_unit"] = df["dimension_unit"].fillna("mm")
      df["weighing_unit"] = df["weighing_unit"].str.lower()
      df["description"] = ""
      df["choice"] = None
      # not defined
      df["quantity"] = None
      df["quantity_unit"] = None
      df["price_per_unit"] = None
      df["supplier"] = None
      df["reserved"] = None
      # cast material id as str
      df["manufacturer_id"] = df["manufacturer_id"].where(df["manufacturer_id"].notna(), "").astype(str)
      df["manufacturer_id"] = df["manufacturer_id"].where(df["manufacturer_id"]=="", None)
      df["material_name"] = df["material_name"].where(df["material_name"].notna(), "").astype(str)
      df["material_name"] = df["material_name"].where(df["material_name"]=="", None)
      # re-order columns
      df = df.reindex(columns=['manufacturer_id', 'material_name', 'quantity', 'quantity_unit', 'price_per_unit', 'supplier', 'length', 'breadth', 'height', 'dimension_unit', 'weight_amount', 'weighing_unit', 'properties', 'description', 'choice', 'reserved'])
      # add additional columns
      df["file_path"] = self.source.replace('\\', '/')
      df["sheet_name"] = sheet_name.strip()
      return df
""
