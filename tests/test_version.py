import pytest

from pyproxmox_ve import ProxmoxVEAPI


@pytest.mark.asyncio
async def test_version_endpoint(proxmox: ProxmoxVEAPI):
    response = await proxmox.version.get_version()
    assert response
    assert response.version
    assert response.repoid
    assert response.release
