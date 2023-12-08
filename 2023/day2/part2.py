total_power = 0

with open("2023\day2\input.txt") as f:
    lines = f.read().split("\n")

for line in lines:
    _, subsets = line.split(":")
    sets = subsets.split(";")
    
    game_max_color = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for set in sets:
        colors = set.split(",")

        for color_info in colors:

            number,color = color_info.strip().split(" ")
            number = int(number)

            if game_max_color[color] < number:
                game_max_color[color] = number

    total_power += game_max_color["red"] * game_max_color["green"] * game_max_color["blue"]

print(total_power)