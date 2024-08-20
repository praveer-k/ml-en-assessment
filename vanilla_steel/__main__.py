import json
from vanilla_steel.llm.llm import get_llm_output
from vanilla_steel.task_organizer.task_organizer import TaskOrganizer
from vanilla_steel.task_organizer.input_source_1 import InputSource1

def show_data(task: TaskOrganizer, source: str):
    input_source: TaskOrganizer = task(source)
    required_fields = """
        material_id, material_name, quantity, unit, price_per_unit, supplier, dimensions, weight
    """
    for text_data in input_source.formatted_text():
        prompt = f"""
        You are an expert in the steel industires. You know in-depth about all the jargons used in its manufacturing and supply chain processes.
        You are also multi-lingual and therefore can translate everything into english language when you encounter a jargon in other language.
        Generate a json object that contains the following fields:
        {required_fields}
        Given the following text: 
        {text_data}
        """
        print(json.dumps(get_llm_output(prompt), indent=4))
        print("="*100)
        break

show_data(InputSource1, "./resources/source1.xlsx")
