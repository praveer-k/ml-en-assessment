from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from vanilla_steel.config import settings
from vanilla_steel.database.base import Base, MaterialTable
from vanilla_steel.database.models import Dimension, Weight, Material

def convert_to_material_table(details: Material) -> MaterialTable:
    # 'material_id', 'material_name', 'quantity', 'quantity_unit', 'price_per_unit', 'supplier', 'length', 'breadth', 'height', 
    # 'dimension_unit', 'weight', 'weighing_unit', 'properties', 'description', 'choice', 'reserved', 'file_path', 'sheet_name'
    return MaterialTable(
        material_id=details.material_id,
        material_name=details.material_name,
        quantity=details.quantity,
        quantity_unit=details.quantity_unit,
        price_per_unit=details.price_per_unit,
        supplier=details.supplier,
        dimensions=Dimension(
            length=details.length,
            breadth=details.breadth,
            height=details.height,
            dimension_unit=details.dimension_unit
        ) if details.length or details.breadth or details.height else None,
        weight=Weight(
            weight_amount=details.weight_amount,
            weighing_unit=details.weighing_unit
        ) if details.weight_amount else None,
        properties=details.properties,
        description=details.description,
        choice=details.choice,
        reserved=details.reserved,
        file_path=details.file_path,
        sheet_name=details.sheet_name
    )


def insert_into_material_table(details: Material):
    engine = create_engine(settings.DB.CONNECTION_STRING)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        new_material = convert_to_material_table(details)
        session.add(new_material)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
    finally:
        session.close()