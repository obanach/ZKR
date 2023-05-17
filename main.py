from src.utils import Color
from src.zad2 import RSAAlgorithm, DHCAlgorithm


def runRSA():
    rsa = RSAAlgorithm(True)
    public, private = rsa.generate(31, 19)

    msg = "Some random text to encrypt and decrypt"
    code = rsa.encrypt(public, msg)
    decrypted = rsa.decrypt(private, code)

    print(f"Message: {Color.OKBLUE}{msg}{Color.DEFAULT}")
    print(f"Public key: {Color.BRIGHT_RED}{public}{Color.DEFAULT}")
    print(f"Private key: {Color.BRIGHT_RED}{private}{Color.DEFAULT}")
    print(f"Decrypted message: {Color.OKBLUE}{decrypted}{Color.DEFAULT}")


def runDH():
    dh = DHCAlgorithm(True)
    dh.run()


if __name__ == '__main__':
    # runRSA()
    runDH()
