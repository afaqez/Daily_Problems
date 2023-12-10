data = []
f = open('file.txt', 'r')

for line in f.readlines():
    _, values = line.split(':')
    data.append(values.strip())

data_list = []

for line in data:
    for char in line:
        if char != ' ':
            data_list.append(char)
    
    data_list.append(' | ')

temp = ''.join(data_list)
print(temp)

time, distance, _ = temp.split(' | ')

time = int(time)
distance = int(distance)
print(time, distance)

# race_dict = {}

# for i, line in enumerate(data):
#     if i % 2 == 0:
#         time = line.split()
#     else:
#         distance = line.split()

# print(time, distance)

# for t, d in zip(time, distance):
#     race_dict[t] = d

# race_dict = {int(key): int(value) for key, value in race_dict.items()}


# number_of_ways = 1

# for time, distance in race_dict.items():
count = 0
   
for hold in range(time):
    actual_time = time
    time_left = actual_time - hold
    speed = hold
    distance_traveled = speed * time_left

    if distance_traveled > distance:
        count += 1



print(count)





