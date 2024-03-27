def multiplication_table(n):
    table = [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
    return table

def print_table(table):
    for row in table:
        for item in row:
            print(item, end="\t")
        print()

n = int(input("구구단을 몇단까지 출력하겠습니까? "))
table = multiplication_table(n)
print_table(table)