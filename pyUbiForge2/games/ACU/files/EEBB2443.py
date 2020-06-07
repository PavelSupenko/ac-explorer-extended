from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader
import numpy


@register_file_reader('EEBB2443')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):

        BaseFile.__init__(self, file_id, resource_type)
        file.read_bytes(2)
        file.read_file_id()

        for _ in range(3):
            file.read_file()
        file.read_numpy(numpy.float32, 16)
        file.read_numpy(numpy.float32, 64).reshape((4, 4), order='F')

        file.read_file()
        file.read_bytes(1)
        file.read_numpy(numpy.float32, 64).reshape((4, 4), order='F')
