from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackVec3 import AnimTrackVec3 as _AnimTrackVec3


class AnimTrackNearestVec3(SubclassBaseFile):
    ResourceType = 0x883CF3F3
    ParentResourceType = _AnimTrackVec3.ResourceType
    parent: _AnimTrackVec3