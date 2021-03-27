def arithmetic_arranger(problems, *args):
    kalkulacija = ""
    line = ""

    for vl in problems:
        tc = vl.split(" ")
        kalkulacija += "{:>6}\n{:>1} {:>4}\n".format(tc[0], tc[1], tc[2])
        line += kalkulacija


    print(line)





arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)


# racunanje = "{:>6}\n{:>1} {:>4}".format("32", "+", "8")
# racunanje1 = "{:>6}\n{:>1} {:>4}".format("1", "-", "3801")
# print(racunanje,"\t",racunanje1)


