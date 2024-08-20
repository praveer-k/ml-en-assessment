import pandas as pd
from typing import Generator, Tuple

from vanilla_steel.task_organizer.task_organizer import TaskOrganizer

class InputSource3(TaskOrganizer):
   def __init__(self, source) -> None:
      self.source = source
      self.data = None

   def read_data(self) -> Generator[Tuple[str, pd.DataFrame], None, None]:
      xls = pd.ExcelFile(self.source)
      for sheet_name in xls.sheet_names:
         df = pd.read_excel(xls, sheet_name=sheet_name)
         yield sheet_name, df
      
   def restructure(self, sheet_name: str, df: pd.DataFrame) -> pd.DataFrame:
      df["Source"] = self.source
      df["Sheet Name"] = sheet_name
      return df

