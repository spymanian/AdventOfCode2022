with open('rps.txt') as rps:
  #Part1 and Part2
  map = {
    "A X\n": 4,
    "A Y\n": 8,
    "A Z\n": 3,
    "B X\n": 1,
    "B Y\n": 5,
    "B Z\n": 9,
    "C X\n": 7,
    "C Y\n": 2,
    "C Z\n": 6
  }
  map2 = {
    "A X\n": 3,
    "A Y\n": 4,
    "A Z\n": 8,
    "B X\n": 1,
    "B Y\n": 5,
    "B Z\n": 9,
    "C X\n": 2,
    "C Y\n": 6,
    "C Z\n": 7
  }
  count = 0
  count2 = 0
  for i in rps:
    count += map[i]
    count2 += map2[i]
  print(count)
  print(count2)
    

