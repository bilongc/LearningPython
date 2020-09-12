def fibo_number(n):
    if n <= 1:
        return n
    
    num_p2 = 0
    num_p1 = 1

    for i in range(n - 2):
        new_p1 = num_p2 + num_p1
        num_p2 = num_p1
        num_p1 = new_p1
        
    return num_p2 + num_p1

for i in range(10):
    print("The ", i, "th number in Fibonacci sequence is:", fibo_number(i))

def fibo_ratio(n):
    if n <= 1:
        return 0

    fibo_num_prev = fibo_number(n - 1)
    fibo_num_curr = fibo_number(n)

    return fibo_num_prev / fibo_num_curr

n = 20
print("Ratio between ", n, "th and ", n + 1, "th number of Fibonacci sequence is:", fibo_ratio(n))
 
