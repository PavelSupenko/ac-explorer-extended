from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '2132CC6E'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(12)
		checkByte = file_object_data_wrapper.read_bytes(1)
		py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper)
