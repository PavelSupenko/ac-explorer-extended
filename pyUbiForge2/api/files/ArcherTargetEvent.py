from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class ArcherTargetEvent(SubclassBaseFile):
    ResourceType = 0xFBEA7CE1
    ParentResourceType = _Event.ResourceType
    parent: _Event