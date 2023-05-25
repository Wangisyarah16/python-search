def binary_search_insert_position(data, target):
    left = 0
    right = len(data) - 1
    posisi_sisipan = len(data)

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return mid

        if data[mid] < target:
            left = mid + 1
        else:
            posisi_sisipan= mid
            right = mid - 1

    return posisi_sisipan

data = [2, 4, 6, 8, 10, 12, 14]
target = 7
posisi_sisipan = binary_search_insert_position(data, target)
print("elemen", target, "dapat disisipkan pada indeks ", posisi_sisipan, "untuk menjaga daftar tetap terurut")
