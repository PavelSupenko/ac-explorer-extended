from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HorseHitchActorGroundData(SubclassBaseFile):
    ResourceType = 0x45705E43
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData