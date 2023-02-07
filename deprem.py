import pytesseract
from PIL import Image
import os

# Klasör yolu
folder_path = "./"

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # Bu kısma pytesseract kurduğunuz yolu yapıştırın

# Tüm resim dosyalarını ara
for filename in os.listdir(folder_path):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        # Görsel dosya yolu
        img = Image.open(os.path.join(folder_path, filename))

        # OCR çıktısı
        text = pytesseract.image_to_string(img, lang='tur', config='--psm 6')

        # Büyük harflerle yaz
        text = text.upper()

        # Txt dosyası yolu
        txt_file = os.path.splitext(filename)[0] + ".txt"

        # Txt dosyasına yaz
        with open(os.path.join(folder_path, txt_file), "w", encoding="utf-8") as file:
            file.write(text)
