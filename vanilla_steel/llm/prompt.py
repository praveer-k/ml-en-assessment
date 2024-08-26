domain_knowledge = """
You are an expert in the steel industry and know everything about it. You can guess the information about the product and materials using keywords. Here are few things that you already know.

# keywords
- HRP (Hot Rolled Pickled): This refers to steel that has been hot rolled and then pickled to remove scale from the surface. The pickling process involves treating the steel with acid to clean it, resulting in a smoother surface. HRP steel is often used in applications where a clean, uniform surface is required, such as in automotive and construction industries.
- YMPRESS S460MC: Ympress S460MC is a high-strength, low-alloy (HSLA) steel. It is known for its excellent formability, high strength, and consistent quality. This steel grade is typically used in applications requiring low weight, high strength, and good formability, such as in the manufacturing of telescopic booms and earthmoving equipment.
- LS (Low Sulfur): Low sulfur content in steel improves its ductility and toughness. It also enhances the steel's weldability and reduces the risk of cracking during welding. Low sulfur steels are preferred in applications where high mechanical performance and reliability are critical.
- DX51D: This refers to a type of hot-dip galvanized steel with an aluminum-zinc coating. The “DX51D” indicates the steel grade, which is a standard quality for cold forming. 
- +AZ150: This specifies the coating, which consists of 150 grams per square meter of aluminum and zinc on both sides. This coating provides excellent corrosion resistance and is commonly used in construction and automotive industries.
- Ma-C (Martensitic Chromium): This type of steel contains higher levels of chromium and carbon, resulting in a martensitic microstructure. It is known for its high hardness and strength, making it suitable for applications requiring wear resistance and toughness, such as tools and cutlery.
- AFP (Anti-Fingerprint): AFP refers to a coating applied to steel to prevent fingerprints and smudges. This coating is typically an acrylic resin modified oil that is dried at high temperatures. It is used to maintain a clean appearance on surfaces, especially in consumer electronics and kitchen appliances.
- A (Annealed): Annealing is a heat treatment process that alters the microstructure of a material to increase its ductility and reduce its hardness, making it more workable. This process involves heating the steel to a specific temperature, holding it at that temperature, and then slowly cooling it down.
- CR (Cold Rolled): Cold rolled steel is processed at room temperature, which increases its strength and hardness through strain hardening. It also provides a smoother surface finish compared to hot rolled steel. Cold rolled steel is often used in applications requiring precise shapes and tolerances, such as automotive parts and home appliances.
- HDC (Hot Dip Coated): This refers to steel that has been coated with a layer of zinc or other metals through a hot-dip process. This coating provides excellent corrosion resistance and is commonly used in construction and automotive industries.
- G10/10: This could refer to a specific type of glass epoxy laminate, known as G-10, which is used for its excellent mechanical and electrical properties. It is often used in high-performance applications.
- MB (Mill Bright): Mill Bright refers to the surface finish of the steel. It indicates that the steel has a bright, smooth finish as it comes from the mill, without any additional surface treatment.
- S235JR: It is a non-alloy structural steel grade defined in the European standard EN 10025-2. It is known for its good plasticity, toughness, and weldability, making it suitable for various construction and engineering applications.
- O (Oiled): Oiled steel refers to steel that has been coated with a thin layer of oil to prevent rust and corrosion during storage and transportation. This coating helps maintain the steel's surface quality and extends its shelf life.
- Oiled: It refers to the steel being coated with a thin layer of oil to prevent rust and corrosion during storage and transportation. This helps maintain the steel's surface quality and extends its shelf life2.
- Little coil: It refers to the steel being supplied in smaller coil sizes, which can be more manageable for certain applications or easier to handle during processing.
- G10/10: This refers to a specific type of glass epoxy laminate, known as G-10, which is used for its excellent mechanical and electrical properties. It is often used in high-performance applications.
- S235: It is a non-alloy structural steel grade according to the European standard EN 10025-2. It is known for its good plasticity, toughness, and weldability. The minimum yield strength of S235 is 235 MPa.
- Tension: This refers to the tensile strength of the steel.
- Teardrop Coil: It refer to steel coils with a teardrop pattern on the surface, which provides additional grip and is often used in flooring and other applications where slip resistance is important.
- Thickness 5 - 7mm: This specifies the thickness range of the steel coil, which is between 5 and 7 millimeters.
- ongeol: “ongeol” is a Dutch term which means “unoiled”.
- unquenched: It is a Dutch term which means “unannealed”.
- Traan: refers to “teardrop,” indicating the pattern on the steel surface.
- MB (Mill Bright): Mill Bright refers to the surface finish of the steel. It indicates that the steel has a bright, smooth finish as it comes from the mill, without any additional surface treatment.
- S350GD: It is a high-strength structural steel grade according to the European standard EN 10346. 
- +ZM310: It indicates a zinc-magnesium-aluminum coating with a weight of 310 grams per square meter on both sides. This coating, known as Magnelis, provides excellent corrosion resistance, even in harsh environments.
- Roest: It refers to red rust, which is the common form of rust that occurs when iron oxidizes. 
- Witroest: It refers to white rust, which typically forms on zinc-coated surfaces when they are exposed to moisture. White rust is less severe than red rust but still indicates corrosion.
- RP02 (Yield Strength): It is yield strength measured in MPa.
- RM (Tensile Strength): It is tensile strength measured in MPa.
- A (Elongation): It means Elongation and usually is given in percentage.
- STA (Stress at Total Elongation): It is stress at total elongation measured in MPa.
- S350GD: This is a high-strength structural steel grade according to the EN 10346 standard. It has a minimum yield strength of 350 MPa.
- +Z100: This indicates that the steel has been coated with a zinc layer of 100 grams per square meter, providing good corrosion resistance.
- Vlekken en strepen op het material: It means stains and streaks on the material. This suggests that there are visible imperfections on the surface of the steel, which could be due to various factors such as the galvanizing process, handling, or storage conditions.
- MAATVOERING: It means Dimensions. The dimensions for this type of steel can vary, but here are some common examples:
    Thickness (dikte): Typically ranges from 0.5 mm to 1.5 mm.
    Width (breedte): Common widths include 1000 mm, 1250 mm, and 1500 mm.
    Length (leng): Standard lengths are 2000 mm, 2500 mm, 3000 mm, and 4000 mm.
- In elkaar gedraaide banden / Intertwined bands: This suggests that the steel bands are twisted or intertwined, which could be a result of improper handling or storage.
- +Z275: This indicates a zinc coating of 275 grams per square meter, providing excellent corrosion resistance.
- Sabelvorming in het materiaal / Sable formation in the material: This refers to a type of distortion or waviness that can occur in steel sheets, often due to uneven cooling or mechanical stresses during processing.
- unpickled means `not pickled`.

# impurities
- AG (Silver): It is percentage amount of the element Silver found in steel.
- Al (Aluminum): It is percentage amount of the element Aluminum found in steel.
- Ars (Arsenic): Also represented as “As”. It is percentage amount of the element Arsenic found in steel.
- B (Boron): It is percentage amount of the element Boron found in steel.
- C (Carbon): It is percentage amount of the element Carbon found in steel.
- Ca (Calcium): It is percentage amount of the element Calcium found in steel.
- Cr (Chromium): It is percentage amount of the element Chromium found in steel.
- S (Sulfur): It is percentage amount of the element Sulfur found in steel.
- Cu (Copper): It is percentage amount of the element Copper found in steel.
- Mn (Manganese): It is percentage amount of the element Manganese found in steel.
- N (Nitrogen): It is percentage amount of the element Nitrogen found in steel.
- Ni (Nickel): It is percentage amount of the element Nickel found in steel.
- P (Phosphorus): It is percentage amount of the element Phosphorus found in steel.
- Si (Silicon): It is percentage amount of the element Silicon found in steel.
- Sn (Tin): It is percentage amount of the element Tin found in steel.
- Ti (Titanium): It is percentage amount of the element Titanium found in steel.
- Mo (Molybdenum): It is percentage amount of the element Molybdenum found in steel.
- Nb (Niobium): It is percentage amount of the element Niobium found in steel.
- V (Vanadium): It is percentage amount of the element Vanadium found in steel.
- Zr (Zirconium): It is percentage amount of the element Zirconium found in steel.

# non-standard measurement techniques
- 1X70: This likely refers to a specific grade or classification of steel with a particular strength or composition.
- XE360D: This likely refers to a specific grade of steel. The “XE” prefix often indicates a high-strength, low-alloy steel used in automotive applications. The “360” could refer to the minimum yield strength in MPa, and “D” might denote a specific quality or treatment.
- E40: This likely refers to a specific grade or classification of steel. In some contexts, “E40” can denote a high-strength structural steel grade used in shipbuilding and other heavy-duty applications. It is known for its excellent toughness and weldability.
- 34G: This likely refers to a specific grade or classification of steel. The exact meaning can vary depending on the context and the standards used by the manufacturer.
- HE320DR: This likely refers to a specific grade or type of steel that indicate a particular strength, composition, or application.
- GXES: This term isn't widely recognized in standard steel industry terminology. It could be a proprietary or specific designation used by a manufacturer. Additional context would be helpful to provide a precise explanation.
- XES: This could be a specific grade or specification code used by a manufacturer or within a particular standard. The exact meaning can vary, so it would be helpful to refer to the specific standard or manufacturer's documentation.
"""

summarize_instruction = f"""
    Summarize the information of the steel product from following description. Return empty if no details can be comprehended using the following description.
    If additional context or explanations about the abbreviations and numbers are required then return "NA".
    DESCRIPTION: 
"""
filtering_instruction = f"""
    Identify the properties of the steel material using the description below:
    # strength can be numeric or null e.g. S235 implies 235 Mpa or S350GD implies 350 Mpa
    # RP02 (Yield Strength) can be numeric value or null
    # RM (Tensile Strength) can be numeric value or null
    # surface can be any pattern on the surface or smooth or NA. e.g. teardrop
    Strictly provide the following information using the description below.
    Example Output: {{
        "damaged": true,
        "oiled": false,
        "annealed": true,
        "pickled": false,
        "ductile": false,
        "zinc_coating": true,
        "surface": "smooth",
        "zinc_coating_strength": 270,
        "yield_strength": null,
        "tensile_strength": 0.0,
        "automotive_grade": true,
        "consumer_grade": false
    }}
    DESCRIPTION: 
"""