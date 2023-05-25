def sequential_search_phone_number(nama, nomor_telepon, target_nama):
    for i in range(len(nama)):
        if nama[i] == target_nama:
            return nomor_telepon[i]
    return "Nomor telepon tidak ditemukan."

nama = ["John Doe", "Jane Smith", "Michael Johnson", "Emily Davis"]
nomor_telepon = ["081234567890", "089876543210", "087811223344", "082122232425"]
target_nama = "Jane Smith"

nomor_telepon = sequential_search_phone_number(nama, nomor_telepon, target_nama)
print("Nomor telepon Jane Smith:", nomor_telepon)
