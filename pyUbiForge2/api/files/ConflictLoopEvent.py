from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class ConflictLoopEvent(SubclassBaseFile):
    ResourceType = 0xC710FDE9
    ParentResourceType = _Event.ResourceType
    parent: _Event