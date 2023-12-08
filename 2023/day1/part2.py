total = 0

numbers = {
    "one":"o1e",
    "two":"t2o",
    "three":"t3e",
    "four":"f4r",
    "five":"f5e",
    "six":"s6x",
    "seven":"s7n",
    "eight":"e8t",
    "nine":"n9e"
}

with open("2023\day1\input.txt","r") as f:
    lines = f.readlines()

for line in lines:
    for s,n in numbers.items():
        line = line.replace(s,n)
    nums = list(filter(lambda c: c.isnumeric(),line))
    total += int(nums[0] + nums[-1])

print(total)