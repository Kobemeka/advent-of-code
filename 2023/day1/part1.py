total = 0

with open("2023\day1\input.txt","r") as f:
    lines = f.readlines()

for line in lines:
    nums = list(filter(lambda c: c.isnumeric(),line))
    total += int(nums[0] + nums[-1])
    
print(total)