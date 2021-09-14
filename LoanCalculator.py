# parameters: --type=annuity --principal=1000 --payment=99 --interest=1.5
import argparse
import math
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=float)
parser.add_argument("--payment", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()
argsv = sys.argv
if len(argsv) < 5 or args.interest is None:
    print("Incorrect parameters.")
elif args.type == "annuity":
    if args.periods is None:
        if args.principal >= 0 and args.payment >= 0 and args.interest >= 0:
            P = args.principal
            A = args.payment
            interest_ = args.interest
            i = interest_ / (12 * 100)
            n = math.ceil(math.log(A / (A - i * P), 1 + i))
            overpayment = round((A * n) - P)
            if n % 12 == 0:
                print(f"It will take {n // 12} years to repay this loan!")
            else:
                print(f"It will take {n // 12} years and {n % 12} months to repay this loan!")
            print(f"Overpayment = {overpayment}")
        else:
            print("Incorrect parameters.")
    elif args.payment is None:
        if args.principal >= 0 and args.periods >= 0 and args.interest >= 0:
            P = args.principal
            n = args.periods
            interest = args.interest
            i = interest / (12 * 100)
            A = math.ceil(P * (i * (pow(1 + i, n))) / (pow(1 + i, n) - 1))
            overpayment = round((A * n) - P)
            print(f"Your monthly payment = {A}!")
            print(f"Overpayment = {overpayment}")
        else:
            print("Incorrect parameters.")
    elif args.principal is None:
        if args.payment >= 0 and args.periods >= 0 and args.interest >= 0:
            A = args.payment
            n = args.periods
            interest = args.interest
            i = interest / (12 * 100)
            P = math.floor(A / ((i * pow(1 + i, n))/(pow(1 + i, n) - 1)))
            overpayment = round((A * n) - P)
            print(f"Your loan principal = {P}!")
            print(f"Overpayment = {overpayment}")
        else:
            print("Incorrect parameters.")
elif args.type == "diff":
    if args.payment is not None:
        print("Incorrect parameters.")
    elif args.payment is None:
        if args.principal >= 0 and args.periods >= 0 and args.interest >= 0:
            P = args.principal
            n = args.periods
            interest = args.interest
            i = interest / (12 * 100)
            m = 1
            D = 0
            A = 0
            while m <= n:
                D = math.ceil((P / n) + i * (P - (P * (m - 1) / n)))
                A += D
                print(f"Month {m}: payment is {D}")
                m += 1
            overpayment = round(A - P)
            print()
            print(f"Overpayment = {overpayment}")
        else:
            print("Incorrect parameters.")
