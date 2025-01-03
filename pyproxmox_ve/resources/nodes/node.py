from __future__ import annotations

from typing import TYPE_CHECKING

from pyproxmox_ve.resources.nodes.lxc import NodeLxcAPI
from pyproxmox_ve.resources.nodes.qemu import NodeQemuAPI

if TYPE_CHECKING:
    from pyproxmox_ve.api import ProxmoxVEAPI

class NodeAPI:
    def __init__(self, api: ProxmoxVEAPI, node: str) -> None:
        self.api = api
        self.base_endpoint = f"/nodes/{node}"

    def lxc(self, vmid: int) -> NodeLxcAPI:
        return NodeLxcAPI(api=self.api, base_endpoint=f"{self.base_endpoint}/lxc/{vmid}")
    
    def qemu(self, vmid: int) -> NodeQemuAPI:
        return NodeQemuAPI(api=self.api, base_endpoint=f"{self.base_endpoint}/qemu/{vmid}")


   
