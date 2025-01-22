# Nokia Fastmile 5G 3 Admin

This code is designed to auth and administer the Fastmile 5G Gateway via Python, 
in order to more easily automate tasks and eventually integrate the device into Home Assistant

## APIs

### Auth

- Endpoint: {router_address}/login_web_app.cgi?nonce
- Type: GET
- Response:
```
{
    iterations: int
    nonce: str
    pubkey: str
    randomKey: str
}
```
sent: C-_ZZqOEDlV_puDNl36KsGqZK4V0MedIpHPNtmhEZWI.
resp: C+/ZZqOEDlV/puDNl36KsGqZK4V0MedIpHPNtmhEZWI=

nonce: + converted to -, / converted to _, = converted to .