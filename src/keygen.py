# input vars
iterations = 1
nonce = "Mo5/Ke/QLSZ+BDKBPfi58Lyzle5tMEnq0ieqROsKhEQ="
pubkey = "-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCjYEjI+CMeQuOcxSe9kItjFBwcC38Ky/VYATqX7PIjLV8yK6GeUIniHXrmiuPH4RU/uTeA/pGMnohMRc9U+BzBuq2wfpSm0Z0QM3mACn0ZRniEwiLvyoFdyesR6kWjfq9ZbzsBrf2/rgw/aYePT67lkVyUQIggOLmECGuQht9CBQIDAQAB-----END PUBLIC KEY-----"
randomKey = "795"

# correct output
out_userhash = "kvj7KlNJd2IauGpXOUyJHEEsR8cKVrtOgoPOpfcHGRM."
out_nonce = "Mo5_Ke_QLSZ-BDKBPfi58Lyzle5tMEnq0ieqROsKhEQ."

# replace = in nonce with .
nonce = nonce.replace("=",".").replace("/","_",).replace("+","-")

if nonce != out_nonce:
    err_msg = f"Nonce value incorrect:\nin: {nonce}\nout: {out_nonce}"
    with open("error.txt", "w") as f:
        f.write(err_msg)
    raise Exception(err_msg)

# generate userhash
