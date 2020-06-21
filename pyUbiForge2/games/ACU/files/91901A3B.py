from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('91901A3B')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        count = file.read_uint_32()
        with file.indent:
            for _ in range(count):
                file.read_file()
