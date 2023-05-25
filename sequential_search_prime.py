def sequential_search_primes(angka):
    primes = []
    for angka in angka:
        if angka > 1:
            bilangan_prima = True
            for i in range(2, angka):
                if angka % i == 0:
                    bilangan_prima = False
                    break
            if bilangan_prima:
                primes.append(angka)
    return primes

angka = [7, 10, 13, 6, 17, 22, 19]
bilangan_prima= sequential_search_primes(angka)
print("Bilangan prima dalam daftar:", bilangan_prima)
