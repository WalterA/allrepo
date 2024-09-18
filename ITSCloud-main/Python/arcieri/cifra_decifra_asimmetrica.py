
# creazione environment
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
#Per iniziare generariamo una coppia di chiavi
# Generating RSA Key Pair

key_pair = RSA.generate(2048)
"""
print(key_pair.export_key())
public_key = key_pair.publickey()
print(public_key.export_key())
exit(0)
"""
sPriv='-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA1RejPEDjJUCe5GvGp2C/1UE+CetjnDc3vKpVnEnZMhuvi/cl\nJO8kuVwuYQB3IspQgLejg8diUQl6ke8423geYyXEJXM+cUlv4bhwqMGUomE5WI4z\nK7VE9evRbpBcWizAL5DKl9jo2m6J7kbHKbrIV+r7B3Zf3ieNDhE3+dOIt8yOPshq\nG5d2v80keug1HFuiDPMpp/+nfSaJyrVhqU1den4T+DNXIq2nzH7xSkXX1/tMXboY\nFsXjHN3P4i2SlV/lyY6M+ZOphaIBwht2uZ1e4zWC1Af/lFMbSOZXxdjdes3dfDf2\nPvN6J2MuAhz3VCjvCqAw3E4VINVwT14WS9OUnQIDAQABAoIBADrQE1WF8ytM8o3I\n0UNRCKErKJxEQ3HSK6f+uzIvj6qsyX6v76iJ+HDQaFyNbFRF0oI0LQUp+pCzNQki\nJWctd/WVbtWHQSyzQBXkefOZuhQ3EUTHuofNuALH2z3Qyix5PXHjXIccbugaqicB\nkeaKjtD1IeOlYEBIWj4PsotZPtq7MXnitgKYzm69V5IgUuMpKpmYIyJJsN5nDrgP\nQw2rYIeSkz2vE+sBtwyffVRNXE+JMCSVjvVXVuo4uMDOyBR8U8LYYOJ7PDcdD89e\nHVyoSY/d2jYzfHXudMuaHVEnQdsWtTGIwxMHkxkWlkaTm9Cf/WJQmVqIAm/nnCTG\nVuxRKWECgYEA6Q9mNM7H3nZEXykau6Uf587G8TjI84+CnTOT/dMomKU1dF6a1qq6\n96WRHaOjWh5jKXXVOV9qkV2QNft6tV4JMN+Ra072aYTN/uRZhqyQFp1qci1lzjSj\noUmnBsUYqO4jUSaX9eYYzou8HU6eiiO3V0yoDLhf5jYE4TAZn2AreW8CgYEA6hEX\n70CZdYio80vNoUV4cohoun6oONoqs6artLjXPFsvG7CpH4TjmaTa5APHu7Pa8XVX\n+AmU4+XN9JJ3aKmFAwzqn4gFxkECG9N7yPMLKABlIkGrjYSrIqwK/mqM/D5rl21R\nW8dS0+gOG7la1xtxgfhr6ur1lfPX+X2pS4SfFLMCgYBU22yFUbzoPPuMAnVfWTIS\nvvEkp15TgC84ea0qwBWJ7q1V35RVEPjeboQ13Hz/tQy57dNi/mDY6M43OYdmPgTu\nrJhQEAIcTWSLqC0IohAci9hUFj95IyVo9l5AUsc1yu9E/t5ZhBwIKEyoBxYmifaZ\nbKnLZ95S/dws+cx6gROTNQKBgQCKCDqNJRNadJTtpS5GhKlbIYZhNIAPxtiXyRpJ\nIRgMx9koAy45ICz4VnefL3uB/baH3iNaaowbOVITgKxaVF3URrG2EokVORD9R+If\nxvQ1SsZZRVDdy/cAI2T4U+2Ac28PhbAM56a4wIhRYSVo5Q4zD0TU7GqXW41p2+kS\nV8tYcQKBgQDJakY4k3vIH8Ty4YIwoQxyGZWIvuswE6DRRm44rL2AWRWB2Crr/0Uq\n+Zhti2VvrhnmMq6h6FKqgT+7ifLm2IiMbV251wAawP5LW0HNvBZg7dusrcnVfYrd\nslmd+xBhesrQ6HSSGdX12o0veahceNfkBNECRqrFGf/HIIxwmt68RQ==\n-----END RSA PRIVATE KEY-----'
sPub='-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1RejPEDjJUCe5GvGp2C/\n1UE+CetjnDc3vKpVnEnZMhuvi/clJO8kuVwuYQB3IspQgLejg8diUQl6ke8423ge\nYyXEJXM+cUlv4bhwqMGUomE5WI4zK7VE9evRbpBcWizAL5DKl9jo2m6J7kbHKbrI\nV+r7B3Zf3ieNDhE3+dOIt8yOPshqG5d2v80keug1HFuiDPMpp/+nfSaJyrVhqU1d\nen4T+DNXIq2nzH7xSkXX1/tMXboYFsXjHN3P4i2SlV/lyY6M+ZOphaIBwht2uZ1e\n4zWC1Af/lFMbSOZXxdjdes3dfDf2PvN6J2MuAhz3VCjvCqAw3E4VINVwT14WS9OU\nnQIDAQAB\n-----END PUBLIC KEY-----'#ore dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair= RSA.import_key(sPriv)
public_key= RSA.import_key(sPub)
# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")

#sPubCollega='-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwdGJCI2pMmq/oHUUEDy4\nowwNq7Sw3f77IcvzNACBlqFGKCcJwH8pwbrquZwkn2sZ0bsYVJTKvnC0J2p4DcN+\nui2Yn0fRo9xVtdl4b+Va4zx6ox4vlnOKmz8t1S4Tx0B9CYmuEr4/VQpCqYkwbyDv\nXO46tAPfCwYcTqEwBLzDXG7suVv8eDMnHpSAE0XFVNA+S2At+HT67PmfGWEQlZMp\nsBBXRXgEE3pjLBTSDrUtKgQ8IdcamJnXBGxo86r2w8whY5DcPjU2HremUviWEVAP\n7dy2LVAwNpAWSCpo+7ZbM1s99mlhVRxPYQbFWzYE/TXe3UEI8fbxNXLqiwYmzl5k\nhwIDAQAB\n-----END PUBLIC KEY-----'
# Example usage
#public_key_collega=RSA.import_key(sPubCollega)
#message = "Ciao Franco sono Vieri"
#encrypted_message = encrypt_message(message, public_key_collega)
#print("Encrypted Message:", encrypted_message)"""
cifrato='sgAN1vKiQOPohGlOJmepSxVWEem/v8MTAI34N1UmWYZaEqpDR2CuafNrokPe54zfAXfdueVkdyHGFfsx/HuGdtJwS+NCmUUx7N2ShP5uIlh91wPBpeW0IkOFu5yDL2KomdwHkm1bU4Dh2Sy5Pb+2QG2LFx1ofbWqd5DCGcZ7PxneSVDSadXMhcFtG8s1r7M1lJS1kcWo1aguP2oY+AvAKarwhZRXyMj4z90pZJbfpoSiQozt4J3KR8pMfKooNQUYYLDTcxjpuhZ5GDSvCC6rgAS116Z3pfzWfdT/GqQi0CfQtT4BnfyOANLia7zzCiILBD4FGDC1/+hGfXP+l3Q2eg=='
decrypted_message = decrypt_message(cifrato, key_pair)
print("Decrypted Message:", decrypted_message)
"""
print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
"""