# the main functionality will be based on the split() function
# i will be splitting each line based on a heirarchy
# the first split will always be ':' and the last split will be based on a ' ' (space)
# after I get each 'single_configuration', it will be further splitted into two different variables of color and number_of_color
# i will be appending the number_of_color in front of my game_dict and at the end, i will get the maximum number of each color and multiply it with the other
# after each iteration, the product will be added to a variable (result variable)




f = open('file.txt', 'r')
sum_of_prod = 0
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
        'red': [],
        'green': [],
        'blue': []
    }


    for i, configuration in enumerate(cube_list):
        configuration_list = []
        configuration_list = configuration.split(',')
        configuration_list = [item.strip() for item in configuration_list]

        for single_configuration in configuration_list:
            number_of_color, color = single_configuration.split(' ')
            game_dict[color].append(int(number_of_color))
        
    # print(game_dict)
    product_of_min = 1
    for color, number_of_color in game_dict.items():
        product_of_min *= max(game_dict[color])

    sum_of_prod += product_of_min

print(sum_of_prod)



        

