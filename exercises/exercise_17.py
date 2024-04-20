rows = int(input())
columns = int(input())

for i in range(rows):
    row = ""
    for j in range(columns):
        row += f"{i}\t"

    print(row)
  
