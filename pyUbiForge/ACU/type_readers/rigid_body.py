from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import numpy


class Reader(BaseReader):
	file_type = '228F402A'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(29)
		file_object_data_wrapper.read_id()
		file_object_data_wrapper.read_bytes(17)
		file_object_data_wrapper.out_file_write('Transformation Matrix\n')
		self.transformation_matrix = file_object_data_wrapper.read_numpy(numpy.float32, 64).reshape((4, 4), order='F')
