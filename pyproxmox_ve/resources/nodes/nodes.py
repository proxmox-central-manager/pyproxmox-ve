from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyproxmox_ve.api import ProxmoxVEAPI

class NodesAPI:
    def __init__(self, api: ProxmoxVEAPI) -> None:
        self.api = api
    
    async def get_qemu_status(self, node: str, vmid: int) -> dict:
        """Get the status of a QEMU VM.

        Args:
            node:   Node name
            vmid:   VM ID
        """
        return await self.api.query(
            endpoint=f"/nodes/{node}/qemu/{vmid}/status/current",
            method="GET",
        )
    
    async def get_lxc_status(self, node: str, lxcid: int) -> dict:
        """Get the status of a LXC container.

        Args:
            node:   Node name
            lxcid:  LXC ID
        """
        return await self.api.query(
            endpoint=f"/nodes/{node}/lxc/{lxcid}/status/current",
            method="GET",
        )
   
