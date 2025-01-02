from typing import Optional

from pyproxmox_ve.models.base import ProxmoxBaseModel

class QemuReboot(ProxmoxBaseModel):
    timeout: Optional[int] = None
  
class QemuReset(ProxmoxBaseModel):
    skiplock: Optional[bool] = None

class QemuResume(ProxmoxBaseModel):
    nocheck: Optional[bool] = None
    skiplock: Optional[bool] = None

class QemuShutdown(ProxmoxBaseModel):
    forceStop: Optional[bool] = None
    keepActive: Optional[bool] = None
    skiplock: Optional[bool] = None
    timeout: Optional[int] = 60

class QemuStart(ProxmoxBaseModel):
    force_cpu: Optional[str] = None
    machine: Optional[str] = None
    migratedfrom: Optional[str] = None
    migration_network: Optional[str] = None
    migration_type: Optional[str] = None
    skiplock: Optional[bool] = None
    stateuri: Optional[str] = None
    targetstorage: Optional[str] = None
    timeout: Optional[int] = None

class QemuStop(ProxmoxBaseModel):
    keepActive: Optional[bool] = False
    migratedfrom: Optional[str] = None
    overrule_shutdown: Optional[bool] = 0
    skiplock: Optional[bool] = None
    timeout: Optional[int] = None

class QemuSuspend(ProxmoxBaseModel):
    skiplock: Optional[bool] = None
    statestorage: Optional[str] = None
    todisk: Optional[bool] = False