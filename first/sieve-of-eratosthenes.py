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
while True:
  new_prime = next(a)
  string = string + str(new_prime)
  if len(string) >= 10004:
      print(y+1, string)
      break
  x |= set([new_prime])
  y+=1
