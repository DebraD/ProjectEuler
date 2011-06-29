# Calculate the sum of even valued Fibonacci numbers that are less than 4 million.

sum = 0

Fibonacci_n_1 = 1
Fibonacci_n_2 = 0

while Fibonacci_n_1 < 4000000:
    Fibonacci_sum = Fibonacci_n_1 + Fibonacci_n_2

    Fibonacci_n_2 = Fibonacci_n_1
    Fibonacci_n_1 = Fibonacci_sum
    if Fibonacci_sum % 2 == 0:
        sum += Fibonacci_sum

print sum
