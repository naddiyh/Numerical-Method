import math
from prettytable import PrettyTable

# Mendefinisikan fungsi yang akan dicari akarnya.
def f(x):
    return 5 - 5*x - math.exp(0.5*x)  # f(x) = 5 - 5x - e^(0.5x)

def Bisection(xl=0, xu=2):
    es = 2  # Toleransi error
    iterasiMax = 100  # Maksimum iterasi 

    print("\nBisection Method")
    print("xl = 0\nxu = 2 \n")
    loop = True
    iterasi = 0
    xr = 0

    # Membuat tabel
    table = PrettyTable()
    table.field_names = ["i", "xl", "f(xl)", "xu", "f(xu)", "xr", "f(xr)", "ea(%)"]

    while(loop):
        fl = f(xl)  
        fu = f(xu)  

        xrOld = xr  # Menyimpan nilai xr sebelumnya untuk menghitung error
        xr = (xl + xu) / 2  # Menghitung xr, titik tengah interval
        fr = f(xr)  # Nilai fungsi di xr

        # Menghitung error aproksimasi, kecuali pada iterasi pertama
        if not xr == 0:
            ea = abs((xr-xrOld)/xr)*100

        # Menambahkan hasil iterasi ke dalam tabel
        if iterasi == 0:
            table.add_row([iterasi, "%.4f" % xl, "%.4f" % fl, "%.4f" % xu, "%.4f" % fu, "%.4f" % xr, "%.4f" % fr, "-"])
        else:
            table.add_row([iterasi, "%.4f" % xl, "%.4f" % fl, "%.4f" % xu, "%.4f" % fu, "%.4f" % xr, "%.4f" % fr, "%.3f" % ea])

        # Memeriksa apakah akar berada di antara xl dan xr atau xr dan xu
        root = fl*fr

        if  root < 0:
            xu = xr 
        elif  root > 0:
            xl = xr  
        else:
            ea = 0  

        if ea < es or iterasi > iterasiMax:
            loop = False

        iterasi += 1

    print(table)

    if iterasi > iterasiMax:
        print("The program has exceeded the maximum iterations")
    print("The root is  %.4f" % xr)

if __name__ == "__main__":
    Bisection()
