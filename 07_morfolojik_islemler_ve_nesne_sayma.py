import cv2
import numpy as np

# Denemek istediğiniz adımın başındaki yorum satırını (###) kaldırabilirsiniz.

# --- ADIM 1: KERNEL (YAPISAL ELEMAN) OLUŞTURMA VE AŞINDIRMA (EROSION) ---
"""
Aşındırma işlemi, nesnelerin kenarlarındaki pikselleri eriterek nesneleri küçültür.
Beyaz gürültüleri (küçük beyaz noktaları) yok etmek veya birleşik nesneleri ayırmak için kullanılır.
"""
### I_gray = cv2.imread('coins.png', 0)
### ret, I_binary = cv2.threshold(I_gray, 127, 255, cv2.THRESH_BINARY_INV)
###
# 5x5 boyutunda kare bir kernel oluşturuyoruz
### kernel = np.ones((5, 5), np.uint8)
###
# Aşındırma işlemini uyguluyoruz (iterations: işlemin kaç kez tekrarlanacağı)
### I_erosion = cv2.erode(I_binary, kernel, iterations=1)
###
### cv2.imshow('Orijinal Ikili Gorsel', I_binary)
### cv2.imshow('Asindirilmis (Kucultulmus) Goruntu', I_erosion)
### cv2.waitKey(0)
### cv2.destroyAllWindows()


# --- ADIM 2: YAYMA (DILATION) İŞLEMİ ---
"""
Yayma işlemi aşındırmanın tam tersidir. Nesne alanını genişletir, nesne içindeki
siyah boşlukları veya delikleri kapatmak için kullanılır.
"""
### I_gray = cv2.imread('coins.png', 0)
### ret, I_binary = cv2.threshold(I_gray, 127, 255, cv2.THRESH_BINARY_INV)
### kernel = np.ones((5, 5), np.uint8)
###
# Yayma işlemini uyguluyoruz
### I_dilation = cv2.dilate(I_binary, kernel, iterations=1)
###
### cv2.imshow('Orijinal Ikili Gorsel', I_binary)
### cv2.imshow('Yayilmis (Genisletilmis) Goruntu', I_dilation)
### cv2.waitKey(0)
### cv2.destroyAllWindows()


# --- ADIM 3: AÇMA VE KAPAMA (MORPHOLOGYEX) İŞLEMLERİ ---
"""
Açma (Opening): Önce aşındırma, sonra yayma yapar. Nesne dışındaki küçük gürültüleri siler.
Kapama (Closing): Önce yayma, sonra aşındırma yapar. Nesne içindeki delikleri ve çatlakları kapatır.
"""
### I_gray = cv2.imread('coins.png', 0)
### ret, I_binary = cv2.threshold(I_gray, 127, 255, cv2.THRESH_BINARY_INV)
### kernel = np.ones((9, 9), np.uint8)  # Etkiyi net görmek için kerneli büyüttük
###
# Açma işlemi (MORPH_OPEN)
### I_opening = cv2.morphologyEx(I_binary, cv2.MORPH_OPEN, kernel)
###
# Kapama işlemi (MORPH_CLOSE)
### I_closing = cv2.morphologyEx(I_binary, cv2.MORPH_CLOSE, kernel)
###
### cv2.imshow('Orijinal Ikili Gorsel', I_binary)
### cv2.imshow('Acma (Gurultu Silinmis)', I_opening)
### cv2.imshow('Kapama (Bosluklar Kapatilmis)', I_closing)
### cv2.waitKey(0)
### cv2.destroyAllWindows()


# --- ADIM 4: CONNECTED COMPONENTS İLE BAĞLANTILI BİLEŞEN (NESNE) SAYMA ---
"""
İkili (binary) bir görüntüdeki birbirine temas eden beyaz piksel gruplarını
analiz ederek görselde toplam kaç adet bağımsız nesne olduğunu matematiksel olarak sayar.
"""
# İçindeki delikleri kapatılmış temiz sürümü yüklüyoruz veya kodla üretiyoruz
### I_filled = cv2.imread('coins_filled.jpg', 0)
### ret, I_filled_binary = cv2.threshold(I_filled, 127, 255, cv2.THRESH_BINARY)
###
# Bağlantılı bileşenleri buluyoruz
# num_labels: Toplam etiket sayısı (Arka plan dahil olduğu için toplam nesne sayısı = num_labels - 1)
# labels_im: Her bir piksele ait etiket numarasını (0, 1, 2...) içeren matris
### num_labels, labels_im = cv2.connectedComponents(I_filled_binary)
###
### total_objects = num_labels - 1
### print(f"Görselde Tespit Edilen Toplam Nesne Sayisi: {total_objects}")
###
### cv2.imshow('Sayilan Nesnelerin Maskesi', I_filled_binary)
### cv2.waitKey(0)
### cv2.destroyAllWindows()