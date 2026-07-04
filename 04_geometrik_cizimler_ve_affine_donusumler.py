import cv2
import numpy as np

# Denemek istediğiniz adımın başındaki yorum satırını (###) kaldırabilirsiniz.

# --- ADIM 1: CV2.POLYLINES İLE ÇOKGEN ÇİZİMİ VE MATEMATİKSEL CENTROID HESABI ---
"""
Bu adımda 3 kanallı boş bir siyah matris üzerine cv2.polylines kullanarak bir üçgen çiziyoruz.
Ardından, bu üçgenin köşe koordinatlarını kullanarak geometrik ağırlık merkezini (centroid)
matematiksel formülle hesaplıyoruz.
"""
### img = np.zeros((400, 400, 3), dtype=np.uint8)
###
# Üçgenin köşe noktalarını (x, y) olarak tanımlıyoruz
### points = np.array([[200, 100], [100, 300], [300, 300]], np.int32)
###
# polylines fonksiyonu noktaları ardışık olarak birleştirir. isClosed=True son noktayı ilke bağlar.
### cv2.polylines(img, [points], isClosed=True, color=(255, 255, 255), thickness=2)
###
# Matematiksel olarak Centroid (Ağırlık Merkezi) Hesaplama: (x1 + x2 + x3) / 3
### centroid_x = (points[0][0] + points[1][0] + points[2][0]) / 3
### centroid_y = (points[0][1] + points[1][1] + points[2][1]) / 3
### print(f"Hesaplanan Üçgen Merkez Koordinatlari: X={centroid_x}, Y={centroid_y}")
###
# Çizilen orijinal üçgeni gösterelim
### cv2.imshow('Orijinal Ucgen', img)
### cv2.waitKey(0)
### cv2.destroyAllWindows()


# --- ADIM 2: GETROTATIONMATRIX2D VE WARPAFFINE İLE DÖNDÜRME (ROTATION) ---
"""
Bir görüntüyü belirli bir merkez noktası etrafında döndürmek için Affine matrisi üretilir.
Bu adımda üstte çizdiğimiz üçgeni, kendi ağırlık merkezi etrafında 90 derece döndürüyoruz.
"""
### img = np.zeros((400, 400, 3), dtype=np.uint8)
### points = np.array([[200, 100], [100, 300], [300, 300]], np.int32)
### cv2.polylines(img, [points], isClosed=True, color=(255, 255, 255), thickness=2)
###
# Dönme merkezini tam orta nokta veya bir önceki adımda hesaplanan centroid seçebiliriz
### rotation_center = (200, 200)
### angle = 90       # Pozitif değer saat yönünün tersine döndürür
### scale = 1.0      # Ölçeklendirme faktörü (1.0: Boyut değişmez)
###
# 2x3 boyutunda döndürme matrisini (M) alıyoruz
### M = cv2.getRotationMatrix2D(rotation_center, angle, scale)
### print("Döndürme Matrisi (M):\n", M)
###
# Üretilen dönüşüm matrisini warpAffine ile görüntüye uyguluyoruz
### rotated_img = cv2.warpAffine(img, M, (400, 400))
###
### cv2.imshow('Orijinal Ucgen', img)
### cv2.imshow('Merkez Etrafinda 90 Derece Dondurulmus Ucgen', rotated_img)
### cv2.waitKey(0)
### cv2.destroyAllWindows()


