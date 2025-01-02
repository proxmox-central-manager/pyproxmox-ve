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
   
    async def reboot(self, timeout: Optional[int] = None) -> bool:
        """Reboot a LXC container.

        Args:
            timeout:    Timeout in seconds (optional).
        """
        await self.api.http_request(
            endpoint=f"{self.base_endpoint}/status/reboot",
            method="POST",
            obj_in=LxeReboot(timeout=timeout),
            data_key="success"
        )

    async def resume(self) -> None:
        """Resume a LXC container.

        Args:
        """
        await self.api.http_request(
            endpoint=f"{self.base_endpoint}/status/resume",
            method="POST",
            data_key="success"
        )

    async def shutdown(self, timeout: Optional[int] = 60, forceStop: Optional[bool] = False) -> bool:
        """Shutdown a LXC container.

        Args:
            timeout:    Timeout in seconds (optional).
            forceStop:  Force stop the container (optional).
        """
        await self.api.http_request(
            endpoint=f"{self.base_endpoint}/status/shutdown",
            method="POST",
            obj_in=LxeShutdown(timeout=timeout, forceStop=forceStop),
            data_key="success"
        )
    
    async def start(self, debug: Optional[bool] = False, skiplock: Optional[bool] = None) -> bool:
        """Start a LXC container.

        Args:
            debug:      Enable debug logging (optional).
            skiplock:   Skip the lock (optional).
        """
        await self.api.http_request(
            endpoint=f"{self.base_endpoint}/status/start",
            method="POST",
            obj_in=LxeStart(debug=debug, skiplock=skiplock),
            data_key="success"
        )

    async def stop(self, overrule_shutdown: Optional[bool] = False, skiplock: Optional[bool] = None) -> bool:
        """Stop a LXC container.

        Args:
            overrule_shutdown:  Overrule the shutdown (optional).
            skiplock:           Skip the lock (optional).
        """
        await self.api.http_request(
            endpoint=f"{self.base_endpoint}/status/stop",
            method="POST",
            obj_in=LxeStop(overrule_shutdown= overrule_shutdown, skiplock=skiplock),
            data_key="success"
        )
    
    async def suspend(self) -> bool:
        """Suspend a LXC container.

        Args:
        """
        await self.api.http_request(
            endpoint=f"{self.base_endpoint}/status/suspend",
            method="POST",
            data_key="success"
        )
