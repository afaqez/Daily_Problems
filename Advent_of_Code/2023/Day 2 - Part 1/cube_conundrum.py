# the main functionality will be based on the split() function
# i will be splitting each line based on a heirarchy
# the first split will always be ':' and the last split will be based on a ' ' (space)
# after I get each 'single_configuration', a flag will be used, if the flag == False then don't count that Game ID
# if the flag stays True then count that GameID in the overall sum


f = open('file.txt', 'r')
id_sum = 0

for line in f.readlines():

    # split Game ID and Game Details
    game_id, game_details = line.split(':')

    # get the game ID number and sum it on each iteration
    game_id = game_id.split(' ')
    game_id = int(game_id[1])

    # get the game details in seperate indexes to perform smooth operations
    cube_list = []
    cube_list = game_details.split(';')
    game_dict = {
        'red': 12,
        'green': 13,
        'blue': 14
    }


    for i, configuration in enumerate(cube_list):
        configuration_list = []
        configuration_list = configuration.split(',')
        configuration_list = [item.strip() for item in configuration_list]

        for single_configuration in configuration_list:
            number_of_color, color = single_configuration.split(' ')
            flag = True
            if int(number_of_color) > game_dict[color]:
                flag = False
            if flag == False:
                break

        if flag == False:
            break

    if flag == True:
        id_sum += game_id

print(id_sum)
