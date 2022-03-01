def computepay(h, r):
    pay = 0
    if float(h) < 40:
        pay = float(h) * float(r)
    else:
        pay = 40 * float(r) + 1.5 * (float(h) - 40) * float(r)
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs, rate)
print("Pay", p)