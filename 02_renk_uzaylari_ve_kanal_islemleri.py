import cv2
import numpy as np
import matplotlib.pyplot as plt

# Denemek istediğiniz adımın başındaki yorum satırını (###) kaldırabilirsiniz.

# --- ADIM 1: OPENCV (BGR) VE MATPLOTLIB (RGB) RENK ÇELİŞKİSİ ---
"""
OpenCV bir görüntüyü varsayılan olarak BGR (Mavi, Yeşil, Kırmızı) okurken, 
Matplotlib RGB sırasıyla işlemeyi bekler. Bu durum, renklerin ters görünmesine 
(örneğin kırmızı nesnelerin maviye dönmesine) neden olur.
"""
### I = cv2.imread('peppers.png', 1)
### plt.imshow(I)
### plt.waitforbuttonpress()
### plt.close()


# --- ADIM 2: MANUEL KANAL AYIRMA VE SIFIR MATRİSİ İLE ÇAPRAZ BİRLEŞTİRME ---
"""
Bu adımda görüntünün renk kanallarını NumPy dilimleme (slicing) ile tek tek ayırıyoruz.
Ardından içi boş (sıfır) bir matris oluşturup kanalların yerini manuel olarak
değiştirerek yerleştiriyoruz. Böylece BGR -> RGB dönüşümünün mantığını kavrıyoruz.
"""
### I = cv2.imread('peppers.png', 1)
###
# Orijinal resimle aynı boyutlarda, içi sıfır (siyah) 3 kanallı bir uint8 matris oluşturalım
### I4 = np.zeros((I.shape[0], I.shape[1], 3), dtype=np.uint8)
###
# Kanalları indekslerine göre çekiyoruz (0: Mavi, 1: Yeşil, 2: Kırmızı)
### I_b = I[:, :, 0]
### I_g = I[:, :, 1]
### I_r = I[:, :, 2]
###
# Tek bir kanalı imshow ile bastığımızda, o kanalın yoğunluk haritasını gri olarak görürüz
### cv2.imshow('Sadece Kirmizi Kanal Yoogunlugu (Gri Gorunur)', I_r)
### cv2.waitKey(0)
### cv2.destroyAllWindows()
###
# Şimdi bu kanalları yeni boş matrise çapraz yerleştirerek renkleri düzeltiyoruz
### I4[:, :, 0] = I_r  # Orijinal Kırmızıyı Mavi kanala atadık
### I4[:, :, 1] = I_g  # Yeşili yerinde bıraktık
### I4[:, :, 2] = I_b  # Orijinal Maviyi Kırmızı kanala atadık
###
### cv2.imshow('Kanallari Manuel Yer Degistirilmis Matris (I4)', I4)
### cv2.waitKey(0)
### cv2.destroyAllWindows()


# --- ADIM 3: CV2.SPLIT() VE CV2.MERGE() HAZIR FONKSİYONLARI ---
"""
OpenCV'nin kendi içinde barındırdığı hazır split ve merge fonksiyonlarını kullanarak
kanalları ayırma ve sıralamasını değiştirerek yeniden birleştirme uygulamasıdır.
"""
### I = cv2.imread('peppers.png', 1)
###
# Fonksiyon yardımıyla 3 kanallı tek seferde değişkenlere bölüyoruz
### I5_b, I5_g, I5_r = cv2.split(I)
###
# Kanalları Matplotlib'in doğru okuyacağı RGB sırasında birleştiriyoruz
### I6 = cv2.merge([I5_r, I5_g, I5_b])
###
# Matplotlib artık renkleri tamamen doğru gösterecektir
### plt.imshow(I6)
### plt.waitforbuttonpress()
### plt.close()


# --- ADIM 4: NUMPY DİLİMLEME (SLICING) İLE HIZLI KANAL TERSLEME ---
"""
Hiç fonksiyon kullanmadan, NumPy'ın matris ters çevirme yeteneğini kullanarak
üçüncü boyuttaki (renk kanalları) veriyi tersten okutup BGR'ı RGB'ye tek satırda dönüştürürüz.
"""
### I = cv2.imread('peppers.png', 1)
###
# Sondaki ::-1 ifadesi renk kanallarının sırasını (0,1,2 -> 2,1,0) yapar
### I7 = I[:, :, ::-1]
###
### plt.imshow(I7)
### plt.waitforbuttonpress()
### plt.close()


# --- ADIM 5: RENK UZAYI DÖNÜŞÜMLERİ (GRİ TONLAMA VE HSV) ---
"""
Görüntüyü tamamen farklı matematiksel uzaylara taşımak için cv2.cvtColor kullanılır.
COLOR_BGR2GRAY görüntüyü tek kanallı griye düşürürken, COLOR_BGR2HSV ise rengi ton (H),
doygunluk (S) ve parlaklık (V) bileşenlerine ayırır.
"""
### I = cv2.imread('peppers.png', 1)
###
# Görüntüyü gri tonlamaya çeviriyoruz
### I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
### print("Gri Görsel Boyutu (Artık 3. boyut yani kanal bilgisi yoktur):", I_gray.shape)
###
# Görüntüyü HSV renk uzayına çeviriyoruz
### I_hsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
###
# Dönüştürülen gri görüntüyü diske kaydetme testi
### cv2.imwrite('peppers_gray.tif', I_gray)
###
### cv2.imshow('Gri Tonlamali Goruntu', I_gray)
### cv2.imshow('HSV Renk Uzayi Goruntusu', I_hsv)
### cv2.waitKey(0)
### cv2.destroyAllWindows()


# --- ADIM 6: MATPLOTLIB İLE GRİ TONLAMALI GÖRSEL BASMA AYARI ---
"""
Matplotlib, tek kanallı (gri) matrisleri varsayılan olarak bir renk haritasıyla (colormap) basar.
Gerçek siyah-beyaz tonları görebilmek için cmap='gray' parametresinin verilmesi zorunludur.
"""
### I_gray = cv2.cvtColor(cv2.imread('peppers.png', 1), cv2.COLOR_BGR2GRAY)
### plt.imshow(I_gray, cmap='gray', interpolation='Nearest')
### plt.waitforbuttonpress()
### plt.close()