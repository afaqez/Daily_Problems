# cooked abon's logic in the end, because of time complexity
# mine was also similar









# # Define data structures to store information
# seeds = []
# seed_to_soil_map = []
# soil_to_fertilizer_map = []
# fertilizer_to_water_map = []
# water_to_light_map = []
# light_to_temperature_map = []
# temperature_to_humidity_map = []
# humidity_to_location_map = []

# # Read input from file
# with open('file.txt', 'r') as file:
#     lines = file.readlines()

# # Process each line and store information in respective data structures
# # Define data structures to store information
# seeds = []
# seed_to_soil_map = []
# soil_to_fertilizer_map = []
# fertilizer_to_water_map = []
# water_to_light_map = []
# light_to_temperature_map = []
# temperature_to_humidity_map = []
# humidity_to_location_map = []

# # Define data structures to store information
# seeds = []
# seed_to_soil_map = []
# soil_to_fertilizer_map = []
# fertilizer_to_water_map = []
# water_to_light_map = []
# light_to_temperature_map = []
# temperature_to_humidity_map = []
# humidity_to_location_map = []

# # Define data structures to store information
# seeds = []
# seed_to_soil_map = []
# soil_to_fertilizer_map = []
# fertilizer_to_water_map = []
# water_to_light_map = []
# light_to_temperature_map = []
# temperature_to_humidity_map = []
# humidity_to_location_map = []

# # Define data structures to store information
# seeds = []
# seed_to_soil_map = []
# soil_to_fertilizer_map = []
# fertilizer_to_water_map = []
# water_to_light_map = []
# light_to_temperature_map = []
# temperature_to_humidity_map = []
# humidity_to_location_map = []

# # Define data structures to store information
# seeds = []
# seed_to_soil_map = []
# soil_to_fertilizer_map = []
# fertilizer_to_water_map = []
# water_to_light_map = []
# light_to_temperature_map = []
# temperature_to_humidity_map = []
# humidity_to_location_map = []

# # Read input from file
# with open('file.txt', 'r') as file:
#     lines = file.readlines()

# # Function to parse variable-sized mappings
# def parse_mapping(lines, start_index, end_delimiter):
#     mapping = []
#     i = start_index + 1  # Move to the next line after the section heading
#     while i < len(lines) and not lines[i].startswith(end_delimiter):
#         mapping.append(list(map(int, lines[i].split())))
#         i += 1
#     return mapping, i  # Return the parsed mapping and the current index

# # Process each line and store information in respective data structures
# i = 0
# while i < len(lines):
#     line = lines[i]
#     if line.startswith('seeds:'):
#         seeds = list(map(int, line.split(':')[1].split()))
#     elif line.startswith('seed-to-soil map:'):
#         seed_to_soil_map, i = parse_mapping(lines, i, 'soil-to-fertilizer map:')
#     elif line.startswith('soil-to-fertilizer map:'):
#         soil_to_fertilizer_map, i = parse_mapping(lines, i, 'fertilizer-to-water map:')
#     elif line.startswith('fertilizer-to-water map:'):
#         fertilizer_to_water_map, i = parse_mapping(lines, i, 'water-to-light map:')
#     elif line.startswith('water-to-light map:'):
#         water_to_light_map, i = parse_mapping(lines, i, 'light-to-temperature map:')
#     elif line.startswith('light-to-temperature map:'):
#         light_to_temperature_map, i = parse_mapping(lines, i, 'temperature-to-humidity map:')
#     elif line.startswith('temperature-to-humidity map:'):
#         temperature_to_humidity_map, i = parse_mapping(lines, i, 'humidity-to-location map:')
#     elif line.startswith('humidity-to-location map:'):
#         humidity_to_location_map, i = parse_mapping(lines, i, 'end-of-file-marker')

# # Print or use the extracted information as needed
# print("Seeds:", seeds)
# print("Seed-to-soil map:", seed_to_soil_map)
# print("Soil-to-fertilizer map:", soil_to_fertilizer_map)
# print("Fertilizer-to-water map:", fertilizer_to_water_map)
# print("Water-to-light map:", water_to_light_map)
# print("Light-to-temperature map:", light_to_temperature_map)
# print("Temperature-to-humidity map:", temperature_to_humidity_map)
# print("Humidity-to-location map:", humidity_to_location_map)



