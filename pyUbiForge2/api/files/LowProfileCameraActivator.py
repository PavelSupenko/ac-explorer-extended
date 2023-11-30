from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class LowProfileCameraActivator(SubclassBaseFile):
    ResourceType = 0x8F27967C
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator