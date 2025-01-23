prev, curr = 0, 1

even_fib_sum = 0
even_fib_count = 0

while even_fib_count < 100:
    next_fib = prev + curr
    
    prev, curr = curr, next_fib
    
    if next_fib % 2 == 0:
        even_fib_sum += next_fib
        even_fib_count += 1

print("The sum of the first 100 even Fibonacci numbers is:", even_fib_sum)
