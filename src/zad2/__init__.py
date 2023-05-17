from sympy import randprime
from src.utils import Color
import random


class RSAAlgorithm:

    def __init__(self, debug: bool = False):
        self.debug = debug

    def generate(self, x: int = None, y: int = None):

        if not x:
            p = randprime(10 ** 3, 10 ** 6)
        else:
            p = x

        if not y:
            q = randprime(10 ** 3, 10 ** 6)
        else:
            q = y

        n = p * q
        phi = (p - 1) * (q - 1)

        e = None
        d = None
        while True:
            e = randprime(1, phi)
            d = pow(e, -1, phi)
            if self.gcd(e, phi) == 1 and e != d:
                # if e != d:
                break

        if self.debug:
            print(f"p = {p}")
            print(f"q = {q}")
            print(f"n = {n}")
            print(f"Φ = {phi}")
            print(f"e = {e}")
            print(f"d = {d}")

        return (e, n), (d, n)

    def encrypt(self, public_key, message):
        e, n = public_key

        if self.debug:
            print(
                f"Encrypting message: {Color.OKBLUE}{message}{Color.DEFAULT} with public key: {Color.BRIGHT_RED}{public_key}{Color.DEFAULT}")

        code = []
        for i in message:
            code.append(pow(ord(i), e, n))
        return code

    def decrypt(self, private_key, code):
        d, n = private_key

        if self.debug:
            print(
                f"Decrypting message: {Color.OKBLUE}{code}{Color.DEFAULT} with public key: {Color.BRIGHT_RED}{private_key}{Color.DEFAULT}\n")

        msg = []
        for i in code:
            msg.append(chr(pow(i, d, n)))

        return ''.join(msg)

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)


class DHCAlgorithm:

    def __init__(self, debug: bool = False):
        self.debug = debug
        self.n = randprime(10 ** 5, 10 ** 6)

    def roots(self, max_amount=0):
        roots = []

        for g in range(2, self.n):
            if self.debug:
                print(f"Checking {Color.OKBLUE}{g}^k{Color.DEFAULT} modulo {Color.OKBLUE}{self.n}{Color.DEFAULT}...")

            array = []
            for k in range(1, self.n):
                array.append(pow(g, k, self.n))
            if len([*set(array)]) == self.n - 1:
                roots.append(g)
                if len(roots) >= max_amount:
                    return roots[-1]

        return roots[-1]

    def run(self):
        g = self.roots(1)

        private_key_a = random.randint(2 ** 1024, 2 ** 2048)
        private_key_b = random.randint(2 ** 1024, 2 ** 2048)

        X = pow(g, private_key_a, self.n)
        Y = pow(g, private_key_b, self.n)

        k_a = pow(Y, private_key_a, self.n)
        k_b = pow(X, private_key_b, self.n)

        if self.debug:
            print(f"N: {Color.OKBLUE}{self.n}{Color.DEFAULT}")
            print(f"G: {Color.OKBLUE}{g}{Color.DEFAULT}")
            print(f"X: {Color.OKBLUE}{X}{Color.DEFAULT}")
            print(f"Y: {Color.OKBLUE}{Y}{Color.DEFAULT}")
            print(f"K_A: {Color.OKBLUE}{k_a}{Color.DEFAULT}")
            print(f"K_B: {Color.OKBLUE}{k_b}{Color.DEFAULT}")

        print(f"Private key (A): {Color.OKBLUE}{private_key_a}{Color.DEFAULT}")
        print(f"Private key (B): {Color.OKBLUE}{private_key_b}{Color.DEFAULT}")
