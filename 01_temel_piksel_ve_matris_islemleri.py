import cv2
import numpy as np

# NOT: Görseller kodla aynı dizindedir.
# Denemek istediğiniz adımın başındaki yorum satırını (###) kaldırabilirsiniz.

# --- ADIM 1: OPENCV VERSİYON KONTROLÜ ---
### print("OpenCV Sürümü:", cv2.__version__)


# --- ADIM 2: GÖRÜNTÜ OKUMA VE ÖZNİTELİK ANALİZİ ---
"""
Bu bölüm, bir görüntünün bellekte nasıl temsil edildiğini; boyutlarını (shape),
veri tipini (dtype) ve toplam piksel sayısını (size) analiz etmek için kullanılır.
"""
### I = cv2.imread('peppers.png', 1)  # 1: Renkli (BGR) modda okuma
###
### print("Görüntü Tipi:", type(I))
### print("Boyut Sayısı (Renkliyse 3, Gri ise 2):", I.ndim)
### print("Toplam Piksel Sayısı (H x W x C):", I.size)
### print("Görüntü Boyutları (Yükseklik, Genişlik, Kanal):", I.shape)
### print("Veri Tipi (Genelde uint8):", I.dtype)


# --- ADIM 3: BELİRLİ BİR PİKSEL DEĞERİNİ OKUMA VE DEĞİŞTİRME ---
"""
Görüntü üzerindeki (y, x) koordinatındaki piksellere erişip onları manipüle ederiz.
OpenCV görüntüleri varsayılan olarak BGR (Mavi, Yeşil, Kırmızı) sırasıyla saklar.
"""
### I = cv2.imread('peppers.png', 1)
### print('-' * 40)
### print("(10, 10) Koordinatındaki Orijinal Piksel (BGR):", I[10, 10])
###
### # Orijinal matrisi korumak için derin kopyasını alıyoruz
### I2 = I.copy()
###
### # (10, 10) konumundaki piksel rengini koyu gri olarak değiştiriyoruz
### I2[10, 10] = [8, 8, 8]
###
### print("Orijinal Görüntüdeki Piksel Durumu (Değişmedi):", I[10, 10])
### print("Kopyalanan Görüntüdeki Yeni Piksel Değeri:", I2[10, 10])
###
### # Ekranda pencere gösterimi ve güvenli kapatma döngüsü
### cv2.imshow('Orijinal Peppers', I)
### cv2.imshow('Pikseli Degistirilmis Peppers (I2)', I2)
### cv2.waitKey(0)
### cv2.destroyAllWindows()


# --- ADIM 4: NUMPY İLE RASTGELE YAPAY GÖRÜNTÜ OLUŞTURMA ---
"""
Bu bölümde, dışarıdan hazır resim yüklemek yerine tamamen matematiksel ve rastgele
0-1 arası float değerlerden oluşan bir matris üretip, bunu OpenCV'nin işleyebileceği
anlamlı bir 8-bit (uint8) görsel matrisine dönüştürüyoruz.
"""
# 300x500 boyutlarında ve 3 renk kanallı, 0-1 arası rastgele değerler içeren matris
### I3 = np.random.random((300, 500, 3))
### print("Rastgele Üretilen Matris Boyutu:", I3.shape)
###
# Değerleri [0, 255] aralığına ölçekleyip yuvarlıyoruz ve uint8 tipine çeviriyoruz
### I3 = np.uint8(np.round(I3 * 255))
### print("Dönüşüm Sonrası Yeni Veri Tipi:", I3.dtype)
###
### cv2.imshow('Rastgele Gurultu Goruntusu', I3)
### cv2.waitKey(0)
### cv2.destroyAllWindows()