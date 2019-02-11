import random

for i in range(1, 6):
    doc = open("{}.txt".format(i), "w")

    t = random.randint(1, 10)
    doc.write(str(t) + "\n")
    for _ in range(t):
        n = random.randint(2, 10**6)
        m = random.randint(2, n)
        doc.write(str(n) + " " + str(m) + "\n")

        for i in range(n-1):
            u, v = random.randint(1, n), random.randint(1, n)
            doc.write(str(u) + " " + str(v) + "\n")

        m_space = random.sample(range(1, n), m-1)
        str_m = ""
        for i in m_space:
            str_m += (str(i) + " ")

        doc.write(str_m + "\n")
    
    doc.close()
print("Done")

