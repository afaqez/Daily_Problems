# kinda used brute force technique in it
# i just the number of times i should analyze each card
# and by 'analyze', I mean running the for loop operations (matching the winning and elf numbers)



f = open('file.txt', 'r')
scratchcards_dict = {}
sum_of_scratchcards = 0


for card in f.readlines():
    card_info, card_details = card.split(':')
    card_name, card_id = card_info.split()
    card_id = int(card_id)
    scratchcards_dict[card_id] = 1

f.seek(0)

for card in f.readlines():
    count = 0
    card_info, card_details = card.split(':')
    card_name, card_id = card_info.split()
    card_id = int(card_id)

    for i in range(scratchcards_dict[card_id]):
        count = 0
        winning_string, elf_string = card_details.split('|')
        winning_numbers = []
        elf_numbers = []
        

        winning_numbers = winning_string.split()
        elf_numbers = elf_string.split()

        winning_numbers = [int(num) for num in winning_numbers]
        elf_numbers = [int(num) for num in elf_numbers]


        for winning_number in winning_numbers:
            for elf_number in elf_numbers:
                if winning_number == elf_number:
                    count += 1

        for card_number in range(count):
            copy = (card_number + 1) + card_id
            scratchcards_dict[copy] += 1

for card_number, number_of_copies in scratchcards_dict.items():
    sum_of_scratchcards += number_of_copies

print(sum_of_scratchcards)



   





