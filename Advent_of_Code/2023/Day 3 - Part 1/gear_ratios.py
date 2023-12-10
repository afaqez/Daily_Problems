data = ["467..114..", 
        "...*......", 
        "..35..633.", 
        "......#...", 
        "617*......", 
        ".....+.58.", 
        "..592.....", 
        "......755.", 
        "...$.*....", 
        ".664.598.."]



for i, line in enumerate(data):
    for char in line:
        if char.isnumeric() == False and char != '.':
            symbol = char
            symbol_index = line.index(symbol)
            