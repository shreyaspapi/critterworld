import random

for i in range(1, 6):
    doc = open("{}.txt".format(i), "w")

    t = random.randint(1, 10)
    doc.write(str(t) + "\n")
    for _ in range(t):
        
        n = random.randint(1, 1000)

        h = random.randint(1, 24)

        doc.write(str(n) + " " + str(h) + "\n")

        n_space = ""

        for j in range(n):
            n_space += str(random.randint(1, 24)) + " "

        doc.write(str(n_space) + "\n")

        for _ in range(n):
            x = random.randint(1, 10)

            x_space = ""

            for _ in range(x):
                x_space += str(random.randint(1, 10)) + " "

            x_final = str(x) + " " + x_space

            doc.write(x_final + "\n")
    
        
