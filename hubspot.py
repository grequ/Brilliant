from hubspot import HubSpot 

from hubspot.auth.oauth import ApiException

try:
    tokens = api_client.auth.oauth.default_api.create_token(
        grant_type="authorization_code",
        redirect_uri='http://localhost',
        client_id='client_id',
        client_secret='client_secret',
        code='code'
    )
except ApiException as e:
    print("Exception when calling create_token method: %s\n" % e)