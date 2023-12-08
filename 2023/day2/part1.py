id_sum = 0
conditions = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

with open("2023\day2\input.txt") as f:
    lines = f.read().split("\n")

for line in lines:
    game, subsets = line.split(":")
    game_id = int(game[5:])
    sets = subsets.split(";")
    
    possible_set = []

    for set in sets:
        colors = set.split(",")
        possible_color_config = []

        for color_info in colors:
            number,color = color_info.strip().split(" ")
            if conditions[color] >= int(number):
                possible_color_config.append(True)
            else:
                possible_color_config.append(False)

        possible_set.append(all(possible_color_config))
    
    if all(possible_set):
        id_sum += game_id

print(id_sum)