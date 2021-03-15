from pyUbiForge.ACU.type_readers.minimap_textures import Reader as MMClass
from pyUbiForge.ACU.type_readers.texture import Reader as TextureClass
from plugins import BasePlugin
from PIL import Image
from io import BytesIO
import struct
from typing import Union, List
import pyUbiForge
import logging


class Plugin(BasePlugin):
    plugin_name = "Export Minimap"
    plugin_level = 4
    file_type = "EE568905"

    def run(
        self,
        file_id: Union[str, int],
        forge_file_name: str,
        datafile_id: int,
        options: Union[List[dict], None] = None,
    ):
        # TODO add select directory option
        save_folder = pyUbiForge.CONFIG.get("dumpFolder", "output")

        data = pyUbiForge.temp_files(file_id, forge_file_name, datafile_id)
        if data is None:
            logging.warning(f"Failed to find file {file_id:016X}")
            return
        file_name = data.file_name

        minimap_textures: MMClass = pyUbiForge.read_file(data.file)
        output_image = None
        tile_width = tile_height = 128
        for y in range(minimap_textures.width):
            for x in range(minimap_textures.height):
                texture_file_id = minimap_textures.image_ids[
                    y * minimap_textures.height + x
                ]
                texture_data = pyUbiForge.temp_files(texture_file_id)
                if texture_data is None:
                    logging.warning(f"Failed to find file {texture_file_id:016X}")
                    continue
                texture: TextureClass = pyUbiForge.read_file(texture_data.file)
                if output_image is None:
                    tile_width = struct.unpack("<I", texture.dwWidth)[0]
                    tile_height = struct.unpack("<I", texture.dwHeight)[0]
                    output_image = Image.new(
                        "RGBA",
                        (
                            tile_width * minimap_textures.width,
                            tile_height * minimap_textures.height,
                        ),
                    )
                temp_image = Image.open(BytesIO(texture.dds_string))
                output_image.paste(
                    temp_image,
                    (
                        tile_width * x,
                        tile_height * minimap_textures.height - tile_height * (y + 1),
                    ),
                )
            logging.info(f"Written {y+1} row of {minimap_textures.width}")
        if output_image is None:
            logging.info("No Minimap to export")
        else:
            output_image.save(f"{save_folder}/{file_name}.png")
