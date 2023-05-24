def caseDetector(letter):
    if letter.islower():
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27

def find_common_items(rucksacks):
    total_priority = 0

    for rucksack in rucksacks:
        compartment_size = len(rucksack) // 2
        first_compartment = set(rucksack[:compartment_size])
        second_compartment = set(rucksack[compartment_size:])
        common_items = first_compartment.intersection(second_compartment)

        for letter in common_items:
            total_priority += caseDetector(letter)

    return total_priority

with open('rucksack.txt', 'r') as file:
    lines = file.readlines()

rucksacks = [line.strip() for line in lines]

total_priority = find_common_items(rucksacks)
print(total_priority)

#Part2
total_priority2 = 0
for i in range(0, len(rucksacks), 3):
    r1, r2, r3 = rucksacks[i:i+3]
    common_items = set(r1) & set(r2) & set(r3)
    if len(common_items) == 1:
        badge_item = common_items.pop()
        priority = caseDetector(badge_item)
        total_priority2 += priority
print(total_priority2)

