import string

from src.utils import Color
from src.zad2 import RSAAlgorithm, DHCAlgorithm
from src.zad3 import VisualCryptography
from src.zad6 import ImageSteganography


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

def runVisualCrypto():
    vc = VisualCryptography('secret.png')
    vc.run()

def runSteganography(msg: string = None, decode: bool = False):
    IMAGE = 'politechnika.png'
    st = ImageSteganography(IMAGE)

    if msg:
        st.encode(msg)
        print(f"Encoded message: {Color.OKBLUE}{msg}{Color.DEFAULT} in image: {Color.BRIGHT_RED}{IMAGE}{Color.DEFAULT}")


    if decode:
        decodedMessage = st.decode()
        if not decodedMessage:
            print(f"Image: {Color.BRIGHT_RED}{IMAGE}{Color.DEFAULT} does not contain a message")
        else:
            print(
                f"Decoded message: {Color.OKBLUE}{st.decode()}{Color.DEFAULT} from image: {Color.BRIGHT_RED}{IMAGE}{Color.DEFAULT}")



if __name__ == '__main__':
    # runRSA()
    # runDH()
    # runVisualCrypto()
    runSteganography("Siemaa", decode=True)

