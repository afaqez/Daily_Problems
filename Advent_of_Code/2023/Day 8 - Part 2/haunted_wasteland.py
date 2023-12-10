direction = 'LR'
dict = {
    '11A': ['11B', 'XXX'],
    '11B': ['XXX', '11Z'],
    '11Z': ['11B', 'XXX'],
    '22A': ['22B', 'XXX'],
    '22B': ['22C', '22C'],
    '22C': ['22Z', '22Z'],
    '22Z': ['22B', '22B'],
    'XXX': ['XXX', 'XXX']
}

starting_strings = []

for state in dict.keys():
    if state[2] == 'A':
        starting_strings.append(state)

print(starting_strings)

        


count = 0
current_state = 'hello'

for state in starting_strings:
    while True:
        for char in direction:
            if char == 'L':
                current_state = dict[current_state][0]
                count += 1
            else:
                current_state = dict[current_state][1]
                count += 1









# found_zzz = False
# for state, directions in dict.items():
#     current_state = state
#     if state == 'AAA':
#         while True:
#             for i, char in enumerate(direction):
#                 if char == 'L':
#                     current_state = dict[current_state][0]
#                     count += 1
#                 else:
#                     current_state = dict[current_state][1]
#                     count += 1
#                 if current_state == 'ZZZ':
#                     found_zzz = True
#                     break
#             if found_zzz:
#                 break
#         if found_zzz:
#             break


               
# print(count)
# print(current_state)



