# easy, don't need to explain




data = []
f = open('file.txt', 'r')

for line in f.readlines():
    _, values = line.split(':')
    data.append(values.strip())


race_dict = {}

for i, line in enumerate(data):
    if i % 2 == 0:
        time = line.split()
    else:
        distance = line.split()



for t, d in zip(time, distance):
    race_dict[t] = d

race_dict = {int(key): int(value) for key, value in race_dict.items()}


number_of_ways = 1

for time, distance in race_dict.items():
    count = 0
   
    for hold in range(time):
        actual_time = time
        time_left = actual_time - hold
        speed = hold
        distance_traveled = speed * time_left

        if distance_traveled > distance:
            count += 1

    number_of_ways *= count

print(number_of_ways)





