from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class WagonClearAmbusherEventSeed(SubclassBaseFile):
    ResourceType = 0x171B628D
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed