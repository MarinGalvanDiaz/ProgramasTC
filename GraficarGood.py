k = 29

with open("resultadogood.txt", "w") as f:
    f.write(f"0\n")
    for l in range(1, k+1):
        for i in range(2 ** l):
            count_ones = bin(i).count('1')
            f.write(f"{count_ones}\n")