import prettytable
from tabulate import tabulate

rows = int(input("Anna rivien määrä:\n"))
columns = int(input("Anna sarakkeiden määrä:\n"))


def my_table(num1, num2):
    table = [[""], [""]]
    headers = [[" "], [" "]]
    for i in range(num1):
        table.insert(i, " ")
        for y in range(num2):
            headers.insert(y, " ")
    print(tabulate(table, headers, tablefmt='pretty'))


my_table(rows, columns)
