import random

for i in range(1, 6):
    doc = open("{}.txt".format(i), "w")

    t = random.randint(1, 5)
    doc.write(str(t) + "\n")

    for _ in range(t):
        n = random.randint(2, 10**5)

        doc.write(str(n) + "\n")

        n_space = ""

        for _ in range(n):
            w = random.randint(-10**8, 10**8)
            n_space += str(w) + " "

        doc.write(n_space + "\n")

        t_space = ""

        for _ in range(n):
            t = random.randint(1, n)
            t_space += str(t) + " "

        doc.write(t_space + "\n")
    doc.close()
