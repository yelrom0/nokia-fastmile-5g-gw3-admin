this.backendservice.getnonce().subscribe({
    next: r => {
        if (r.nonce) {
            let o = ""
              , l = r.iterations
              , h = "";
            const f = cryptoJS.sha256url(e.username, r.nonce);
            this.backendservice.getSalt(`userhash=${f}&nonce=${cryptoJS.base64url_escape(r.nonce)}`).subscribe({
                next: y => {
                    y && (h = y.alati,
                    sessionStorage.setItem("alati", h)),
                    o = l >= 1 ? fs.SHA256(h + e.password).toString() : h + e.password;
                    for (let ue = 1; ue < l; ue++) {
                        var D = fs.enc.Hex.parse(o);
                        o = fs.SHA256(D).toString()
                    }
                    const P = cryptoJS.sha256(e.username, o.toLowerCase())
                      , H = cryptoJS.sha256url(P, r.nonce)
                      , U = cryptoJS.sha256url(r.randomKey, r.nonce);
                    let W = `userhash=${f}&RandomKeyhash=${U}&response=${H}&nonce=${cryptoJS.base64url_escape(r.nonce)}`;
                    const Z = sjcl.codec.base64
                      , se = Z.fromBits(sjcl.random.randomWords(4, 0))
                      , K = Z.fromBits(sjcl.random.randomWords(4, 0));
                    W += `&enckey=${cryptoJS.base64url_escape(se)}`,
                    W += `&enciv=${cryptoJS.base64url_escape(K)}`,
                    this.backendservice.login(W).subscribe({
                        next: ue => {
                            0 === ue.result ? (sessionStorage.setItem(ue.sid, `${se} ${K}`),
                            sessionStorage.setItem("token", ue.token),
                            sessionStorage.setItem("sid", ue.sid),
                            sessionStorage.setItem("currentUser", e.username),
                            this.sessionActive.next(!0),
                            this.startSessionExpireTimer(),
                            n = ue,
                            a(n)) : ((-1 === ue.result || -2 === ue.result) && (n = ue),
                            this.closeSession(),
                            a(n))
                        }
                        ,
                        error: () => {
                            this.closeSession(),
                            n = nl.LOGINFAILED,
                            a(n)
                        }
                        ,
                        complete: () => console.info("complete")
                    })
                }
                ,
                error: () => s()
            })
        }
    }
    ,
    error: () => s()
})