import re
import pandas as pd
from typing import Tuple
from collections.abc import Callable, Generator
from abc import ABC, abstractmethod

class TaskOrganizer(ABC):
    pattern = r'(?P<length>\d{1,2}(?:[,.]\d{2})?) x (?P<breadth>\d{1,4}(?:[,.]\d{2})?)(?: x (?P<height>\d{1,4}(?:[,.]\d{2})?))?(?: (?P<dimension_unit>mm))?'
    def __init__(self, source) -> None:
        self.source = source

    @abstractmethod
    def read_data(self) -> Generator[Tuple[str, pd.DataFrame], None, None]:
        pass

    @abstractmethod
    def restructure(self, sheet_name: str, df: pd.DataFrame) -> pd.DataFrame:
        pass

    def extract_dimensions(self, text):
        match = re.search(self.pattern, text)
        if match:
            return match.groupdict()
        return {"length": None, "breadth": None, "height": None, "dimension_unit": None}

    def formatted_records(self) -> Generator[Tuple[int, dict], None, None]:
        for sheet_name, df in self.read_data():
            formatted_df: pd.DataFrame = self.restructure(sheet_name, df)
            for idx, row in formatted_df.iterrows():
                yield idx, row.to_dict()

class TaskOrganizerFactory:
    def __init__(self) -> None:
        self.funcs: dict[str, Callable[..., TaskOrganizer]] = {}

    def register(self, input_source: str, task_organizer_func: Callable[..., TaskOrganizer]) -> TaskOrganizer:
        self.funcs[input_source] = task_organizer_func
        return task_organizer_func

    def unregister(self, input_source: str):
        self.funcs.pop(input_source, None)


