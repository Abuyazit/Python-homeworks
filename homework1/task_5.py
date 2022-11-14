def reverse_int(n):
    f=str(n)
    return int(f[::-1])


assert(reverse_int(1000)) == 1
assert(reverse_int(142522)) == 225241
assert(reverse_int(104)) == 401
assert(reverse_int(10001)) == 10001
assert(reverse_int(111111111)) == 111111111
assert(reverse_int(101010101010000000000000000)) == 10101010101

