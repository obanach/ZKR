# ImageSteganography

To narzędzie napisane w Pythonie, służące do ukrywania wiadomości w obrazach. Wykorzystuje technikę steganografii obrazu, polegającą na modyfikacji najmniej znaczących bitów (LSB - Least Significant Bits) każdego piksela obrazu.


## Działanie

Klasa ImageSteganography działa na zasadzie modyfikacji LSB każdego piksela w obrazie, aby ukryć w nim wiadomość. Najmniej znaczący bit jest częścią liczby binarnej, która ma najmniejszy wpływ na wartość liczby. W kontekście obrazów, modyfikacja LSB piksela nie wpływa znacząco na kolor piksela, co czyni modyfikację niezauważalną dla ludzkiego oka.

## Instalacja

### Wymagania

- Python 3.8 lub nowszy
- Biblioteka Pythona `PIL` (Pillow)


Możesz je zainstalować za pomocą pip:

```bash
pip install pillow
```

## Sposób użycia

1. Utwórz instancję klasy `ImageSteganography`, przekazując ścieżkę do obrazu tajnego jako argument:
```python
st = ImageSteganography('IMAGE.PNG')
```
2. Zakoduj wiadomość w obrazie:
```python
st.encode('Tajna wiadomość')
```
3. Dekoduj wiadomość z obrazu:
```python
print(st.decode())
```

## Metody

- `__init__`:  Inicjalizuje instancję klasy ImageSteganography, wczytuje obraz i ustala jego wymiary.
- `_int_to_bin()` i `_bin_to_int()`: Metody pomocnicze służące do konwersji między liczbami całkowitymi a ich reprezentacjami binarnymi.
- `encode()`: Koduje wiadomość w obrazie poprzez modyfikację LSB każdego piksela.
- `decode()`: Dekoduje wiadomość z obrazu poprzez odczytanie LSB każdego piksela.

