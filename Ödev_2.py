# Girdiler
input_data = [
    ['6', '?', '8', '6', 'x'],
    ['1', '5', '?', '5', 'y'],
    ['6', '4', '8', '6', 'x'],
    ['1', '5', '3', '2', 'y'],
    ['0', '?', '8', '6', 'x'],
    ['7', '5', '7', '?', 'y']
]

arrayCol = len(input_data[0])
arrayRow = len(input_data)
arraypassenger = []

# Kaç farklı sınıf olduğunu öğrenme
for l in range(arrayRow):
    if input_data[l][arrayCol - 1] not in arraypassenger:
        arraypassenger.append(input_data[l][arrayCol - 1])

# Her sınıf için ortalama hesaplamak üzere yeni bir array oluşturma
tempmean = [[None] * (arrayCol - 1) for _ in range(len(arraypassenger))]
sum_values = 0
counter = 0

# Her sınıf ve sütun için ortalama bulunması
for e in range(len(arraypassenger)):
    for c in range(arrayCol - 1):
        for r in range(arrayRow):
            if input_data[r][c] == "?":
                continue
            if input_data[r][arrayCol - 1] == arraypassenger[e]:
                sum_values += float(input_data[r][c])
                counter += 1
        if counter > 0:
            tempmean[e][c] = sum_values / counter
        sum_values = 0
        counter = 0

# Eksik değerleri sınıf ortalamasıyla doldurma
for a in range(arrayRow):
    for b in range(arrayCol - 1):
        if input_data[a][b] == "?":
            for d in range(len(arraypassenger)):
                if input_data[a][arrayCol - 1] == arraypassenger[d]:
                    input_data[a][b] = tempmean[d][b]

# Sonuçları yazdırma
for row in input_data:
    print(','.join(map(str, row)))

