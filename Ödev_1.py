# Girdiler
input_data = [
    ['s', '8', 'ı', '6', 'x'],
    ['s', '5', 't', '5', 'y'],
    ['k', '2', 'ı', '1', 'x'],
    ['b', '5', 'p', '1', 'y'],
    ['f', '5', 't', '4', 'z']
]

arrayCol = len(input_data[0])
arrayRow = len(input_data)
arraypassenger = []

# Sütunlardaki sayısal olmayan değerleri öğrenme
for j in range(arrayCol - 1):
    if not input_data[0][j].isdigit():
        for k in range(arrayRow):
            if input_data[k][j] not in arraypassenger:
                arraypassenger.append(input_data[k][j])
        # Sayısal olmayan değerleri sayısal değerlere çevirme
        for i in range(arrayRow):
            input_data[i][j] = arraypassenger.index(input_data[i][j]) + 1
        arraypassenger = []

# Kaç farklı sınıf olduğunu öğrenme
for l in range(arrayRow):
    if input_data[l][arrayCol - 1] not in arraypassenger:
        arraypassenger.append(input_data[l][arrayCol - 1])

# Yeni bir array oluşturma
newarray = [[0] * (arrayCol + len(arraypassenger) - 1) for _ in range(arrayRow)]

# Sınıf hariç tüm özellikleri yeni array'e aktarma
for a in range(arrayRow):
    for b in range(arrayCol - 1):
        newarray[a][b] = input_data[a][b]

# Sınıfları 0 ve 1 olarak yeni array'e aktarma
for c in range(len(arraypassenger)):
    for d in range(arrayRow):
        if input_data[d][arrayCol - 1] == arraypassenger[c]:
            newarray[d][arrayCol - 1 + c] = 1
        else:
            newarray[d][arrayCol - 1 + c] = 0

# Sonucu yazdırma
for row in newarray:
    print(','.join(map(str, row)))

