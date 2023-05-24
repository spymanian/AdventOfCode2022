with open('cal.txt') as f:
    lines = f.read().split('\n')
    arr = []
    add = 0;
    
    ##print(lines)
    for i in lines:
      ##print(i)
      if(i != ''):
        add += int(i);

      if(i == ''):
        arr.append(add)
        add = 0

    arr.append(add)
  
    sortedArr = sorted(arr)
    print(sortedArr[-1])
    top3 = sum(sortedArr[-3:])
    print(top3)
    
    





    




