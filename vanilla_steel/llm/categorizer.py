import json
from vanilla_steel.config import logger
from vanilla_steel.llm.prompt import filtering_instruction, summarize_instruction
from vanilla_steel.llm.llm import get_llm_output
from vanilla_steel.database.queries import get_distinct_property_desc, insert_into_material_properties_table
from vanilla_steel.database.models import MaterialProperties
from rich.progress import Progress

class Categorizer:
    def run(self):
        property_descs = get_distinct_property_desc()
        with Progress() as progress:
            task = progress.add_task("[cyan]Processing ...", total=len(property_descs))
            for i, prop_desc in enumerate(property_descs, 1):
                material_ids, property_desc = prop_desc
                summary = self.summarize(property_desc)
                filters = self.filter(property_desc)
                try:
                    extra_material_info = [MaterialProperties(material_id=material_id, summary=summary, **filters) for material_id in material_ids]
                    insert_into_material_properties_table(extra_material_info)
                    progress.update(task, advance=1)
                    progress.update(task, description=f"[cyan]Processing {i} out of {len(property_descs)}")
                except:
                    logger.error("Error Occured while constructing and inserting data from LLM")
                    logger.error(f"ids: {material_ids}")
                    logger.error(f"summary: {summary}")
                    logger.error(f"filters: {json.dumps(filters, indent=4)}")
            

    def summarize(self, input_text):
        prompt = f"{summarize_instruction}\n\n{input_text}\n\nSUMMARY:"
        response = get_llm_output(prompt)
        return response
    
    def filter(self, input_text):
        prompt = f"{filtering_instruction}\n\n{input_text}\n\nOUTPUT:"
        response = get_llm_output(prompt, format="json")
        return response 