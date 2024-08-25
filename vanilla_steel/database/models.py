from datetime import datetime
# from pydantic import BaseModel
from pydantic.dataclasses import dataclass, Field

@dataclass
class MetadataMixin:
    id: int
    api_version: str
    created_at: datetime
    updated_at: datetime

@dataclass
class Dimension:
    length: float | None = Field(default_factory=None)
    breadth: float | None = Field(default_factory=None)
    height: float | None = Field(default_factory=None)
    dimension_unit: str | None = Field(default_factory=None)

@dataclass
class Weight:
    weight_amount: float | None = Field(default_factory=None)
    weighing_unit: str | None = Field(default_factory=None)

@dataclass
class Material:
    # required fields
    # 'manufacturer_id', 'material_name', 'quantity', 'quantity_unit', 'price_per_unit', 'supplier', 'length', 'breadth', 'height', 
    # 'dimension_unit', 'weight', 'weighing_unit', 'properties', 'description', 'choice', 'reserved', 'file_path', 'sheet_name'

    manufacturer_id: str | None = Field(default_factory=None)
    material_name: str | None = Field(default_factory=None)
    quantity: float | None = Field(default_factory=None)
    quantity_unit: str | None = Field(default_factory=None)
    price_per_unit: float | None = Field(default_factory=None)
    supplier: str | None = Field(default_factory=None)
    # dimensions
    length: float | None = Field(default_factory=None)
    breadth: float | None = Field(default_factory=None)
    height: float | None = Field(default_factory=None)
    dimension_unit: str | None = Field(default_factory=None)

    # weight
    weight_amount: float | None = Field(default_factory=None)
    weighing_unit: str | None = Field(default_factory=None)

    # properties and description
    properties: str | None = Field(default_factory=None)
    description: str | None = Field(default_factory=None)

    # customer choice and reservation remark
    choice: int | None = Field(default_factory=None)
    reserved: str | None = Field(default_factory=None)

    # meta information
    file_path: str | None = Field(default_factory=None)
    sheet_name: str | None = Field(default_factory=None)

@dataclass
class MaterialProperties:
    material_id: int
    summary               : str   | None = Field(default_factory=None)
    # properties
    damaged               : bool  | None = Field(default_factory=None)
    oiled                 : bool  | None = Field(default_factory=None)
    annealed              : bool  | None = Field(default_factory=None)
    pickled               : bool  | None = Field(default_factory=None)
    ductile               : bool  | None = Field(default_factory=None)
    surface               : str   | None = Field(default_factory=None)
    # coating
    zinc_coating          : bool  | None = Field(default_factory=None)
    zinc_coating_strength : float | None = Field(default_factory=None)
    # strength
    yield_strength        : float | None = Field(default_factory=None)
    tensile_strength      : float | None = Field(default_factory=None)
    # grade of steel
    automotive_grade      : bool  | None = Field(default_factory=None)
    consumer_grade        : bool  | None = Field(default_factory=None)
