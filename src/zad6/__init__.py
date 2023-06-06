# Importowanie modułu PIL (Python Imaging Library), który umożliwia otwieranie, manipulowanie i zapisywanie wielu różnych formatów obrazów.
from PIL import Image

# Definiowanie klasy ImageSteganography do wykonywania operacji steganografii na obrazach
class ImageSteganography:
    # Inicjalizacja klasy z plikiem obrazu, który ma być używany
    def __init__(self, filename):
        self.FILENAME = filename  # Przechowywanie nazwy pliku
        self.PATH = f"data/{filename}"  # Ustalanie ścieżki do pliku
        self.image = Image.open(self.PATH)  # Otwarcie obrazu
        self.width, self.height = self.image.size  # Przechowywanie szerokości i wysokości obrazu

    @staticmethod
    # Metoda zamienia liczbę całkowitą na 8-bitowy ciąg binarny
    def _int_to_bin(n):
        return f"{n:08b}"

    @staticmethod
    # Metoda zamienia ciąg binarny na liczbę całkowitą
    def _bin_to_int(bin_str):
        return int(bin_str, 2)

    # Metoda koduje wiadomość w obrazie poprzez modyfikację najmniej znaczących bitów
    def encode(self, message):
        # Zamiana wiadomości na binarną reprezentację
        secret_msg_bin = "".join(self._int_to_bin(ord(i)) for i in message)
        iterator = 0

        # Iteracja po każdym pikselu obrazu
        for h in range(self.height):
            for w in range(self.width):
                # Pobranie wartości pikseli
                pixels = self.image.getpixel((w,h))
                new_pixels = []

                # Iteracja po wartościach pikseli i modyfikacja najmniej znaczących bitów
                for p in pixels:
                    if iterator >= len(secret_msg_bin):
                        new_pixels.append(self._bin_to_int(self._int_to_bin(p)[:-1] + '1'))
                    else:
                        new_bit = secret_msg_bin[iterator]
                        new_pixels.append(self._bin_to_int(self._int_to_bin(p)[:-1] + new_bit))
                        iterator += 1

                # Ustawienie nowych wartości pikseli
                self.image.putpixel((w,h), tuple(new_pixels))

        # Zapisanie zmodyfikowanego obrazu
        self.image.save(self.PATH)

    # Metoda dekoduje wiadomość z obrazu poprzez odczytanie najmniej znaczących bitów
    def decode(self):
        message = ""
        buffer = ""

        # Iteracja po każdym pikselu obrazu
        for h in range(self.height):
            for w in range(self.width):
                # Pobranie wartości pikseli
                pixels = self.image.getpixel((w,h))

                # Iteracja po wartościach pikseli i odczytanie najmniej znaczących bitów
                for p in pixels:
                    buffer += self._int_to_bin(p)[-1]
                    if len(buffer) == 8:
                        # Jeśli odczytano 8 bitów i są to same jedynki, to wiadomość została zakończona
                        if buffer == "11111111":
                            return message
                        # Dodanie znaku do wiadomości i wyczyszczenie bufora
                        message += chr(self._bin_to_int(buffer))
                        buffer = ""
        return message