# # seeds = [79, 14, 55, 13]
# # seed_to_soil_map = [[50, 98, 2], [52, 50, 48]]
# # soil_to_fertilizer_map = [[0, 15, 37], [37, 52, 2], [39, 0, 15]]
# # fertilizer_to_water_map = [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]]
# # water_to_light_map = [[88, 18, 7], [18, 25, 70]]
# # light_to_temperature_map = [[45, 77, 23], [81, 45, 19], [68, 64, 13]]
# # temperature_to_humidity_map = [[0, 69, 1], [1, 0, 69]]
# # humidity_to_location_map = [[60, 56, 37], [56, 93, 4]]


# seed_soil = {}
# soil_fertilizer = {}
# fertilizer_water = {}
# water_light = {}
# light_temperature = {}
# temperature_humidity = {}
# humidity_location = {}
# seed_location = {}

# def get_mapping(map_list, key):
#     map_dict = {}
#     for i in range(len(map_list)):
#         destination = map_list[i][0]
#         source = map_list[i][1]
#         range_of_map = map_list[i][2]
#         # for i in range(destination):
#         #     map_dict[i] = i

#         for i in range(range_of_map):
#             map_dict[source] = destination
#             source += 1
#             destination += 1
#     # print(map_list)
#     # print(map_dict)

#     if key not in map_dict.keys():
#         return key
    
#     return map_dict[key]



# def main():
#     locations = []
#     for seed in seeds:
#         soil = get_mapping(seed_to_soil_map, seed)
#         fertilizer = get_mapping(soil_to_fertilizer_map, soil)
#         water = get_mapping(fertilizer_to_water_map, fertilizer)
#         light = get_mapping(water_to_light_map, water)
#         temperature = get_mapping(light_to_temperature_map, light)
#         humidity = get_mapping(temperature_to_humidity_map, temperature)
#         location = get_mapping(humidity_to_location_map, humidity)
#         locations.append(location)
    
#     print(locations)

# main()


data = []

# Read input from file
with open('file.txt', 'r') as file:
    lines = file.readlines()
    data.append(lines)

data = data[0]
seeds_str = data[0]
_, seeds_arr = seeds_str.split(': ')
seeds = [int(string) for string in seeds_arr.split()]

data.pop(0)
data.remove('\n')

arr = []
dictionary = {}
for line in data:
    line = line.strip()

    if line != '':
        arr.append(line)
    else:
        name_arr = arr[0].split()[0]
        num_arr = arr[1:]
        new_num_arr = []
        for string in num_arr:
            new_num_arr.append([int(st) for st in string.split()])

        dictionary[name_arr] = new_num_arr
        arr = []

# For the last thing in arr
name_arr = arr[0].split()[0]
num_arr = arr[1:]
new_num_arr = []
for string in num_arr:
    new_num_arr.append([int(st) for st in string.split()])

dictionary[name_arr] = new_num_arr

seed_to_soil_map = dictionary['seed-to-soil']
soil_to_fertilizer_map = dictionary['soil-to-fertilizer']
fertilizer_to_water_map = dictionary['fertilizer-to-water']
water_to_light_map = dictionary['water-to-light']
light_to_temperature_map = dictionary['light-to-temperature']
temperature_to_humidity_map = dictionary['temperature-to-humidity']
humidity_to_location_map = dictionary['humidity-to-location']

# Print or use the extracted information as needed
# print("Seeds:", seeds)
# print("Seed-to-soil map:", seed_to_soil_map)
# print("Soil-to-fertilizer map:", soil_to_fertilizer_map)
# print("Fertilizer-to-water map:", fertilizer_to_water_map)
# print("Water-to-light map:", water_to_light_map)
# print("Light-to-temperature map:", light_to_temperature_map)
# print("Temperature-to-humidity map:", temperature_to_humidity_map)
# print("Humidity-to-location map:", humidity_to_location_map)

def get_item(item, item_mapping):

    range_found = False
    for destination, source, range_length in item_mapping:
        if item >= source and item < (source + range_length):
            range_found = True
            return destination + abs(item - source)

    if range_found == False:
        return item

minimum_location = float('inf')

for seed in seeds:
    soil = get_item(seed, seed_to_soil_map)
    fertilizer = get_item(soil, soil_to_fertilizer_map)
    water = get_item(fertilizer, fertilizer_to_water_map)
    light = get_item(water, water_to_light_map)
    temperature = get_item(light, light_to_temperature_map)
    humidity = get_item(temperature, temperature_to_humidity_map)
    location = get_item(humidity, humidity_to_location_map)
    
    if minimum_location > location:
        minimum_location = location

print("Minimum : ", minimum_location)

