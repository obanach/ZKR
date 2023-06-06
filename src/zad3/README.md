# Kryptografia Wizualna 

Projekt ten implementuje koncepcję wizualnej kryptografii. Jest to technika zabezpieczania informacji, gdzie obraz (tajemnica) jest dzielony na dwie części zwane udziałami. Te dwa udziały, gdy są nałożone na siebie, odsłaniają oryginalny obraz, a każdy z nich osobno nie daje żadnej informacji o obrazie.

## Instalacja

Aby skorzystać z tego projektu, musisz mieć zainstalowane następujące biblioteki:

1. PIL (Pillow)
2. random

Możesz je zainstalować za pomocą pip:

```bash
pip install pillow
```

## Sposób użycia

1. Utwórz instancję klasy `VisualCryptography`, przekazując ścieżkę do obrazu tajnego jako argument:
```python
vc = VisualCryptography("secret_image.png")
```
2. Uruchom proces:
```python
vc.run()
```
W wyniku tego obraz tajny zostanie podzielony na dwa udziały, które zostaną zapisane jako `part1.png` i `part2.png`. Odszyfrowany obraz zostanie zapisany jako `secret-decrypted.png`, a obraz podsumowujący jako `final.png`.

## Metody

- `create()`: tworzy udziały z obrazu tajnego.
- `decryptImage()`: odszyfrowuje obraz, dodając piksele z obu udziałów.
- `summary()`: tworzy obraz podsumowujący, który pokazuje obraz tajny, oba udziały i odszyfrowany obraz.
- `save()`: zapisuje oba udziały, odszyfrowany obraz i obraz podsumowujący.
- `run()`: uruchamia cały proces.

