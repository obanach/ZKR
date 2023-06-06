from PIL import Image
import random

# Definiujemy klasę VisualCryptography, której celem jest realizacja kryptografii wizualnej - techniki umożliwiającej
# dzielenie obrazu na części (shares), które są nieczytelne samodzielnie, ale razem odtwarzają pierwotny obraz.
class VisualCryptography:
    def __init__(self, secret_path):
        # Tworzymy obrazy na podstawie wejściowego obrazu oraz tworzymy miejsce na przyszłe wynikowe obrazy
        self.summaryImg = None
        self.secretDecryptedImg = None
        # Definiujemy kolory biały i czarny
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        # Wczytujemy obraz do zaszyfrowania
        self.secretImg = Image.open(f"data/{secret_path}")
        # Pobieramy rozmiar obrazu
        self.width, self.height = self.secretImg.size
        # Tworzymy obrazy na które podzielimy nasz tajny obraz
        self.share1Img = Image.new( mode = "RGBA", size = (self.width, self.height) )
        self.share2Img = Image.new( mode = "RGBA", size = (self.width, self.height) )

    # Metoda statyczna do odczytu wartości pixeli - jeśli oba pixele są białe to zwraca biały, w przeciwnym razie zwraca czarny
    @staticmethod
    def readPixel(px1, px2):
        return tuple(255 if p1 and p2 else 0 for p1, p2 in zip(px1, px2))

    # Metoda generująca dwa obrazy na podstawie oryginalnego obrazu
    def generate(self):
        for y in range(self.height):
            for x in range(self.width):
                # Jeśli piksel jest biały, losujemy czy oba piksele będą białe lub oba będą czarne
                if self.secretImg.getpixel((x,y))[:3] == self.WHITE:
                    if random.randint(0,1) == 0:
                        self.share1Img.putpixel((x,y), self.WHITE )
                        self.share2Img.putpixel((x,y), self.WHITE )
                    else:
                        self.share1Img.putpixel((x,y), self.BLACK )
                        self.share2Img.putpixel((x,y), self.BLACK )
                # Jeśli piksel jest czarny, losujemy który z pikseli będzie biały a który czarny
                else:
                    if random.randint(0,1) == 0:
                        self.share1Img.putpixel((x,y), self.WHITE )
                        self.share2Img.putpixel((x,y), self.BLACK )
                    else:
                        self.share1Img.putpixel((x,y), self.BLACK )
                        self.share2Img.putpixel((x,y), self.WHITE )

    # Metoda deszyfrująca obraz na podstawie dwóch wygenerowanych obrazów
    def decryptImage(self):
        # Przebiegamy przez wszystkie piksele i odczytujemy wartość pikseli na podstawie metody readPixel
        pixel_data = [[self.readPixel(self.share1Img.getpixel((x, y)), self.share2Img.getpixel((x, y))) for x in range(self.width)] for y in range(self.height)]
        # Spłaszczamy listę pikseli do jednej listy
        flat_pixel_data = [pixel for row in pixel_data for pixel in row]
        # Tworzymy nowy obraz i umieszczamy w nim nasze odczytane piksele
        self.secretDecryptedImg = Image.new("RGBA", (self.width, self.height))
        self.secretDecryptedImg.putdata(flat_pixel_data)

    # Metoda tworząca obraz podsumowujący cały proces - zawiera oryginalny obraz, dwa wygenerowane obrazy oraz odszyfrowany obraz
    def summary(self):
        self.summaryImg = Image.new( mode = "RGBA", size = (self.width*2, self.height*2), color = (255,255,255,255) )
        for y in range(self.height):
            for x in range(self.width):
                self.summaryImg.putpixel((x, y), self.secretImg.getpixel((x,y)) )
                self.summaryImg.putpixel((x, y+self.height), self.share1Img.getpixel((x,y)) )
                self.summaryImg.putpixel((x+self.width, y+self.height), self.share2Img.getpixel((x,y)) )
                self.summaryImg.putpixel((x+self.width, y), self.secretDecryptedImg.getpixel((x,y)) )

    # Metoda zapisująca wszystkie wygenerowane obrazy do plików
    def save(self):
        self.share1Img.save("data/part1.png")
        self.share2Img.save("data/part2.png")
        self.secretDecryptedImg.save("data/secret-decrypted.png")
        self.summaryImg.save("data/final.png")

    # Metoda uruchamiająca cały proces
    def run(self):
        self.generate()
        self.decryptImage()
        self.summary()
        self.save()
