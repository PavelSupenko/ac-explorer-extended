from typing import Dict, Type

from pyUbiForge2.api import BaseGame, BaseFile
from pyUbiForge2.api.file_object import FileDataWrapper

from .forge import ACUForge


FileReaders: Dict[int, Type[BaseFile]] = {}


def register_file_reader(file_id: str):
    """Register a class that can read a given file id eg \"0984415E\""""
    def register_(cls):
        assert issubclass(cls, BaseFile), "The @register_file_reader can only be used with classes that subclass BaseFile"
        FileReaders[int(file_id, 16)] = cls
        return cls

    return register_


class ACUGame(BaseGame):
    ForgeClass = ACUForge
    GameIdentifier = "ACU"
    FileIDType = "Q"
    ResourceType = "I"

    def read_file(self, file: FileDataWrapper) -> BaseFile:
        file_id = file.read_file_id()
        resource_id = file.read_resource_type()
        if resource_id in FileReaders:
            with file.indent:
                return FileReaders[resource_id](file_id, resource_id, file)
        raise NotImplementedError(f"{resource_id:08X}")
