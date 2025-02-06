def fibonacci_series(n):
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series

if __name__ == "__main__":
    n = int(input("Enter the number of terms in the Fibonacci series: "))
    series = fibonacci_series(n)
    print("Fibonacci series:", series)

