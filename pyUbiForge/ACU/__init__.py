import json
import os
from .getMaterialIDs_ import get_material_ids

game_identifier = "ACU"
file_types = json.load(open(f"{os.path.dirname(__file__)}/fileFormats.json"))
pre_header_length = 1
file_id_datatype = "Q"
file_type_length = 4
