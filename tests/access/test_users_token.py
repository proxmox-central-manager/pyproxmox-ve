from datetime import datetime

import pytest

from pyproxmox_ve import ProxmoxVEAPI
from pyproxmox_ve.exceptions import ProxmoxAPIResponseError


@pytest.mark.asyncio
@pytest.mark.order(before="test_access_users.py::TestAccessUsers::test_delete_user")
class TestAccessUsersToken:
    async def test_get_user_tokens_not_exist(self, proxmox: ProxmoxVEAPI):
        user_tokens = await proxmox.access.users.get_user_tokens(
            user_id="pyproxmox-ve-pytest@pam"
        )
        assert user_tokens is None

    async def test_create_user_token(self, proxmox: ProxmoxVEAPI):
        token_response = await proxmox.access.users.create_user_token(
            user_id="pyproxmox-ve-pytest@pam", token_id="pytest"
        )
        assert token_response
        assert token_response.value
        assert "pyproxmox-ve-pytest@pam" in token_response.full_tokenid

    async def test_get_user_tokens(self, proxmox: ProxmoxVEAPI):
        user_tokens = await proxmox.access.users.get_user_tokens(
            user_id="pyproxmox-ve-pytest@pam"
        )
        assert user_tokens
        assert len(user_tokens) > 0

    async def test_get_user_check_token_dict(self, proxmox: ProxmoxVEAPI):
        user = await proxmox.access.users.get_user(user_id="pyproxmox-ve-pytest@pam")
        assert user
        for token, token_data in user.tokens.items():
            assert token
            assert token_data.expire == 0
            assert token_data.privsep == 1

    async def test_get_user_token(self, proxmox: ProxmoxVEAPI):
        user_token = await proxmox.access.users.get_user_token(
            user_id="pyproxmox-ve-pytest@pam", token_id="pytest"
        )
        assert user_token
        assert user_token.expire == 0
        assert user_token.privsep == 1

    async def test_update_user_token(self, proxmox: ProxmoxVEAPI):
        epoch_update = int(datetime.utcnow().strftime("%s")) + 86400
        await proxmox.access.users.update_user_token(
            user_id="pyproxmox-ve-pytest@pam",
            token_id="pytest",
            expire=epoch_update,
        )

        user_token_updated = await proxmox.access.users.get_user_token(
            user_id="pyproxmox-ve-pytest@pam", token_id="pytest"
        )

        assert user_token_updated
        assert user_token_updated.expire == epoch_update

    async def test_delete_user_token(self, proxmox: ProxmoxVEAPI):
        await proxmox.access.users.delete_user_token(
            user_id="pyproxmox-ve-pytest@pam", token_id="pytest"
        )

    async def test_delete_user_token_not_exist(self, proxmox: ProxmoxVEAPI):
        with pytest.raises(ProxmoxAPIResponseError) as exc_info:
            await proxmox.access.users.delete_user_token(
                user_id="pyproxmox-ve-pytest@pam", token_id="pytest"
            )

        error = exc_info.value
        assert error.status == 500
        assert "no such token" in error.reason