import math
from prettytable import PrettyTable


def f(x):
    return 5 - 5*x - math.exp(0.5*x)


def d(x):
    return -5 - 0.5*math.exp(0.5*x)


# Variable
es = 2
imax = 100      # Maksimum Iterasi


def Bisect(xl=0, xu=2):
    print("\nBisection Method")
    loop = True
    iter = 0
    xr = 0

    table1 = PrettyTable()
    table1.field_names = ["i", "xl",
                          "f(xl)", "xu", "f(xu)", "xr", "f(xr)", "ea(%)"]

    while(loop):
        fl = f(xl)
        fu = f(xu)

        xrold = xr
        xr = (xl + xu) / 2
        fr = f(xr)

        if not xr == 0:
            ea = abs((xr-xrold)/xr)*100

        if iter == 0:
            table1.add_row([iter, "%.4f" % xl, "%.4f" % fl, "%.4f" %
                            xu, "%.4f" % fu, "%.4f" % xr, "%.4f" % fr, "-"])
        else:
            table1.add_row([iter, "%.4f" % xl, "%.4f" % fl, "%.4f" %
                            xu, "%.4f" % fu, "%.4f" % xr, "%.4f" % fr, "%.3f" % ea])

        test = fl*fr

        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0

        if ea < es:
            loop = False
        if iter > imax:
            loop = False

        iter = iter + 1

    print(table1)
    if iter > imax:
        print("The program has exceeded the maximum iterations")
    print("The solution is approximately %.4f" % xr)


def NewRap(xi=0.7):
    print("\nNewton-Raphson Method")
    loop = True
    iter = 0

    table2 = PrettyTable()
    table2.field_names = [
        "Iter", "x\u1D62", "f(x\u1D62)", "f'(x\u1D62)", "x\u1D62\u208A\u2081", "ea(%)"]
    # table2.add_row([iter, "%.4f" % xi, "-"])

    while(loop):
        iter += 1
        xold = xi
        xi = xold - f(xold)/d(xold)

        if not xi == 0:
            ea = abs((xi-xold)/xi)*100

        table2.add_row([iter, "%.4f" % xold, "%.4f" %
                        f(xold), "%.4f" % d(xold), "%.4f" % xi, "%.3f" % ea])

        if ea < es:
            loop = False
        if iter > imax:
            loop = False

    print(table2)
    if iter > imax:
        print("The program has exceeded the maximum iterations")
    print("The solution is approximately %.4f" % xi)


def Secant(x_prev=0, x_curr=2):
    print("\nSecant Method")
    loop = True
    iter = 1

    table3 = PrettyTable()
    table3.field_names = ["Iter", "x\u1D62\u208B\u2081",
                          "f(x\u1D62\u208B\u2081)", "x\u1D62", "f(x\u1D62)", "x\u1D62\u208A\u2081", "ea(%)"]

    while(loop):
        x_next = x_curr - (f(x_curr)*(x_prev-x_curr))/(f(x_prev)-f(x_curr))

        if not x_next == 0:
            ea = abs((x_next-x_curr)/x_next)*100

        table3.add_row([iter, "%.4f" % x_prev, "%.4f" % f(
            x_prev), "%.4f" % x_curr, "%.4f" % f(x_curr), "%.4f" % x_next, "%.3f" % ea])

        x_prev, x_curr = x_curr, x_next
        iter += 1

        if ea < es:
            loop = False
        if iter > imax:
            loop = False

    print(table3)
    if iter > imax:
        print("The program has exceeded the maximum iterations")
    print("The solution is approximately %.4f" % x_next)


# No. 1
Bisect()
# No. 2
NewRap()
# No. 3
Secant()

dum = input("")