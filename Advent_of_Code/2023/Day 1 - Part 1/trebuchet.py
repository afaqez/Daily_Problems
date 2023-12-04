# this is easy 
# just the indexes tbh


f = open('file.txt', 'r')
nums_to_add = []

for line in f.readlines():
    line_str = line
    str_list = list(line_str)
    nums = []


    for letter in str_list:
        if letter.isnumeric():
            nums.append(letter)

    n = len(nums)
    temp = str(nums[0]) + str(nums[n - 1])
    nums_to_add.append(int(temp))

f.close()

result = sum(nums_to_add)
print(result)