from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorVectorNegate(SubclassBaseFile):
    ResourceType = 0x7CA403C6
    ParentResourceType = _Operator.ResourceType
    parent: _Operator