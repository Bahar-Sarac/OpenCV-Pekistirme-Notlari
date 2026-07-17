import cv2
import numpy as np

# Denemek istediğiniz adımın başındaki yorum satırını (###) kaldırabilirsiniz.

# --- ADIM 1: SABİT EŞİKLEME (BINARY THRESHOLDING) ---
"""
Gri tonlamalı bir görselde, belirlenen bir sınır değerinin (thresh) üstündeki
pikselleri beyaz (255), altındakileri ise siyah (0) yapma işlemidir.
"""
### I_gray = cv2.imread('cameraman.tif', 0)  # 0: Doğrudan gri tonlamada okur
###
# 127 sınır değerimiz, 255 ise sınır aşılınca piksele atanacak maksimum değerdir
### ret, I_thresh = cv2.threshold(I_gray, 127, 255, cv2.THRESH_BINARY)
###
### cv2.imshow('Orijinal Cameraman', I_gray)
### cv2.imshow('127 Esikli Binary Sonuc', I_thresh)
### cv2.waitKey(0)
### cv2.destroyAllWindows()


# --- ADIM 2: TERS EŞİKLEME (BINARY THRESHOLD INV) ---
"""
THRESH_BINARY_INV yöntemi mantığı tamamen tersine çevirir. 
Sınır değerin altında kalan pikseller beyaz (255), üstündekiler siyah (0) olur.
Özellikle koyu renkli nesneleri öne çıkarmak için kullanılır.
"""
### I_gray = cv2.imread('cameraman.tif', 0)
###
### ret, I_thresh_inv = cv2.threshold(I_gray, 127, 255, cv2.THRESH_BINARY_INV)
###
### cv2.imshow('Orijinal Cameraman', I_gray)
### cv2.imshow('Ters Esiklenmis Sonuc', I_thresh_inv)
### cv2.waitKey(0)
### cv2.destroyAllWindows()


# --- ADIM 3: OTSU ALGORİTMASI İLE OTOMATİK EŞİKLEME ---
"""
Her görsel için elle "127" gibi sabit bir eşik değeri girmek doğru sonuç vermez.
Otsu algoritması, görselin piksel histogramını analiz ederek en ideal eşik değerini 
matematiksel olarak kendi hesaplar.
"""
### I_gray = cv2.imread('cameraman.tif', 0)
###
# Sınır değer kısmına 0 yazarız ve THRESH_OTSU bayrağını ekleriz.
# Algoritmanın bulduğu en ideal eşik değeri 'ret' değişkenine döner.
### optimal_thresh, I_otsu = cv2.threshold(I_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
### print(f"Otsu Algoritmasinin Buldugu En Ideal Esik Degeri: {optimal_thresh}")
###
### cv2.imshow('Orijinal Cameraman', I_gray)
### cv2.imshow('Otsu Otomatik Esikleme', I_otsu)
### cv2.waitKey(0)
### cv2.destroyAllWindows()