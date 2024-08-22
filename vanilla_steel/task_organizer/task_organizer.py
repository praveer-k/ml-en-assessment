import re
import pandas as pd
from typing import Generator, Tuple
from abc import ABC, abstractmethod
from vanilla_steel.llm.llm import get_llm_output
from vanilla_steel.llm.prompt import domain_knowledge, instruction

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

    def formatted_text(self) -> Generator[str, None, None]:
        for idx, row in self.formatted_records():
            text = [f"Row Number: {idx}"]
            for k, v in row.items():
                text += [f"{k}: {v}"]
            yield "\n".join(text)

    def get_source_records(self) -> Generator[dict, None, None]:
        for text_data in self.formatted_text():
            print(text_data)
            prompt = f"""CONTEXT: 
            You are a multi-lingual expert in the field of steel industry. Following arre some supporting documentation on steel industry jargons.
            
            {domain_knowledge}

            Always use the following format:
            {{'function': 'Answer Question', 'answer_text': ''}} 
            
            INSTRUCTIONS TO GENERATE JSON OBJECT:
            
            {instruction}
            
            QUESTION: 
            Generate a json object, given the following test data:
            
            {text_data}

            ANSWER:
            """
            yield get_llm_output(prompt)