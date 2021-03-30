def arithmetic_arranger(problems, val=False):
    section = []
    arranged_problems = ""
    count_problems = 0

    # Check for errors

    section = [problem.split(" ") for problem in problems]
    print(section)

    for case in section:
        if case[1] == '*' or case[1] == '/':
            count_problems += (case[1] == '*' or case[1] == '/')
            arranged_problems = "Operator must be '+' or '-'."
        if not case[0].isdigit() or not case[2].isdigit():
            count_problems += (not case[0].isdigit()) + (not case[2].isdigit())
            arranged_problems = "Numbers must only contain digits."
        if len(case[0]) > 4 or len(case[2]) > 4:
            count_problems += 1
            arranged_problems = "Numbers cannot be more than four digits."


    if count_problems > 5:
        arranged_problems = "Too many problems"


    # first row
    for test in section:
        width = max(len(test[0]), len(test[2]))
        blank = " " * (width + 2)
        arranged_problems += f"{test[0]:>{width+2}}{blank}"

    arranged_problems += '\n'

    #second row
    for test in section:
        width = max(len(test[0]), len(test[2]))
        blank = " " * (width + 2)
        arranged_problems += f"{test[1]}{test[2]:>{width+1}}{blank}"

    arranged_problems += '\n'

    #third row
    for test in section:
        width = max(len(test[0]), len(test[2]))
        blank = " " * (width + 2)
        border = "-" * (width + 2)
        arranged_problems += border + blank

    if val:
        arranged_problems += "\n"
        for test in problems:
            sum = str(eval(test))
            arranged_problems += f"{sum:>{len(sum)+2}}    "
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
