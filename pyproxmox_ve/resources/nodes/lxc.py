from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pyproxmox_ve.models.lxe import (
  LxeReboot,
  LxeShutdown,
  LxeStart,
  LxeStop
)

if TYPE_CHECKING:
    from pyproxmox_ve.api import ProxmoxVEAPI

class NodeLxcAPI:
    def __init__(self, api: ProxmoxVEAPI, base_endpoint: str) -> None:
        self.api = api
        self.base_endpoint = base_endpoint
        
    async def get_status(self) -> dict:
        """Get the status of a LXC container.

        Args:
        """
        return await self.api.query(
            endpoint=f"{self.base_endpoint}/status/current",
            method="GET",
        )
   
    async def reboot(self, timeout: Optional[int] = None) -> None:
        """Reboot a LXC container.

        Args:
            timeout:    Timeout in seconds (optional).
        """
        await self.api.create(
            endpoint=f"{self.base_endpoint}/status/reboot",
            obj_in=LxeReboot(timeout=timeout),
        )

    async def resume(self) -> None:
        """Resume a LXC container.

        Args:
        """
        await self.api.create(
            endpoint=f"{self.base_endpoint}/status/resume",
        )

    async def shutdown(self, timeout: Optional[int] = 60, forceStop: Optional[bool] = False) -> None:
        """Shutdown a LXC container.

        Args:
            timeout:    Timeout in seconds (optional).
            forceStop:  Force stop the container (optional).
        """
        await self.api.create(
            endpoint=f"{self.base_endpoint}/status/shutdown",
            obj_in=LxeShutdown(timeout=timeout, forceStop=forceStop),
        )
    
    async def start(self, debug: Optional[bool] = False, skiplock: Optional[bool] = None) -> None:
        """Start a LXC container.

        Args:
            debug:      Enable debug logging (optional).
            skiplock:   Skip the lock (optional).
        """
        await self.api.create(
            endpoint=f"{self.base_endpoint}/status/start",
            obj_in=LxeStart(debug=debug, skiplock=skiplock),
        )

    async def stop(self, overrule_shutdown: Optional[bool] = False, skiplock: Optional[bool] = None) -> None:
        """Stop a LXC container.

        Args:
            overrule_shutdown:  Overrule the shutdown (optional).
            skiplock:           Skip the lock (optional).
        """
        await self.api.create(
            endpoint=f"{self.base_endpoint}/status/stop",
            obj_in=LxeStop(overrule_shutdown= overrule_shutdown, skiplock=skiplock),
        )
    
    async def suspend(self) -> None:
        """Suspend a LXC container.

        Args:
        """
        await self.api.create(
            endpoint=f"{self.base_endpoint}/status/suspend",
        )
