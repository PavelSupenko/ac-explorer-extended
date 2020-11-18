from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('7313743E')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        count1 = file.read_uint_32()
        file.read_bytes(10)
        for _ in range(count1):
            file.read_file()