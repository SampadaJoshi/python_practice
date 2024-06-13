def count_ones(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

print(count_ones(12))  # Output: 2
