import matplotlib.pyplot as plt
import math

initial_amount = float(input("Enter the initial amount [10000]: ") or "10000")
interest_rate_ent = float(
    input("Enter the interest rate(can be a number between 1 to 100) [8]: ") or "8")
interest_rate = interest_rate_ent / 100
compoundint = float(input(
    "Enter the number of times you'd like it compound each year (12 for monthly, 1 for yearly) [12]:  ") or "12")
time_period = float(input("Enter the time period (In years) [10]: ") or "10")


def calculate_final_amount():
    final_amount = initial_amount * \
        ((1 + interest_rate / compoundint) ** (time_period * compoundint))
    print(round(final_amount, 2))


if 1 <= compoundint <= 12:
    calculate_final_amount()
else:
    print("Please enter a number between 1 to 12 for the compounding method.")


x = []
y = []


def loop_compound():
    i = 1
    while i <= time_period:
        y.append(initial_amount *
                 ((1 + interest_rate / compoundint) ** (i * compoundint)))
        x.append(i)
        i += 1


loop_compound()
print("x", x)
print("y", y)
plt.bar(x, y, width=0.72)
plt.plot(x, y, marker='o', markerfacecolor='blue', markersize='2')
plt.xlabel('year')
plt.ylabel('amount')
plt.title('compounding over years')
low = min(y)
high = max(y)
plt.ylim([math.ceil(low-0.1*(high-low)), math.ceil(high+0.1*(high-low))])
plt.xticks(x)
plt.savefig("latestgraph.png")
plt.show()
