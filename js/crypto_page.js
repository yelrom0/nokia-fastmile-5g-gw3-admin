(
    (sjcl.beware &&
      sjcl.beware[
        "CBC mode is dangerous because it doesn't protect message integrity."
      ]) ||
    function () {}
  )();
  
  var cryptoJS = (function () {
    var base64url_escape = function (b64) {
      var out = "";
      for (i = 0; i < b64.length; i++) {
        var c = b64.charAt(i);
        if (c == "+") {
          out += "-";
        } else if (c == "/") {
          out += "_";
        } else if (c == "=") {
          out += ".";
        } else {
          out += c;
        }
      }
      return out;
    };
  
    var encrypt = function (pubkey, plaintext) {
      var aeskey = sjcl.random.randomWords(4, 0);
      var iv = sjcl.random.randomWords(4, 0);
      var pt = sjcl.codec.utf8String.toBits(plaintext);
      var aes = new sjcl.cipher.aes(aeskey);
      var ct = sjcl.mode.cbc.encrypt(aes, pt, iv);
  
      var rsa = new JSEncrypt();
      if (rsa.setPublicKey(pubkey) == false) return fasle;
  
      var base64url = sjcl.codec.base64url;
      var base64 = sjcl.codec.base64;
      var aesinfo = base64.fromBits(aeskey) + " " + base64.fromBits(iv);
      var ck = rsa.encrypt(aesinfo);
      if (ck == false) return false;
  
      return {
        ct: base64url.fromBits(ct),
        ck: base64url_escape(ck),
      };
    };
  
    var aes_decrypt = function (ciphertext) {
      var sid = sessionStorage.getItem("sid");
      var keyinfo = sessionStorage.getItem(sid);
      if (keyinfo && ciphertext.length > 0) {
        var key_iv = keyinfo.split(" ");
        var key = sjcl.codec.base64.toBits(key_iv[0]);
        var iv = sjcl.codec.base64.toBits(key_iv[1]);
        var ct = sjcl.codec.base64.toBits(ciphertext);
        var aes = new sjcl.cipher.aes(key);
        try {
          var pt = sjcl.mode.cbc.decrypt(aes, ct, iv);
          return sjcl.codec.utf8String.fromBits(pt);
        } catch (err) {
          console.log(err.message);
        }
      }
  
      return ciphertext;
    };
  
    var encrypt_post_data = function (pubkey, plaintext) {
      var p = encrypt(pubkey, plaintext);
      return "encrypted=1&ct=" + p.ct + "&ck=" + p.ck;
    };
  
    var sha256 = function (val1, val2) {
      var out = sjcl.hash.sha256.hash(val1 + ":" + val2);
      return sjcl.codec.base64.fromBits(out);
    };
  
    var sha256url = function (val1, val2) {
      return base64url_escape(sha256(val1, val2));
    };
  
    var sha256url = function (val1, val2) {
      return base64url_escape(sha256(val1, val2));
    };
  
    var clearModalReference = function () {
      document.getElementsByTagName("body")[0].classList.remove("modal-open");
      clearElementByTagName("ngb-modal-backdrop");
      clearElementByTagName("ngb-modal-window");
    };
    var clearElementByTagName = function (element) {
      var element = document.getElementsByTagName(element),
        index;
      for (index = element.length - 1; index >= 0; index--) {
        element[index].parentNode.removeChild(element[index]);
      }
    };
  
    return {
      encrypt: encrypt,
      encrypt_post_data: encrypt_post_data,
      sha256: sha256,
      sha256url: sha256url,
      base64url_escape: base64url_escape,
      aes_decrypt: aes_decrypt,
      clearModalReference: clearModalReference,
    };
  })();
  