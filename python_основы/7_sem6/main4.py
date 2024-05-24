def sum_div(n):
    total = 1
    sq_n = n ** 0.5
    sq_n_int = int(sq_n)
    if sq_n == sq_n_int:
        total += sq_n_int
    for div in range(2, sq_n_int):
        if n % div == 0:
            total += div + n // div

    return total


k = 300000

for num1 in range(2, k + 1):
    num2 = sum_div(num1)
    if num1 < num2 <= k and num1 == sum_div(num2):
        print(num1, num2)

