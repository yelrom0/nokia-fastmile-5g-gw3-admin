# Nokia Fastmile 5G 3 Admin

This code is designed to auth and administer the Fastmile 5G Gateway via Python, 
in order to more easily automate tasks and eventually integrate the device into Home Assistant

## Running

1. Copy `default.env` to `.env` and fill in values
2. Create folder `/usr/local/bin/restart-modem`
3. Copy `restart-modem-python.sh`, `requirements.txt`, `.env` and entire `./src` folder to `/usr/local/bin/restart-modem/` if you place these in a folder other than mentioned here, the paths will need to be updated in `restart-modem.service` and `./src/settings.py`
4. Copy contents of `systemd` folder (not the folder itself) to `/etc/systemd/system`
5. Run the commands (in order):
    - `systemctl daemon-reload`
    - `systemctl enable restart-modem.timer`
    - `systemctl start restart-modem.timer`

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
sent: C-_ZZqOEDlV_puDNl36KsGqZK4V0MedIpHPNtmhEZWI.
resp: C+/ZZqOEDlV/puDNl36KsGqZK4V0MedIpHPNtmhEZWI=

nonce: + converted to -, / converted to _, = converted to .

l = iterations
f = userhash = cryptoJS.sha256url(username, nonce)
```