import pandas as pd
from typing import Generator, Tuple

from vanilla_steel.task_organizer.task_organizer import TaskOrganizer

class InputSource2(TaskOrganizer):
   def __init__(self, source) -> None:
      self.source = source
      self.data = None

   def read_data(self) -> Generator[Tuple[str, pd.DataFrame], None, None]:
      xls = pd.ExcelFile(self.source)
      for sheet_name in xls.sheet_names:
         df = pd.read_excel(xls, sheet_name=sheet_name)
         yield sheet_name, df
   
   def restructure(self, sheet_name: str, df: pd.DataFrame) -> pd.DataFrame:
      match sheet_name.strip():
         case 'First choice':
            df = self.sheet1(sheet_name, df)
         case '2nd choice':
            df = self.sheet2(sheet_name, df)
      df["Source"] = self.source
      df["Sheet Name"] = sheet_name
      return df
         
   def sheet1(self, df: pd.DataFrame) -> pd.DataFrame:
      df1 = df.iloc[1:12]
      df1.columns = df.iloc[0].tolist()
      df1.reset_index(drop=True, inplace=True)
      df2 = df.iloc[15:23]
      df2.columns = df.iloc[14].tolist()
      df2.reset_index(drop=True, inplace=True)
      df3 = df.iloc[26:]
      df3.columns = df.iloc[25].tolist()
      df3.reset_index(drop=True, inplace=True)
      df3 = df3.dropna(axis=1, how='all')
      df = pd.concat([df1, df2, df3])
      return df
   
   def sheet2(self, df: pd.DataFrame) -> pd.DataFrame:
      df.columns = df.iloc[1].tolist()
      df = df.drop(index=1)
      product_form1, product_form2, product_form3 = df.iloc[0,0], df.iloc[16,0], df.iloc[28,0]
      print(f"{product_form1}, {product_form2}, {product_form3}")
      df["Product Form"] = None
      df.loc[0:12, "Product Form"] = product_form1
      df.loc[18:26, "Product Form"] = product_form2
      df.loc[30:, "Product Form"] = product_form3
      df = df.dropna(axis=0, how='all')
      df.drop(index=[0, 16, 17, 28, 29], inplace=True)
      return df