# --- ADIM 3: TEMEL VE GELİŞMİŞ BOYUTLANDIRMA (RESIZE & INTERPOLATION) ---
"""
Görüntü boyutlarını değiştirmek için cv2.resize kullanılır. Piksel bozulmalarını önlemek
için inter_cubic veya inter_area gibi interpolasyon yöntemleri seçilir.
"""
### I6 = cv2.imread('peppers.png', 1)
###
# Sabit piksel boyutuna (200x200) küçültme/büyütme
### I7_fixed = cv2.resize(I6, (200, 200))
###
# INTER_CUBIC interpolasyonu kullanarak daha keskin bir yeniden boyutlandırma yapma
### I7_cubic = cv2.resize(I6, (100, 100), interpolation=cv2.INTER_CUBIC)
###
# fx ve fy parametreleri ile oran bazlı (Örn: Genişlik 2 katına, Yükseklik yarıya) boyutlandırma
### I8_scaled = cv2.resize(I6, None, fx=2, fy=0.5, interpolation=cv2.INTER_CUBIC)
###
### cv2.imshow('Orijinal Peppers', I6)
### cv2.imshow('200x200 Sabit Boyut', I7_fixed)
### cv2.imshow('100x100 Cubic Interpolation', I7_cubic)
### cv2.imshow('fx=2 fy=0.5 Oranli Boyutlandirma', I8_scaled)
### cv2.waitKey(0)
### cv2.destroyAllWindows()


# --- ADIM 4: NUMPY DİLİMLEME İLE MANUEL GÖRÜNTÜ KIRPMA (CROP) ---
"""
Herhangi bir OpenCV fonksiyonuna ihtiyaç duymadan, matris satır ve sütunlarını
slicing yöntemiyle sınırlayarak görüntü üzerinde ROI (Region of Interest) yani kırpma yaparız.
"""
### I6 = cv2.imread('peppers.png', 1)
###
# y_start:y_end , x_start:x_end aralığını dilimliyoruz
### I9_cropped = I6[250:320, 400:535]
###
### cv2.imshow('Orijinal Peppers', I6)
### cv2.imshow('Kirpilmis Bolge (ROI)', I9_cropped)
### cv2.waitKey(0)
### cv2.destroyAllWindows()


# --- ADIM 5: MATRİS İLE MANUEL ÖTELEME (TRANSLATION) ---
"""
Görüntüyü X ve Y ekseninde kaydırmak için 2x3'lük bir Affine matrisini kendimiz tanımlarız.
Matris yapısı: [[1, 0, dx], [0, 1, dy]] şeklindedir.
"""
### I = cv2.imread('peppers.png', 1)
### height, width = I.shape[0:2]
###
# x yönünde 50 piksel sağa, y yönünde 100 piksel aşağı öteleme matrisi (M2)
### M2 = np.float32([[1, 0, 50], [0, 1, 100]])
###
# Öteleme sonrası taşan piksellerin kırpılmaması için hedef tuval boyutunu (width+50, height+100) yapabiliriz
### I_translated = cv2.warpAffine(I, M2, (width + 50, height + 100))
###
### cv2.imshow('Orijinal', I)
### cv2.imshow('Otelendikten Sonra Alani Genisletilmis Gorntu', I_translated)
### cv2.waitKey(0)
### cv2.destroyAllWindows()


# --- ADIM 6: ÜÇ NOKTA EŞLEŞMESİ İLE MANUEL AYNALAMA (FLIP VIA AFFINE) ---
"""
Görüntünün üç köşe noktasının (Sol Üst, Sağ Üst, Sol Alt) hedefte nereye denk geleceğini
belirterek cv2.getAffineTransform yardımıyla manuel bir ters çevirme/aynalama matrisi üretiriz.
"""
### I6 = cv2.imread('peppers.png', 1)
### height, width = I6.shape[:2]
###
# Kaynak görüntüdeki 3 köşe noktası
### pts1 = np.float32([[0, 0], [width, 0], [0, height]])
# Bu noktaların aynalanmış hedef matristeki yeni konumları (Genişlik tersine dönüyor)
### pts2 = np.float32([[width, 0], [0, 0], [width, height]])
###
# Noktalardan dönüşüm matrisini çıkarıyoruz
### M_flip = cv2.getAffineTransform(pts1, pts2)
### I14_flipped = cv2.warpAffine(I6, M_flip, (width, height))
###
### cv2.imshow('Orijinal Peppers', I6)
### cv2.imshow('Affine ile Manuel Aynalanmis Goruntu', I14_flipped)
### cv2.waitKey(0)
### cv2.destroyAllWindows()