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

    async def reboot(self, timeout: Optional[int] = None) -> None:
        """Reboot a qemu.

        Args:
            timeout (int, optional): Timeout in seconds. Defaults to None.
        """
        return await self.api.create(
            endpoint=f"{self.base_endpoint}/status/reboot",
            obj_in=QemuReboot(timeout=timeout),
        )

    async def reset(self, skiplock: Optional[bool] = None) -> None:
        """Reset a qemu.

        Args:
        """
        return await self.api.query(
            endpoint=f"{self.base_endpoint}/status/reset",
            obj_in=QemuReset(skiplock=skiplock),
        )
    
    async def resume(self, nocheck: Optional[bool] = None, skiplock: Optional[bool] = None) -> None:
        """Resume a qemu.

        Args:
            nocheck (bool, optional): Nocheck. Defaults to None.
            skiplock (bool, optional): Skiplock. Defaults to None.
        """
        return await self.api.create(
            endpoint=f"{self.base_endpoint}/status/resume",
            obj_in=QemuResume(nocheck=nocheck, skiplock=skiplock),
        )
    
    async def shutdown(self, forceShutdown: Optional[bool] = False, keepAlive: Optional[bool] = False, skiplock: Optional[bool] = None,  timeout: Optional[int] = None,) -> None:
        """Shutdown a qemu.

        Args:
            forceShutdown (bool, optional): Force shutdown. Defaults to False.
            keepAlive (bool, optional): Keep alive. Defaults to False.
            skiplock (bool, optional): Skiplock. Defaults to None.
            timeout (int, optional): Timeout in seconds. Defaults to None.
        """
        return await self.api.create(
            endpoint=f"{self.base_endpoint}/status/shutdown",
            obj_in=QemuShutdown(forceShutdown=forceShutdown, keepAlive=keepAlive, skiplock=skiplock, timeout=timeout),
        )

    async def start (self, forceCpu: Optional[str] = None, machine: Optional[str] = None, migratedFrom: Optional[str] = None, migrationNetwork: Optional[str] = None, migrationType: Optional[str] = None, skiplock: Optional[bool] = None, stateUri: Optional[str] = None, targetStorage: Optional[str] = None, timeout: Optional[int] = None) -> None:
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
            endpoint=f"{self.base_endpoint}/status/start",
            obj_in=QemuStart(forceCpu=forceCpu, machine=machine, migratedFrom=migratedFrom, migrationNetwork=migrationNetwork, migrationType=migrationType, skiplock=skiplock, stateUri=stateUri, targetStorage=targetStorage, timeout=timeout),
        )
    
    async def stop(self, forceStop: Optional[bool] = False, keepActive: Optional[bool] = False, migratedFrom: Optional[str] = None, overruleShutdown: Optional[bool] = False, skiplock: Optional[bool] = None, timeout: Optional[int] = None) -> None:
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
            endpoint=f"{self.base_endpoint}/status/stop",
            obj_in=QemuStop(forceStop=forceStop, keepActive=keepActive, migratedFrom=migratedFrom, overruleShutdown=overruleShutdown, skiplock=skiplock, timeout=timeout),
        )

    async def suspend(self, skiplock: Optional[bool] = None, statestorage: Optional[str] = None, todisk: Optional[bool] = False) -> None:
        """Suspend a qemu.
        
        Args:
            skiplock (bool, optional): Ignore locks - only root is allowed to use this option. Defaults to None.
            statestorage (str, optional): The storage for the VM state. Defaults to None.
            todisk (bool, optional): If set, suspends the VM to disk. Will be resumed on next VM start. Defaults to None.
        """
        return await self.api.create(
            endpoint=f"{self.base_endpoint}/status/suspend",
            obj_in=QemuSuspend(skiplock=skiplock, statestorage=statestorage, todisk=todisk),
        )