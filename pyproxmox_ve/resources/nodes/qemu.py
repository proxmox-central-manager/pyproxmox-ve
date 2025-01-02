from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pyproxmox_ve.models.qemu import (
  QemuReboot,
  QemuReset,
  QemuResume,
  QemuShutdown,
  QemuStart,
  QemuStop,
  QemuSuspend
)

if TYPE_CHECKING:
    from pyproxmox_ve.api import ProxmoxVEAPI

class NodeQemuAPI:
    def __init__(self, api: ProxmoxVEAPI, base_endpoint: str) -> None:
        self.api = api
        self.base_endpoint = base_endpoint
        
    async def get_status(self) -> dict:
        """Get the status of a qemu.

        Args:
        """
        return await self.api.query(
            endpoint=f"{self.base_endpoint}/status/current",
            method="GET",
        )
   
    # Created endpoints for: reboot, reset, resume, shutdown, start, stop, suspend
    # using the Models from pyproxmox_ve.models.qemu

    async def reboot(self, **kwargs) -> bool:
        """Reboot a qemu.

        Args:
            timeout (int, optional): Timeout in seconds. Defaults to None.
        """
        return await self.api.create(
            module_model=("pyproxmox_ve.models.qemu", "QemuReboot"),
            endpoint=f"{self.base_endpoint}/status/reboot",
            obj_in=kwargs,
            data_key="success"
        )

    async def reset(self, **kwargs) -> bool:
        """Reset a qemu.

        Args:
        """
        return await self.api.create(
            module_model=("pyproxmox_ve.models.qemu", "QemuReset"),
            endpoint=f"{self.base_endpoint}/status/reset",
            obj_in=kwargs,
            data_key="success"
        )
    
    async def resume(self, **kwargs) -> bool:
        """Resume a qemu.

        Args:
            nocheck (bool, optional): Nocheck. Defaults to None.
            skiplock (bool, optional): Skiplock. Defaults to None.
        """
        return await self.api.create(
            module_model=("pyproxmox_ve.models.qemu", "QemuResume"),
            endpoint=f"{self.base_endpoint}/status/resume",
            method="POST",
            obj_in=kwargs,
            data_key="success"
        )
    
    async def shutdown(self, **kwargs) -> bool:
        """Shutdown a qemu.

        Args:
            forceShutdown (bool, optional): Force shutdown. Defaults to False.
            keepAlive (bool, optional): Keep alive. Defaults to False.
            skiplock (bool, optional): Skiplock. Defaults to None.
            timeout (int, optional): Timeout in seconds. Defaults to None.
        """
        return await self.api.create(
            module_model=("pyproxmox_ve.models.qemu", "QemuShutdown"),
            endpoint=f"{self.base_endpoint}/status/shutdown",
            obj_in=kwargs,
            data_key="success"
        )

    async def start (self, **kwargs) -> bool:
        """Start a qemu.

        Args:
            forceCpu (str, optional): Override QEMU's -cpu argument with the given string. Defaults to None.
            machine (str, optional): Specify the QEMU machine. Defaults to None.
            migratedFrom (str, optional): The cluster node name. Defaults to None.
            migrationNetwork (str, optional): CIDR of the (sub) network that is used for migration. Defaults to None.
            migrationType (str, optional): Migration traffic is encrypted using an SSH tunnel by default. On secure, completely private networks this can be disabled to increase performance. Defaults to None.
            skiplock (bool, optional): Ignore locks - only root is allowed to use this option. Defaults to None.
            stateUri (str, optional): Some command save/restore state from this location. Defaults to None.
            targetStorage (str, optional): Mapping from source to target storages. Providing only a single storage ID maps all source storages to that storage. Providing the special value '1' will map each source storage to itself. Defaults to None.
            timeout (int, optional): Wait maximal timeout seconds. Defaults to None.
        """
        return await self.api.create(
            module_model=("pyproxmox_ve.models.qemu", "QemuStart"),
            endpoint=f"{self.base_endpoint}/status/start",
            method="POST",
            obj_in=kwargs,
            data_key="success"
        )
    
    async def stop(self, **kwargs) -> bool:
        """Stop a qemu.

        Args:
            forceStop (bool, optional): Force stop. Defaults to False.
            keepActive (bool, optional): Do not deactivate storage volumes. Defaults to False.
            migratedFrom (str, optional): The cluster node name. Defaults to None.
            overruleShutdown (bool, optional): Try to abort active 'qmshutdown' tasks before stopping. Defaults to False.
            skiplock (bool, optional): Ignore locks - only root is allowed to use this option. Defaults to None.
            timeout (int, optional): Wait maximal timeout seconds. Defaults to None.
        """
        return await self.api.create(
            module_model=("pyproxmox_ve.models.qemu", "QemuStop"),
            endpoint=f"{self.base_endpoint}/status/stop",
            method="POST",
            obj_in=kwargs,
            data_key="success"
        )

    async def suspend(self, **kwargs) -> bool:
        """Suspend a qemu.
        
        Args:
            skiplock (bool, optional): Ignore locks - only root is allowed to use this option. Defaults to None.
            statestorage (str, optional): The storage for the VM state. Defaults to None.
            todisk (bool, optional): If set, suspends the VM to disk. Will be resumed on next VM start. Defaults to None.
        """
        return await self.api.create(
            module_model=("pyproxmox_ve.models.qemu", "QemuSuspend"),
            endpoint=f"{self.base_endpoint}/status/suspend",
            obj_in=kwargs,
            data_key="success"
        )