# from os import path as os_path
# from sys import path as sys_path
# src = os_path.abspath('..')
# sys_path.append(src)
from test_data import (
    username,
    nonce,
    randomKey,
    iterations,
    salt,
    userhash as uh_test,
    RandomKeyHash as RKH_test,
)
from cryptoJS import CryptoJS

userhash = CryptoJS.sha256url(username, nonce)
print(f"Userhash: {userhash}")
if userhash != uh_test:
    err_msg = f"Userhash value incorrect:\nOur value: {userhash}\nCorrect value: {uh_test}"
    with open("error.txt", "w") as f:
        f.write(err_msg)
    raise Exception(err_msg)

RandomKeyHash = CryptoJS.sha256url(randomKey, nonce)
print(f"RandomKeyHash: {RandomKeyHash}")
if RandomKeyHash != RKH_test:
    err_msg = f"RandomKeyHash value incorrect:\nOur value: {RandomKeyHash}\nCorrect value: {RKH_test}"
    with open("error.txt", "w") as f:
        f.write(err_msg)
    raise Exception(err_msg)

if iterations > 0:
    pass
"""
salt = response_from_salt_endpoint["alati"]
if iterations > 0: 
    o = SHA256(salt + password).toString()
else:
    o = salt + password
for i in range(1, iterations):
    D = CryptoJS.string_to_hex(o)
    o = CryptoJS.sha256(D).toString()

P = CryptoJS.sha256(username, o.toLower())
response = CryptoJS.sha256url(P, nonce)

se = base64(CryptoJS.random_words(4)) # 4 words, each word is 32 bits
K = base64(CryptoJS.random_words(4)) # 4 words, each word is 32 bits

enckey = CryptoJS.base64url_escape(se)
enciv = CryptoJS.base64url_escape(K)
"""