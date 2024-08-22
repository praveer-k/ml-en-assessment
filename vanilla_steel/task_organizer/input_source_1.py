import pandas as pd
from typing import Generator, Tuple

from vanilla_steel.task_organizer.task_organizer import TaskOrganizer

class InputSource1(TaskOrganizer):
    def __init__(self, source) -> None:
        self.source = source
        self.strength = ['RP02', 'RM', 'A', 'STA']
        self.composition = ['AG', 'Al', 'Ars', 'B', 'C', 'Ca', 'Cr', 'S', 'Cu', 'Mn', 'Mo', 'N', 'Nb', 'Ni', 'P', 'Si', 'Sn', 'Ti', 'V', 'Zr']

    @staticmethod
    def kv(row, keys, sep="\n"):
        parts = []
        for key in keys:
            if row[key] is not None and pd.notna(row[key]):
                parts.append(f"{key}: {row[key]}")
        return sep.join(parts) if len(parts) > 0 else None

    def set_properties(self, row):
        props = []
        grade = row["Grade"] if row["Grade"] is not None and pd.notna(row["Grade"]) else None
        strength = self.kv(row, self.strength, sep="\n\t")
        composition = self.kv(row, self.composition, sep="\n\t")
        if grade:
            props.append(f"Grade: {grade}")
        if strength:
            props.append(f"Strength: \n\t{strength}")
        if composition:
            props.append(f"Chemical composition: \n\t{composition}")
        return "\n".join(props) if len(props) > 0 else None

    def set_description(self, row):
        keys = ['Description', 'Finish']
        return self.kv(row, keys)
    
    def read_data(self) -> Generator[Tuple[str, pd.DataFrame], None, None]:
        xls = pd.ExcelFile(self.source)
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            yield sheet_name, df

    def restructure(self, sheet_name: str, df: pd.DataFrame) -> pd.DataFrame:
        # cleaning
        df = df.drop(df.index[-1])
        df["Finish"] = df["Finish"].str.replace("ungebeizt, nicht geglüht", "Unpickled, Not Annealed")
        df["Finish"] = df["Finish"].str.replace("gebeizt und geglüht", "Pickled and Annealed")
        # description
        df["Description"] = df["Description"].str.replace('Sollmasse (Gewicht) unterschritten', "Below target weight")
        df["Description"] = df["Description"].str.replace('Kantenfehler - FS-Kantenrisse', "Edge defects - FS edge cracks")
        df["Description"] = df["Description"].str.replace('Längs- oder Querrisse', "Longitudinal or transverse cracks")
        # properties
        df["properties"] = df.apply(self.set_properties, axis=1)
        df["Description"] = df.apply(self.set_description, axis=1)
        # remove unwanted columns
        df.drop(columns=["Finish"] + self.strength + self.composition, inplace=True)
        # rename columns
        df.columns = [col.lower().strip().replace(" ","_") for col in df.columns]
        df.rename(columns={"quality/choice": "choice", "grade": "material_name", "thickness_(mm)": "height", "width_(mm)": "breadth", "gross_weight_(kg)": "weight_amount"}, inplace=True)
        # defaults found using from column names and its values
        df["choice"] = df["choice"].str.replace("2nd", "2")
        df["choice"] = df["choice"].fillna("-1")
        df["choice"] = df["choice"].astype(int)
        df["choice"] = df["choice"].replace(-1, None)
        df["quantity_unit"] = "piece"
        df["dimension_unit"] = "mm" 
        df["weighing_unit"] = "kg"
        # not defined
        df['length'] = None
        df["quantity"] = None
        df["material_id"] = None
        df["total_price"] = None
        df["price_per_unit"] = None
        df["supplier"] = None
        df["reserved"] = None
        # cast material id as str
        df["material_id"] = df["material_id"].astype(str)
        df["material_name"] = df["material_name"].fillna("").astype(str)
        df["material_name"] = df["material_name"].replace("", None)
        # re-order columns
        df = df.reindex(columns=['material_id', 'material_name', 'quantity', 'quantity_unit', 'price_per_unit', 'supplier', 'length', 'breadth', 'height', 'dimension_unit', 'weight_amount', 'weighing_unit', 'properties', 'description', 'choice', 'reserved'])
        # extra information
        df["file_path"] = self.source
        df["sheet_name"] = sheet_name
        return df