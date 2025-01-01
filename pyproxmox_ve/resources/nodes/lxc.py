from __future__ import annotations

from typing import TYPE_CHECKING

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
   
