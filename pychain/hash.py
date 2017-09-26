import hashlib

def hash256(preimage):
    if type(preimage) is int:
        preimage = bin(preimage)

    preimage = preimage.encode()

    return hashlib.sha256(hashlib.sha256(preimage).hexdigest().encode()).hexdigest().encode()
