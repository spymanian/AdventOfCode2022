def is_range_contained(range1, range2):
    start1, end1 = map(int, range1.split('-'))
    start2, end2 = map(int, range2.split('-'))
    return start1 <= start2 and end1 >= end2

def count_contained_pairs(assignment_pairs):
    count = 0
    for pair in assignment_pairs:
        range1, range2 = pair.split(',')
        if is_range_contained(range1, range2) or is_range_contained(range2, range1):
            count += 1
    return count

def count_overlapping_pairs(assignments):
    overlap_count = 0

    for pair in assignments:
        range1, range2 = pair.split(',')

        start1, end1 = map(int, range1.split('-'))
        start2, end2 = map(int, range2.split('-'))

        overlap_start = max(start1, start2)
        overlap_end = min(end1, end2)

        if overlap_start <= overlap_end:
            overlap_count += 1

    return overlap_count

with open('overlap.txt', 'r') as file:
    lines = file.readlines()

data = [line.strip() for line in lines]

result = count_contained_pairs(data)
r2 = count_overlapping_pairs(data)

print(result)
print(r2)
