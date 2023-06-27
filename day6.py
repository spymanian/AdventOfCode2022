inputFile = open("go.txt", "r")

inputValues = inputFile.read()

#for letter in range(len(inputValues)):
    # string[ start_index_pos: end_index_pos: step_size]
   # marker = inputValues[letter : letter + 4]
    #if len(set(marker)) == len(marker):
     #   print(letter + 4)
     #   break
      
for letter in range(len(inputValues)):
    # string[ start_index_pos: end_index_pos: step_size]
    marker = inputValues[letter : letter + 14]
    if len(set(marker)) == len(marker):
        print(letter + 14)
        break