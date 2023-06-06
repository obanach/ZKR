from PIL import Image


class ImageSteganography:
    def __init__(self, filename):
        self.FILENAME = filename
        self.PATH = f"data/{filename}"
        self.image = Image.open(self.PATH)
        self.width, self.height = self.image.size

    @staticmethod
    # Konwersja liczby całkowitej na 8-bitowy ciąg binarny
    def _int_to_bin(n):
        return f"{n:08b}"

    @staticmethod
    # Konwersja ciągu binarnego na liczbę całkowitą
    def _bin_to_int(bin_str):
        return int(bin_str, 2)

    # Kodowanie wiadomości w obrazie poprzez modyfikację najmniej znaczących bitów
    def encode(self, message):
        secret_msg_bin = "".join(self._int_to_bin(ord(i)) for i in message)
        iterator = 0

        for h in range(self.height):
            for w in range(self.width):
                pixels = self.image.getpixel((w,h))
                new_pixels = []

                for p in pixels:
                    if iterator >= len(secret_msg_bin):
                        new_pixels.append(self._bin_to_int(self._int_to_bin(p)[:-1] + '1'))
                    else:
                        new_bit = secret_msg_bin[iterator]
                        new_pixels.append(self._bin_to_int(self._int_to_bin(p)[:-1] + new_bit))
                        iterator += 1

                self.image.putpixel((w,h), tuple(new_pixels))

        self.image.save(self.PATH)

    # Dekodowanie wiadomości z obrazu poprzez odczytanie najmniej znaczących bitów
    def decode(self):
        message = ""
        buffer = ""

        for h in range(self.height):
            for w in range(self.width):
                pixels = self.image.getpixel((w,h))

                for p in pixels:
                    buffer += self._int_to_bin(p)[-1]
                    if len(buffer) == 8:
                        if buffer == "11111111":
                            return message
                        message += chr(self._bin_to_int(buffer))
                        buffer = ""
        return message