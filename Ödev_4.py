import random

# Giriş verileri
array2D = [
    [6, 8, 8, 6, 'x'], [1, 5, '?', 5, 'y'], [1, 5, 3, 2, 'y'], [1, '?', 8, 6, 'x'], 
    [7, '?', 7, '?', 'y'], [4, 3, 1, 0, 'x'], [5, 1, 2, 3, 'y'], [3, 3, 3, 3, '?'],
    [1, 0, 0, 0, 'x'], [9, 1, 2, 1, 'y'], [8, 8, 8, 8, '?'], [4, 5, '?', 7, 'y'],
    [2, 6, 5, 5, 'x'], [1, 1, 0, 1, 'y'], [6, 7, '?', 4, '?'], [3, '?', 2, 2, 'x'],
    [1, 0, 1, 0, 'y'], [7, 5, '?', 8, 'x'], [4, 2, 6, 0, 'y'], [1, 0, 0, 1, 'x'],
    [1, 3, 2, '?', 'y'], [3, 2, 2, 1, 'x'], [7, '?', 3, 5, 'y'], [5, 4, 1, 4, '?'],
    [3, 3, 2, 4, 'x'], [6, '?', 6, 1, 'y'], [1, 1, '?', 1, 'x'], [9, 8, 7, '?', 'y'],
    [2, 3, 4, 5, 'x'], [5, 1, 0, 6, 'y'], [4, 0, 1, 2, '?'], [8, 8, 8, 7, 'x'],
    [7, 5, '?', 4, 'y'], [1, '?', 3, '?', 'x'], [6, 1, 0, 1, 'y'], [2, 0, 1, 3, '?'],
    [1, 6, 7, 8, 'x'], [5, 1, 1, 2, 'y'], [9, '?', 3, 1, 'x'], [8, 7, 6, '?', 'y'],
    [1, 5, 5, 5, 'x'], [3, 4, '?', 4, 'y'], [1, 2, 3, '?', '?'], [7, 3, 1, 1, 'x'],
    [4, 0, '?', 0, 'y'], [9, '?', 1, 5, 'x'], [2, 6, 6, 0, 'y'], [6, 2, 1, 5, '?'],
    [5, 3, '?', 3, 'x'], [3, 4, 1, 1, 'y'], [1, 0, 2, 0, '?'], [9, 8, 7, 6, 'x'],
    [4, 1, '?', 5, 'y'], [1, 0, 0, 1, 'x'], [2, 1, 1, 1, 'y'], [8, 5, 2, 3, '?'],
    [3, 4, 1, 0, 'x'], [1, 1, 0, '?', 'y'], [2, 5, 3, 1, 'x'], [7, '?', 4, 2, 'y'],
    [5, 0, 0, 0, '?'], [8, 1, 1, 1, 'x'], [1, '?', 0, 3, 'y'], [1, 2, 2, '?', 'y'],
    [4, 5, 3, 0, 'x'], [6, 2, '?', 1, 'y'], [2, '?', 2, 2, 'x'], [9, 7, 6, 3, 'y'],
    [8, 0, 1, 1, 'x'], [5, 5, 5, 5, 'y'], [2, 3, '?', 0, 'x'], [1, 0, '?', 3, 'y'],
    [3, 1, 4, 4, 'z'], [5, 2, 2, 2, 'x'], [1, '?', 1, 0, 'y'], [6, 4, 0, 1, 'y'],
    [4, 0, '?', 4, 'x'], [3, 2, 1, 0, 'y'], [9, 8, 3, 3, '?'], [1, 1, 1, '?', 'x'],
    [2, 5, '?', 3, 'y'], [7, 0, 1, 5, 'x'], [1, 3, 2, '?', 'y'], [5, 5, 1, 4, 'x'],
    [6, 1, 3, 1, 'y'], [1, 2, 2, 2, 'x'], [4, 3, 1, 1, 'y']
]

# Eksik veriyi doldurma
arrayCol = len(array2D[0])
arrayRow = len(array2D)

# Sınıfları bulma
arraypassenger = []
for row in array2D:
    if row[arrayCol - 1] not in arraypassenger and row[arrayCol - 1] != '?':
        arraypassenger.append(row[arrayCol - 1])

# Ortalama hesaplama
tempmean = [[0 for _ in range(arrayCol - 1)] for _ in range(len(arraypassenger))]

for e in range(len(arraypassenger)):
    for c in range(arrayCol - 1):
        sum_val, counter = 0, 0
        for r in range(arrayRow):
            if array2D[r][c] == '?' or array2D[r][arrayCol - 1] != arraypassenger[e]:
                continue
            sum_val += float(array2D[r][c])
            counter += 1
        if counter > 0:
            tempmean[e][c] = sum_val / counter

# Eksik değerleri doldurma
for a in range(arrayRow):
    for b in range(arrayCol - 1):
        if array2D[a][b] == '?':
            for d in range(len(arraypassenger)):
                if array2D[a][arrayCol - 1] == arraypassenger[d]:
                    array2D[a][b] = round(tempmean[d][b], 2)

# Min ve max değerlerin belirlenmesi
mins = [[float('inf') for _ in range(arrayCol - 1)] for _ in range(len(arraypassenger))]
maxs = [[-float('inf') for _ in range(arrayCol - 1)] for _ in range(len(arraypassenger))]

for a in range(len(arraypassenger)):
    for b in range(arrayCol - 1):
        for c in range(arrayRow):
            if array2D[c][arrayCol - 1] == arraypassenger[a]:
                value = float(array2D[c][b])
                mins[a][b] = min(mins[a][b], value)
                maxs[a][b] = max(maxs[a][b], value)

# Oversampling
clastooversampling = 'x'
countTosampling = 3

if countTosampling < 0 or not isinstance(countTosampling, int):
    print("Geçersiz bir örnekleme sayısı girdiniz.")
elif clastooversampling not in arraypassenger:
    print("Geçerli bir sınıf giriniz.")
else:
    for _ in range(countTosampling):
        temparray = [0] * arrayCol
        for a in range(len(arraypassenger)):
            if clastooversampling == arraypassenger[a]:
                temparray[arrayCol - 1] = arraypassenger[a]
                for b in range(arrayCol - 1):
                    random_value = random.uniform(mins[a][b], maxs[a][b])
                    temparray[b] = round(random_value, 2)
        array2D.append(temparray)

# Çıktı
for row in array2D:
    print(row)
