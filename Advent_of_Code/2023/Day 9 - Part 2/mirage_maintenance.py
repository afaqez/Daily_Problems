# used dictionary logic in the beginning, but of course the code didn't run and it was not optimized
# optimized it a little and then used all() function with the help of Abon



sum_of_num = 0

with open('file.txt', 'r') as file:
    lines = file.readlines()

# lines = [
#     '0 3 6 9 12 15',
#     '1 3 6 10 15 21',
#     '10 13 16 21 30 45'
# ]

for line in lines:
    abon = []
    sequence = []
    data = line.split()
    data = [int(num) for num in data]
    abon.append(data[0])

    sequence = data

    while all(number == 0 for number in sequence) == False:   
        temp = []
        for i in range(len(sequence) - 1):
            diff = sequence[i + 1] - sequence[i]
            temp.append(diff)
        
        sequence = temp
        
        abon.append(sequence[0])
    
    print(abon)
    # sum_of_num += sum(abon)
    
    for i in range(len(abon) -1, -1 , -1):
        abon[i - 1] = abon[i - 1] - abon[i]
    
    sum_of_num += abon[0]

print(sum_of_num)



