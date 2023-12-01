from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractShopServices import AbstractShopServices as _AbstractShopServices


class DoctorShopServices(SubclassBaseFile):
    ResourceType = 0x61CA47A5
    ParentResourceType = _AbstractShopServices.ResourceType
    parent: _AbstractShopServices