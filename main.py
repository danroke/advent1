# import
# 

List_A = []
List_B = []
Total_distance = 0
# Read the input and save into 2 lists
with open('input.txt', 'r') as file:
    for row in file:    
        line = row.split()

        line_A = int(line[0])
        line_B = int(line[1])

        List_A.append(line_A)
        List_B.append(line_B)

# Sort the lists
List_A.sort()
List_B.sort()

# loop over lists, and compute the distance between each pair
while List_A:
    num_A = List_A.pop()
    num_B = List_B.pop()
    Total_distance = Total_distance + abs(int(num_A) - int(num_B))

print("Total Distance between the input lists is ", Total_distance)