def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
primes = gen_primes()


x = set()
string = ""
y = 0
a = gen_primes()

while y < 2287:
  new_prime = next(a)
  string = string + str(new_prime)
  x |= set([new_prime])
  y+=1

print(len(x))
print(string)
print(len(string))

print(string[10000:10000+5])
