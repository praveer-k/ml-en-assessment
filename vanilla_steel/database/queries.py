from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, select, distinct, func
from vanilla_steel.config import settings
from vanilla_steel.database.base import Base, MaterialTable, MaterialPropertiesTable
from vanilla_steel.database.models import Dimension, Weight, Material, MaterialProperties

def convert_to_material_table(details: Material) -> MaterialTable:
    # 'material_id', 'material_name', 'quantity', 'quantity_unit', 'price_per_unit', 'supplier', 'length', 'breadth', 'height', 
    # 'dimension_unit', 'weight', 'weighing_unit', 'properties', 'description', 'choice', 'reserved', 'file_path', 'sheet_name'
    return MaterialTable(
        manufacturer_id=details.manufacturer_id,
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

def get_distinct_property_desc():
    engine = create_engine(settings.DB.CONNECTION_STRING)
    session = Session(engine)
    subquery = select(MaterialPropertiesTable.material_id)
    query = select(
                func.array_agg(MaterialTable.id).label('ids'), 
                func.concat(MaterialTable.properties, ' ', MaterialTable.description).label('property_desc')
            ).where(
                MaterialTable.properties.isnot(None),
                MaterialTable.description.isnot(None),
                MaterialTable.id.not_in(subquery)
            ).group_by(
                MaterialTable.properties,
                MaterialTable.description
            )
    result = session.execute(query).all()
    results = [(row.ids, row.property_desc) for row in result]
    return results

def insert_into_material_properties_table(records: list[MaterialProperties]):
    engine = create_engine(settings.DB.CONNECTION_STRING)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        for record in records:
            new_material_property = MaterialPropertiesTable(
                material_id=record.material_id,
                summary=record.summary,
                damaged=record.damaged,
                oiled=record.oiled,
                annealed=record.annealed,
                pickled=record.pickled,
                ductile=record.ductile,
                surface=record.surface,
                zinc_coating=record.zinc_coating,
                zinc_coating_strength=record.zinc_coating_strength,
                yield_strength=record.yield_strength,
                tensile_strength=record.tensile_strength,
                automotive_grade=record.automotive_grade,
                consumer_grade=record.consumer_grade
            )
            session.add(new_material_property)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
    finally:
        session.close()

def fetch_stats():
    engine = create_engine(settings.DB.CONNECTION_STRING)
    session = Session(engine)
    query = select(
        func.count().label('total_count'),
        func.count().filter(MaterialPropertiesTable.annealed == True).label('annealed'),
        func.count().filter(MaterialPropertiesTable.ductile == True).label('ductile'),
        func.count().filter(MaterialPropertiesTable.damaged == True).label('damaged'),
        func.count().filter(MaterialPropertiesTable.oiled == True).label('oiled'),
        func.count().filter(MaterialPropertiesTable.pickled == True).label('pickled'),
        func.count().filter(MaterialPropertiesTable.zinc_coating == True).label('zinc_coated')
    )
    result = session.execute(query).one()
    session.close()
    return {
        'total_count': result.total_count,
        'annealed': result.annealed,
        'ductile': result.ductile,
        'damaged': result.damaged,
        'oiled': result.oiled,
        'pickled': result.pickled,
        'zinc_coated': result.zinc_coated
    }