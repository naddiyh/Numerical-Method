import math
from prettytable import PrettyTable

# Mendefinisikan function
def f(x):
    return 5 - 5*x - math.exp(0.5*x)


def d(x):
    return -5 - 0.5*math.exp(0.5*x)

def NewtonRapshon(xi=0.7):
    es = 2  # Toleransi erorr
    iterasiMax = 100  # Maximum iterations

    print("\nNewton-Raphson Method")
    print("xi = 0.7\n ")
    loop = True
    iterasi = 0

    # Membuat Tabel
    table = PrettyTable()
    table.field_names = ["Iterasi", "x\u1D62", "f(x\u1D62)", "f'(x\u1D62)", "x\u1D62\u208A\u2081", "ea(%)"]

    while(loop):
        iterasi += 1
        xOld = xi
        xi = xOld - f(xOld)/d(xOld) 

        # Menghitung approximation error
        if not xi == 0:
            ea = abs((xi-xOld)/xi)*100

        # Menambahkan hasil iterasi ke dalam tabel
        table.add_row([iterasi, "%.4f" % xOld, "%.4f" % f(xOld), "%.4f" % d(xOld), "%.4f" % xi, "%.3f" % ea])

        if ea < es or iterasi > iterasiMax:
            loop = False


    print(table)
    if iterasi > iterasiMax:
        print("The program has exceeded the maximum iterations")
    print("The root is  %.4f" % xi)

if __name__ == "__main__":
    NewtonRapshon()
