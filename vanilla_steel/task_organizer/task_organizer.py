import pandas as pd
from typing import Generator, Tuple
from abc import ABC, abstractmethod

class TaskOrganizer(ABC):
    @abstractmethod
    def read_data(self) -> Generator[Tuple[str, pd.DataFrame], None, None]:
        pass

    @abstractmethod
    def restructure(self, sheet_name: str, df: pd.DataFrame) -> pd.DataFrame:
        pass

    def formatted_text(self) -> Generator[str, None, None]:
        for sheet_name, df in self.read_data():
            formatted_df: pd.DataFrame = self.restructure(sheet_name, df)
            for idx, row in formatted_df.iterrows():
                text = [f"Row Number: {idx}"]
                for k, v in row.items():
                    text += [f"{k}: {v}"]
                yield "\n".join(text)