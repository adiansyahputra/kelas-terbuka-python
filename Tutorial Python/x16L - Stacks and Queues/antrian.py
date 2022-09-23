from collections import deque
antrian = deque([1, 2, 3, 4, 5, 6])

print("data sekarang :", antrian)

# menambahkan data
antrian.append(7)
print("data ditambahkan :", 7)
print("data sekarang :", antrian)

antrian.append(8)
print("data ditambahkan :", 8)
print("data sekarang :", antrian)

# mengurangi antrian
out = antrian.popleft()
print("data keluar :", out)
print("data sekarang :", antrian)

out = antrian.popleft()
print("data keluar :", out)
print("data sekarang :", antrian)

out = antrian.popleft()
print("data keluar :", out)
print("data sekarang :", antrian)
