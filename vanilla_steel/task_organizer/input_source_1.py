import pandas as pd
from typing import Generator, Tuple

from vanilla_steel.task_organizer.task_organizer import TaskOrganizer

class InputSource1(TaskOrganizer):
    def __init__(self, source) -> None:
        self.source = source
        self.data = None

    def read_data(self) -> Generator[Tuple[str, pd.DataFrame], None, None]:
        xls = pd.ExcelFile(self.source)
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            yield sheet_name, df

    def restructure(self, sheet_name: str, df: pd.DataFrame) -> pd.DataFrame:
        df.drop(df.index[-1], inplace=True)
        df.reset_index(drop=True, inplace=True)
        df["Source"] = self.source
        df["Sheet Name"] = sheet_name
        return df

    def formatted_text(self) -> Generator[str, None, None]:
        for sheet_name, df in self.read_data():
            formatted_df: pd.DataFrame = self.restructure(sheet_name, df)
            for idx, row in formatted_df.iterrows():
                text = [f"Row Number: {idx}"]
                for k, v in row.items():
                    text += [f"{k}: {v}"]
                yield "\n".join(text)
        return super().formatted_text()