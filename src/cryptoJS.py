from base64 import b64encode
from hashlib import sha256 as sha256hash
from random import randbytes


class CryptoJS():

    @classmethod
    def base64url_escape(cls, b64: str) -> str:
        """
        ----------------
        base64url_escape
        ----------------
        Converts a base64 string into a format suitable for urls.
        
        :param: b64 - str - The base64 string to format

        :return: str - The base64 string, formatted for use in urls.
        """
        return (
            b64
            .replace("=",".")
            .replace("/","_",)
            .replace("+","-")
        )


    @classmethod
    def sha256(cls, val1: str, val2: str) -> str:
        """
        ------
        sha256
        ------
        Takes two values (val1, val2), 
        combines the two values with a : between them,
        sha256 encodes, the value, then returns the
        b64encoded value of of the sha256 bytes
        """
        out = sha256hash((val1 + ":" + val2).encode()).digest()
        return b64encode(out).decode()
    
    @classmethod
    def sha256_single(cls, val: str) -> str:
        """
        ------
        sha256_single
        ------
        Takes a single value (val1), sha256 encodes the value, 
        then returns the b64encoded value of of the sha256 bytes
        """
        return sha256hash((val).encode()).hexdigest()
        # return b64encode(out).decode()

    @classmethod
    def sha256url(cls, val1: str, val2: str) -> str:
        """
        ---------
        sha256url
        ---------
        Takes val1 and val2, hashes them using sha256
        and converts them into a base64 string with url formatting
        """

        return cls.base64url_escape(cls.sha256(val1, val2))
    
    @classmethod
    def bytes_to_base64(cls, byt: bytes) -> str:
        """
        ------
        bytes_to_base64
        ------
        Converts bytes to a base_64 string
        """
        # if this doesn't work, try removing line below
        b64str = b64encode(byt)
        return b64str.decode()
    
    @classmethod
    def random_words(cls, num_words: int) -> str:
        """
        ------
        random_words
        ------
        Generates a random base64 string of num_words words, each word being 32 bits
        """        

        return cls.bytes_to_base64(randbytes(num_words * 4))
