
def fibonacci_dp(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0] * n
    fib[0], fib[1] = 0, 1

    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib

n = int(input("Enter the number of terms in the Fibonacci series: "))
fibonacci_series = fibonacci_dp(n)

print(f"The first {n} terms of the Fibonacci series are: {fibonacci_series}")
