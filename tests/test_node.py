import pytest

from pyproxmox_ve import ProxmoxVEAPI


@pytest.mark.asyncio
async def get_lxc_status(proxmox: ProxmoxVEAPI):
    response = await proxmox.node("proxmox").lxc(101).get_status()
    assert response
    assert response.cpu
    assert response.cpus
    assert response.maxmem
    assert response.mem
    assert response.name

async def get_qemu_status(proxmox: ProxmoxVEAPI):
    response = await proxmox.node("proxmox").qemu(100).get_status()
    assert response
    assert response.agent
    assert response.cpu
    assert response.cpus
    assert response.maxmem
    assert response.mem
    assert response.name
