# Prepare > Python > Collections > collections.Counter()
#Using collection.Counter()

from collections import Counter

X = int(input())
ukuran_sepatu = list(map(int, input().split()))
N = int(input())

ukuran_counter = Counter(ukuran_sepatu)

penghasilan = 0

for pembeli in range(N):
    ukuran, harga = list(map(int, input().split()))
    if ukuran in ukuran_counter.keys():
        if ukuran_counter[ukuran] > 0:
            penghasilan = penghasilan + harga
            ukuran_counter[ukuran] = ukuran_counter[ukuran] - 1
print(penghasilan)
