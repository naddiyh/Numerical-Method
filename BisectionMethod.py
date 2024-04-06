from tabulate import tabulate
from math import e

# Mendefinisikan fungsi formula/rumus
def f(x):
    return (9.8 * x / 25) * (1 - e ** (-(25 / x) * 15 )) - 45   # x=m dimana x adalah massa 



def bisection(xl, xu, approxError):
    print("\nHasil Perhitungan Bisection Method")

    # Inisialisasi variabel untuk proses iterasi dan menyimpan hasil.
    head = ["Iterasi", "xl", "f(xl)", "xu", "f(xu)", "xr", "f(xr)", "ea(%)"]
    hasil = []
    iterasi = 0
    xr = 0

    while True:  # Loop untuk iterasi metode bisection
        xrOld = xr
        xr = (xl + xu) / 2  # Menghitung nilai tengah (root approximation)
        iterasi = iterasi + 1
        
        # Menghitung error aproksimasi jika xr tidak nol.
        if xr != 0:
            ɛa = (abs(xr-xrOld) / xr) * 100
            
        # Menambahkan hasil iterasi ke dalam array 
        hasil.append([iterasi, xl, f(xl), xu, f(xu), xr, f(xr), ɛa if ɛa != 100 else " "])
        
        # Menentukan interval baru berdasarkan hasil f(xl) * f(xr)
        if f(xl) * f(xr) < 0:
            xu = xr
        elif f(xl) * f(xr) > 0:
            xl = xr
        else:
            ɛa = 0
        
        # Memeriksa apakah error lebih kecil dari error yang dapat diterima.
        if ɛa < approxError:
            break
        
    # Menampilkan hasil perhitungan dalam format tabel.
    print(tabulate(hasil, headers=head, tablefmt="grid"), end="\n")

print("Diketahui dibawah ini: ")
print("g = 9.8 m/s^2\nc = 25 kg\nv = 45 m/s\nt = 15s \nɛa = 0.1 %\n")
print("Masukkan Nilai  ")
xl = float(input("xl: ")) 
xu = float(input("xu: "))  
approxError = float(input("ɛa: ")) 
bisection(xl, xu, approxError)
