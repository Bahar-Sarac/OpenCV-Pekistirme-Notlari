import cv2
import numpy as np

# Denemek istediğiniz adımın başındaki yorum satırını (###) kaldırabilirsiniz.

# --- ADIM 1: NUMPY VE OPENCV ARASINDAKİ TAŞMA (OVERFLOW) FARKI ---
"""
Görüntü işlemede piksel değerleri 0-255 arasındadır (uint8). 
Bir piksele değer eklerken 255 sınırı aşılırsa:
- NumPy matrisi modüler aritmetik yapar (başa sarar: 250 + 10 = 260 -> 260 % 256 = 4).
- OpenCV cv2.add() fonksiyonu ise değeri kırpar/sabitler (saturation: 250 + 10 = 255).
"""
### a = np.uint8([250])
### b = np.uint8([10])
###
### print("NumPy Dogrudan Toplama (Tasip Basa Sarar):", a + b)     # Çıktı: [4]
### print("OpenCV cv2.add ile Toplama (255'te Sabitler):", cv2.add(a, b)) # Çıktı: [[255]]


# --- ADIM 2: CV2.ADD VE CV2.SUBTRACT İLE PARLAKLIK AYARI ---
"""
Görüntünün tüm piksellerine sabit bir değer eklemek parlaklığı artırır,
sabit bir değer çıkarmak ise parlaklığı azaltır. Taşma piksellerini bozmamak için
OpenCV fonksiyonlarını kullanıyoruz.
"""
### I = cv2.imread('peppers.png', 1)
###
# Resimle aynı boyutta ve her pikseli 50 olan bir matris üretiyoruz
### brightness_matrix = np.ones(I.shape, dtype="uint8") * 50
###
# Parlaklığı artırma (Görsel beyazlaşır)
### I_bright = cv2.add(I, brightness_matrix)
###
# Parlaklığı azaltma (Görsel siyahlaşır)
### I_dark = cv2.subtract(I, brightness_matrix)
###
### cv2.imshow('Orijinal Peppers', I)
### cv2.imshow('Parlakligi Artirilmis', I_bright)
### cv2.imshow('Parlakligi Azaltilmis', I_dark)
### cv2.waitKey(0)
### cv2.destroyAllWindows()


# --- ADIM 3: MATEMATİKSEL FORMÜLLE KONTRAST VE PARLAKLIK (F(X) = A * X + B) ---
"""
Kontrast, görüntüdeki en karanlık ve en aydınlık bölgeler arasındaki farktır.
Görüntüyü bir katsayı (alfa) ile çarpmak kontrastı değiştirirken, 
bir sabit (beta) eklemek parlaklığı değiştirir.
Formül: Yeni_Piksel = alfa * Orijinal_Piksel + beta
"""
### I = cv2.imread('peppers.png', 1)
###
### alpha = 2.0  # Kontrast kontrolü (1.0 - 3.0 arası kontrastı artırır)
### beta = 30    # Parlaklık kontrolü (Pozitif değerler aydınlatır)
###
# np.zeros_like: Orijinal resimle tamamen aynı boyutta ve tipte boş bir matris açar
### I_contrast = np.zeros_like(I)
###
# cv2.convertScaleAbs fonksiyonu üstteki f(x) = alpha*x + beta formülünü
# tüm matrise optimize ve taşmaları engelleyecek şekilde otomatik uygular.
### I_contrast = cv2.convertScaleAbs(I, alpha=alpha, beta=beta)
###
### cv2.imshow('Orijinal Peppers', I)
### cv2.imshow('Yuksek Kontrast ve Parlaklik', I_contrast)
### cv2.waitKey(0)
### cv2.destroyAllWindows()