# split card_info and card_details using .split()
# further split the cart_details based on ' | '
# maybe turn into list
# check every winning number against every number that we actually get
# there are two ways to get the total points; one of them is to get 2^number_of_matches - 1 
# or we just simply multiply the number of points we previously got by two




f = open('file.txt', 'r')
points = 0

for card in f.readlines():
    card_info, card_details = card.split(':')
    winning_string, elf_string = card_details.split('|')
    winning_numbers = []
    elf_numbers = []


    winning_numbers = winning_string.split()
    elf_numbers = elf_string.split()

    winning_numbers = [int(num) for num in winning_numbers]
    elf_numbers = [int(num) for num in elf_numbers]
    

    count = 0

    for winning_number in winning_numbers:
        for elf_number in elf_numbers:
            if winning_number == elf_number:
                count += 1
                points = 2^count


print(points) 



