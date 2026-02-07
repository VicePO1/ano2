import pytesseract
import cv2

def ler():
    # faz o opencv ler a imagem
    imagem = cv2.imread('inspiracao.jpg')

    # faz o Tesseract abrir o executável no computador
    caminho = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = caminho

    # pedir para o Tesseract converter a imagem para texto
    texto = pytesseract.image_to_string(imagem)
    print(texto)

ler()