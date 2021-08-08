import matplotlib.pyplot as plt
import math

initial_amount = float(input("Enter the initial amount: "))
interest_rate_ent = float(
    input("Enter the interest rate(can be a number between 1 to 100): "))
interest_rate = interest_rate_ent / 100
compoundint = float(input(
    "Enter the number of times you'd like it compound each year (12 for monthly, 1 for yearly):  "))
time_period = float(input("Enter the time period (In years): "))


def calculate_final_amount():
    final_amount = initial_amount * \
        ((1 + interest_rate / compoundint) ** (time_period * compoundint))
    print(final_amount)

if 1 <= compoundint <= 12:
    calculate_final_amount()
else:
    print("Please enter a number between 1 to 12 for the compounding method.")


x = []
y = []
r = (0, time_period)


def loop_da_compounde():
    i = 1
    while i <= time_period:
        y.append(initial_amount * \
        ((1 + interest_rate / compoundint) ** (i * compoundint)))
        x.append(i)
        i += 1
    
loop_da_compounde()
plt.hist(y, len(x), r, color = 'blue', histtype = 'bar', rwidth = 0.1)
plt.xlabel('year')
plt.ylabel('amount')
plt.title('Compounding over years')
plt.savefig('latestgraph.png')
