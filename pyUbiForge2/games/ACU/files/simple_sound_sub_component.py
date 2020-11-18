from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('4E7C39C3')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        for _ in range(2):
            file.read_file()