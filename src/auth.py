import json
import requests
from cryptoJS import CryptoJS
from typing import Tuple, Dict

from settings import get_settings

# load settings from .env
settings = get_settings()

def auth() -> Tuple[Dict[str, str], requests.Session]:
    """
    ----
    auth
    ----
    From the values in .env, this with auth with the modem
    and return the dictionary of auth values and the session
    used to auth (which contains the sid cookie)
    """
    # get nonce, pubkey and random_key
    resp = requests.get(f"http://{settings.router_ip}/login_web_app.cgi?nonce")
    # write to file for debugging
    # with open("login_web_app_nonce.txt", "w") as f:
    #     f.write(f"Status Code: {resp.status_code}\nHeaders: {resp.headers}\nContent: {resp.text}\n")

    nonce_json = json.loads(resp.text)

    with open("nonce_data", "w") as f:
        f.write(f"nonce: {nonce_json['nonce']}\nrandomKey: {nonce_json['randomKey']}\niterations: {nonce_json['iterations']}\npubkey: {nonce_json['pubkey']}")
    # print(
    #     f"Status Code: {resp.status_code}\nHeaders: {resp.headers}\nContent: {resp.json}\n"
    # )


    # get salt
    userhash = CryptoJS.sha256url(settings.username, nonce_json['nonce'])
    data = {'userhash': userhash, 'nonce': CryptoJS.base64url_escape(nonce_json['nonce'])}
    resp = requests.post(f"http://{settings.router_ip}//login_web_app.cgi?salt", data=data)
    salt_json = json.loads(resp.text)
    salt = salt_json['alati']

    pass_hash = salt + settings.password
    if nonce_json['iterations'] >= 1:
        pass_hash = CryptoJS.sha256_single(pass_hash)

    # currently don't require below loop as iterations
    # is always 1
    # for i in range(nonce_json['iterations'], 1):
    #     print(f"went into loop {i}")
    login_hash = CryptoJS.sha256(settings.username, pass_hash.lower())
    response = CryptoJS.sha256url(login_hash, nonce_json['nonce'])
    random_key_hash = CryptoJS.sha256url(nonce_json['randomKey'], nonce_json['nonce'])

    data = {'userhash': userhash}
    data['RandomKeyhash'] = random_key_hash
    data['response'] = response
    data['nonce'] = CryptoJS.base64url_escape(nonce_json['nonce'])

    enckey = CryptoJS.random_words(4)
    enciv = CryptoJS.random_words(4)

    data['enckey'] = CryptoJS.base64url_escape(enckey)
    data['enciv'] = CryptoJS.base64url_escape(enciv)

    sess = requests.Session()
    resp = sess.post(f"http://{settings.router_ip}//login_web_app.cgi", data=data)
    login_data = json.loads(resp.text)
    print(login_data)

    if login_data['result'] != 0:
        print(data)

    return login_data, sess


# userhash
# lO-bCUdUNso8u1CTvl6M8hWCNwJmsyGW-gdCSpr_2HU.
# f6a_MzRIvuSnBcebf6w2IsPBsfSbYyWDCfUrSR8Yfb8.
