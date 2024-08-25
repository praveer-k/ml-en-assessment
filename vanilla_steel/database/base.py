from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, func, ForeignKey
from sqlalchemy.orm import composite, relationship
from sqlalchemy import Column, Integer, String, Float, Text, Boolean
from vanilla_steel.database.models import Dimension, Weight

Base = declarative_base()

# Define the main MaterialTable class
class MaterialTable(Base):
    __tablename__ = 'materials'

    id = Column(Integer, primary_key=True, autoincrement=True)

    manufacturer_id = Column(String, nullable=True)
    material_name = Column(String, nullable=True)
    quantity = Column(Integer, nullable=True)
    quantity_unit = Column(String, nullable=True)
    price_per_unit = Column(Float, nullable=True)
    supplier = Column(String, nullable=True)
    
    # Composite mapping for dimensions
    dimensions = composite(Dimension,
                           Column("length", Float, nullable=True),
                           Column("breadth", Float, nullable=True),
                           Column("height", Float, nullable=True),
                           Column("dimension_unit", String, nullable=True))
    
    # Composite mapping for weight
    weight = composite(Weight,
                       Column("weight_amount", Float, nullable=True),
                       Column("weighing_unit", String, nullable=True))

    properties = Column(Text, nullable=True)
    description = Column(Text, nullable=True)

    choice = Column(Integer, nullable=True)
    reserved = Column(String, nullable=True)
    file_path = Column(Text, nullable=True)
    sheet_name = Column(String, nullable=True)

    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now(), server_default=func.now())


class MaterialPropertiesTable(Base):
    __tablename__ = 'material_properties'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # foreign key from materials table
    material_id = Column(Integer, ForeignKey('materials.id'))

    summary = Column(Text, nullable=True, default=None)
    # filter properties
    damaged = Column(Boolean, nullable=True, default=None)
    oiled = Column(Boolean, nullable=True, default=None)
    annealed = Column(Boolean, nullable=True, default=None)
    pickled = Column(Boolean, nullable=True, default=None)
    ductile = Column(Boolean, nullable=True, default=None)
    surface = Column(String, nullable=True, default=None)
    # coating
    zinc_coating = Column(Boolean, nullable=True, default=None)
    zinc_coating_strength = Column(Float, nullable=True, default=None)
    # strength
    yield_strength = Column(Float, nullable=True, default=None)
    tensile_strength = Column(Float, nullable=True, default=None)
    # grade of steel
    automotive_grade = Column(Boolean, nullable=True, default=None)
    consumer_grade = Column(Boolean, nullable=True, default=None)
    
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now(), server_default=func.now())
