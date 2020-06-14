from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('C0DD28A9')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        file.read_bytes(1)
        file.read_file_id()
        file.read_bytes(5)
        file.read_bytes(12)
        file.read_bytes(4 * 4 * 4 + 4)
        count = file.read_uint_32()
        for _ in range(count):
            file.indent()
            file.read_file()
            file.indent(-1)