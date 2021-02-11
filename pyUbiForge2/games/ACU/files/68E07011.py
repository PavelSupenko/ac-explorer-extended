from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('68E07011')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        file.read_bytes(1)
