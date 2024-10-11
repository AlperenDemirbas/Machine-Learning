import numpy as np

data = [
    [6, 8, 8, 6, 'x'],
    [1, 5, '?', 5, 'y'],
    [1, 5, 3, 2, 'y'],
    [0, '?', 8, 6, 'x'],
    [7, '?', 7, '?', 'y'],
    [4, 3, 1, 0, 'x'],
    [5, 1, 2, 3, 'y'],
    [3, 3, 3, 3, '?'],
    [0, 0, 0, 0, 'x'],
    [9, 1, 2, 1, 'y'],
    [8, 8, 8, 8, '?'],
    [4, 5, '?', 7, 'y'],
    [2, 6, 5, 5, 'x'],
    [1, 1, 0, 1, 'y'],
    [6, 7, '?', 4, '?'],
    [3, '?', 2, 2, 'x'],
    [1, 0, 1, 0, 'y'],
    [7, 5, '?', 8, 'x'],
    [4, 2, 6, 0, 'y'],
    [0, 0, 0, 1, 'x'],
    [1, 3, 2, '?', 'y'],
    [3, 2, 2, 1, 'x'],
    [7, '?', 3, 5, 'y'],
    [5, 4, 1, 4, '?'],
    [3, 3, 2, 4, 'x'],
    [6, '?', 6, 1, 'y'],
    [1, 1, '?', 1, 'x'],
    [9, 8, 7, '?', 'y'],
    [2, 3, 4, 5, 'x'],
    [5, 1, 0, 6, 'y'],
    [4, 0, 1, 2, '?'],
    [8, 8, 8, 7, 'x'],
    [7, 5, '?', 4, 'y'],
    [1, '?', 3, '?', 'x'],
    [6, 1, 0, 1, 'y'],
    [1, 0, 1, 3, '?'],
    [0, 6, 7, 8, 'x'],
    [5, 1, 1, 2, 'y'],
    [9, '?', 3, 1, 'x'],
    [8, 7, 6, '?', 'y'],
    [0, 5, 5, 5, 'x'],
    [3, 4, '?', 4, 'y'],
    [1, 2, 3, '?', '?'],
    [7, 3, 1, 1, 'x'],
    [4, 0, '?', 0, 'y'],
    [9, '?', 1, 5, 'x'],
    [2, 6, 6, 0, 'y'],
    [6, 2, 1, 5, '?'],
    [5, 3, '?', 3, 'x'],
    [3, 4, 1, 1, 'y'],
    [1, 0, 2, 0, '?'],
    [9, 8, 7, 6, 'x'],
    [4, 1, '?', 5, 'y'],
    [0, 0, 0, 1, 'x'],
    [2, 1, 1, 1, 'y'],
    [8, 5, 2, 3, '?'],
    [3, 4, 1, 0, 'x'],
    [1, 1, 0, '?', 'y'],
    [2, 5, 3, 1, 'x'],
    [7, '?', 4, 2, 'y'],
    [5, 0, 0, 0, '?'],
    [8, 1, 1, 1, 'x'],
    [1, '?', 0, 3, 'y'],
    [0, 2, 2, '?', 'y'],
    [4, 5, 3, 0, 'x'],
    [6, 2, '?', 1, 'y'],
    [2, '?', 2, 2, 'x'],
    [9, 7, 6, 3, 'y'],
    [8, 0, 1, 1, 'x'],
    [5, 5, 5, 5, 'y'],
    [2, 3, '?', 0, 'x'],
    [0, 0, '?', 3, 'y'],
    [3, 1, 4, 4, 'z'],
    [5, 2, 2, 2, 'x'],
    [1, '?', 1, 0, 'y'],
    [6, 4, 0, 1, 'y'],
    [4, 0, '?', 4, 'x'],
    [3, 2, 1, 0, 'y'],
    [9, 8, 3, 3, '?'],
    [0, 1, 1, '?', 'x'],
    [2, 5, '?', 3, 'y'],
    [7, 0, 1, 5, 'x'],
    [1, 3, 2, '?', 'y'],
    [5, 5, 1, 4, 'x'],
    [6, 1, 3, 1, 'y'],
    [0, 2, 2, 2, 'x'],
    [4, 3, 1, 1, 'y']
]

# Eksik verileri sınıf ortalaması ile doldurma
def fill_missing_with_class_mean(data):
    # ? karakterini np.nan ile değiştiriyoruz
    # Data'yi numpy array'e çeviriyoruz ve '?' karakterini np.nan ile değiştiriyoruz
    df = np.array([[np.nan if val == '?' else val for val in row] for row in data], dtype=object)
    
    # Her sütun ve sınıf için işlemleri gerçekleştirme
    for col in range(4):  # İlk dört sütun üzerinde işlem yapıyoruz
        for label in ['x', 'y', 'z']:  # Sınıflar 'x', 'y', 'z' olarak belirlenmiş
            # Belirli bir sınıfa ait verileri maskeleme
            mask = df[:, -1] == label  # Sınıfa göre filtreleme
            class_data = df[mask, col].astype(float)  # Sınıfa ait verileri alıyoruz ve float'a dönüştürüyoruz
            class_mean = np.nanmean(class_data)  # Sınıfın ortalama değerini hesaplıyoruz
            # Eksik verileri (NaN) sınıf ortalaması ile dolduruyoruz
            df[mask & np.isnan(df[:, col].astype(float)), col] = class_mean

    # np.nan olanları tekrar ? ile değiştiriyoruz
    # Sonuçta ? olmayan tüm değerler ortalama ile doldurulmuş olacak
    df = [[str('?') if isinstance(val, float) and np.isnan(val) else val for val in row] for row in df]
    
    return df

# Eksik verileri doldur
filled_data = fill_missing_with_class_mean(data)

# Sonuçları yazdır
for row in filled_data:
    print(row)
