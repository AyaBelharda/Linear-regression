import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

def gradient_descent(a, b, points, L):
    n = len(points)
    gradient_a = 0
    gradient_b = 0

    for i in range(n):
        x = points.iloc[i].X
        y = points.iloc[i].Y

        gradient_a += -(2/n) * x * (y - (a * x + b))
        gradient_b += -(2/n) * (y - (a * x + b))

    a -= gradient_a * L
    b -= gradient_b * L

    return a, b

a = 0
b = 0
L = 0.0001
iterations = 1000

for i in range(iterations):

    a, b = gradient_descent(a, b, data, L)

# Plot the final regression line
plt.scatter(data.X, data.Y, color="black")
plt.plot(range(0, 100), [a * x + b for x in range(0, 100)], color="red")
plt.show()
