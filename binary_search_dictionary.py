def binary_search(kamus, target):
    low = 0
    high = len(kamus) - 1

    while low <= high:
        mid = (low + high) // 2
        if kamus[mid][0] == target:
            return kamus[mid][1]
        elif kamus[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1

    return "Definisi kata tidak ditemukan"

kamus = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

target_kata = input("Masukkan kata yang ingin dicari definisinya : ")
definisi = binary_search(kamus, target_kata)
print(f"Definisi kata '{target_kata}': {definisi}")