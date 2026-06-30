import cv2
import numpy as np

# Denemek istediğiniz adımın başındaki yorum satırını (###) kaldırabilirsiniz.

# --- ADIM 1: GÖRÜNTÜYÜ 3x3 PARÇALARA BÖLME VE DİNAMİK BOŞLUKLU IZGARA OLUŞTURMA ---
"""
Bu adımda, girdiğimiz görüntünün yükseklik ve genişlik değerlerini tam 3'e bölerek
dokuz adet eşit parça (sub-image) elde ediyoruz. Ardından, bu parçaların arasına
kullanıcının belirlediği piksel boyutunda (gap_size) siyah boşluklar yerleştirerek
yeni ve dinamik bir yapay tuval üzerinde birleştiriyoruz.
"""
### I = cv2.imread('peppers.png', 1)
### h, w, c = I.shape
###
# Görüntünün 3 eşit parçaya tam bölünebilmesi için parça boyutlarını hesaplıyoruz
### patch_h = h // 3
### patch_w = w // 3
###
# Parçaların arasına eklenecek boşluk piksel miktarı
### gap_size = 10
###
# 3 parça için 2 adet ara boşluk olacağından, yeni tuvalin (grid) boyutlarını belirliyoruz
### grid_h = 3 * patch_h + 2 * gap_size
### grid_w = 3 * patch_w + 2 * gap_size
###
# İçi tamamen sıfır (siyah) olan yeni büyük tuvalimizi oluşturuyoruz
### I_grid = np.zeros((grid_h, grid_w, c), dtype=np.uint8)
###
# Çift döngü ile 3x3'lük matrisin her bir hücresini tek tek dolaşıyoruz
### for i in range(3):
###     for j in range(3):
###         # Orijinal görüntüden ilgili parçayı dilimliyoruz (Slicing)
###         y_start = i * patch_h
###         y_end = (i + 1) * patch_h
###         x_start = j * patch_w
###         x_end = (j + 1) * patch_w
###         patch = I[y_start:y_end, x_start:x_end]
###
###         # Yeni büyük tuval (I_grid) üzerindeki hedef koordinatları hesaplıyoruz
###         # Her parça, hücre indeksi kadar boşluk (gap_size) payı ile ötelenir
###         target_y_start = i * (patch_h + gap_size)
###         target_y_end = target_y_start + patch_h
###         target_x_start = j * (patch_w + gap_size)
###         target_x_end = target_x_start + patch_w
###
###         # Parçayı hedef konumuna yerleştiriyoruz
###         I_grid[target_y_start:target_y_end, target_x_start:target_x_end] = patch
###
### cv2.imshow('3x3 Dinamik Bosluklu Izgara', I_grid)
### cv2.waitKey(0)
### cv2.destroyAllWindows()


# --- ADIM 2: GELİŞMİŞ MATRİS YAZDIRMA VE FORMATLAMA AYARLARI ---
"""
NumPy matrislerini ekrana bastığımızda varsayılan olarak orta kısımlar üç nokta (...) ile gizlenir.
Ayrıca float değerler çok uzun görünebilir. Bu adımda np.set_printoptions kullanarak
tüm matris matrisini gizlemeden, net ve okunabilir şekilde yazdırmayı yapılandırıyoruz.
"""
# precision: Ondalık basamak sayısı, suppress: Bilimsel gösterimi (e-05 vb.) kapatır
# threshold: Matrisin kaç elemana kadar tam basılacağını belirler (inf: asla gizleme)
### np.set_printoptions(precision=4, suppress=True, threshold=np.inf)
###
### test_matrix = np.random.random((5, 5))
### print("Formatlanmış ve Tamamı Açık NumPy Matrisi:\n", test_matrix)


# --- ADIM 3: MATRİS VERİ TİPLERİ VE DOĞRULUK ANALİZİ ---
"""
Görüntü işlemede veri tipleri (uint8, float32, float64) arasındaki farklar çok kritiktir.
Bu adımda float matrislerin bellekteki kapladığı alan ve hassasiyet farklarını inceliyoruz.
"""
### matrix_64 = np.random.random((10, 10))  # Varsayılan float64
### matrix_32 = np.float32(matrix_64)      # Bellekte yarı yarıya az yer kaplar
###
### print("Float64 Tipi Bellek Boyutu:", matrix_64.nbytes, "bytes")
### print("Float32 Tipi Bellek Boyutu:", matrix_32.nbytes, "bytes")