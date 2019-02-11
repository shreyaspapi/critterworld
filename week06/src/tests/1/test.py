import random

for i in range(1, 6):
    doc = open("{}.txt".format(i), "w")

    t = random.randint(1, 10)
    
    doc.write(str(t) + "\n")
    for _ in range(t):
        n = random.randint(1, 20000)
        doc.write(str(n) + "\n")
        for _ in range(n-1):
            x = random.randint(1, n)
            y = random.randint(1, n)
            while x == y:
                y = random.randint(1, n)
            z = random.randint(1, 10**9)
            doc.write(str(x) + " " + str(y) + " " + str(z) + "\n")
        
            
