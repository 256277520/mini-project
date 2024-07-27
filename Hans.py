"""Data science foundation assignment
Turn raw data into meaningful information
"""

data = open("./data.txt", "r")
file_number = 1
num_of_times = {}
lines_at = {}

for line in data:
    line = line.rstrip().split(" ")
    
    for num in line:
        if int(num) not in num_of_times.keys():
            num_of_times[int(num)] = 1
        else:
            num_of_times[int(num)] += 1
            
        if int(num) not in lines_at.keys():
            lines_at[int(num)] = [file_number]
        else:
            lines_at[int(num)].append(file_number)

    file_number += 1
print(f"{num_of_times}\n")

for k,v in lines_at.items():
    print(f"{k}: {{{', '.join(map(str, v))}}}", end=",\n")