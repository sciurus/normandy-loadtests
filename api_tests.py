from molotov import scenario
import os

cdn = os.environ.get('MOLOTOV_USE_CDN', False)
if cdn:
    _DOMAIN = 'normandy-cdn-gcp.stage.mozaws.net'
else:
    _DOMAIN = 'stage.normandy.nonprod.cloudops.mozgcp.net'

print(f"Testing {_DOMAIN}")


@scenario(weight=1)
async def api_endpoint_test(session):
    api_endpoint = f'https://{_DOMAIN}/api/v1/'

    async with session.get(api_endpoint) as resp:
        res = await resp.json()
        assert resp.status == 200
        assert 'action-list' in res
        assert 'action-signed' in res
        assert 'recipe-list' in res
        assert 'recipe-signed' in res
        assert 'reciperevision-list' in res
        assert 'approvalrequest-list' in res
        assert 'classify-client' in res


@scenario(weight=1)
async def recipe_endpoint_test(session):
    recipe_endpoint = f'https://{_DOMAIN}/api/v1/recipe/signed/?enabled=true'
    async with session.get(recipe_endpoint) as resp:
        res = await resp.json()
        assert resp.status == 200
        assert len(res) > 0
        assert 'signature' in res[0]
        assert 'recipe' in res[0]


@scenario(weight=1)
async def action_endpoint_test(session):
    action_endpoint = f'https://{_DOMAIN}/api/v1/action/signed/'
    async with session.get(action_endpoint) as resp:
        res = await resp.json()
        assert resp.status == 200
        assert len(res) > 0
        assert 'signature' in res[0]
        assert 'action' in res[0]


@scenario(weight=1400)
async def classify_client_test(session):
    classify_client_endpoint = f'https://{_DOMAIN}/api/v1/classify_client/'
    async with session.get(classify_client_endpoint) as resp:
        res = await resp.json()
        assert resp.status == 200
        assert 'country' in res
        assert 'request_time' in res

@scenario(weight=8)
async def heartbeat_test(session):
    classify_client_endpoint = f'https://{_DOMAIN}/__heartbeat__'
    async with session.get(classify_client_endpoint) as resp:
        res = await resp.json()
        assert resp.status == 200
        assert 'status' in res
