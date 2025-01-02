from typing import Optional

from pyproxmox_ve.models.base import ProxmoxBaseModel

class LxeReboot(ProxmoxBaseModel):
    timeout: Optional[int] = None

class LxeShutdown(ProxmoxBaseModel):
    forceStop: Optional[bool] = None
    timeout: Optional[int] = 60

class LxeStart(ProxmoxBaseModel):
    debug: Optional[bool] = 0
    skiplock: Optional[bool] = None

class LxeStop(ProxmoxBaseModel):
    overrule_shutdown: Optional[bool] = 0
    skiplock: Optional[bool] = None