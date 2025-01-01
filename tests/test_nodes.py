import pytest

from pyproxmox_ve import ProxmoxVEAPI


@pytest.mark.asyncio
async def get_lxc_status(proxmox: ProxmoxVEAPI):
    response = await proxmox.nodes.get_lxc_status(node="proxmox", lxcid=101)
    assert response
    assert response.cpu
    assert response.cpus
    assert response.maxmem
    assert response.mem
    assert response.name

async def get_qemu_status(proxmox: ProxmoxVEAPI):
    response = await proxmox.nodes.get_qemu_status(node="proxmox", vmid=100)
    assert response
    assert response.agent
    assert response.cpu
    assert response.cpus
    assert response.maxmem
    assert response.mem
    assert response.name
