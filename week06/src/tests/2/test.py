import random

for i in range(1, 6):
    doc = open("{}.txt".format(i), "w")
    
    t = random.randint(1, 5)
    doc.write(str(t)+"\n")
    for _ in range(t):
        n, q = random.randint(1, 10 ** 5), random.randint(1, 10**5)
        doc.write(str(n) + " " + str(q) + "\n")
        for _ in range(n-1):
            u, v = random.randint(1, n), random.randint(1, n)
            while n == v:
                v = random.randint(1, n)
            doc.write(str(u) + " " + str(v) + "\n")
        for _ in range(q):
            x, y = random.randint(1, n), random.randint(1, n)
            while x == y:
                y = random.randint(1, n)
            doc.write(str(x) + " " + str(y) + "\n")
