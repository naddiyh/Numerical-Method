import math
from prettytable import PrettyTable


# Mendefinisikan Fungsi
def f(x):
    return 5 - 5*x - math.exp(0.5*x)

def Secant(x_prev=0, x_curr=2):
    es = 2 #toleransi erorr
    iterasiMax = 100      # Maksimum Iterasi

    print("\nSecant Method")
    print("xi−1 = 0 \nxi = 2\n")
    loop = True
    iterasi= 1
    
    #Mmebuat Tabel
    table = PrettyTable()
    table.field_names = ["Iterasi", "x\u1D62\u208B\u2081",
                          "f(x\u1D62\u208B\u2081)", "x\u1D62", "f(x\u1D62)", "x\u1D62\u208A\u2081", "ea(%)"]

    while(loop):
        x_next = x_curr - (f(x_curr)*(x_prev-x_curr))/(f(x_prev)-f(x_curr))
        
        #Menghitung approxiamate erorr
        if not x_next == 0:
            ea = abs((x_next-x_curr)/x_next)*100
        
        #Menambahkan hasil ke tabel
        table.add_row([iterasi, "%.4f" % x_prev, "%.4f" % f(
            x_prev), "%.4f" % x_curr, "%.4f" % f(x_curr), "%.4f" % x_next, "%.3f" % ea])

        x_prev, x_curr = x_curr, x_next
        iterasi+= 1

        if ea < es:
            loop = False
        if iterasi >  iterasiMax :
            loop = False

    print(table)
    if iterasi > iterasiMax :
        print("The program has exceeded the maximum iterations")
    print("The root is %.4f" % x_next)

if __name__ == "__main__":
    Secant()
