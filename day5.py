with open('input.txt') as file:
    lines = file.read().splitlines()

rearrange = [[0]]
finished = False
for line in lines:
    if not line:
        continue
    if not finished and line[1] != '1':
        n = len(line)
        for i in range(1, n, 4):
            f = i // 4 + 1
            if len(rearrange) <= f:
                rearrange.append([line[i]])
            else:
                rearrange[f].append(line[i])
    elif not finished and line[1] == '1':
        finished = True
        for i, stack in enumerate(rearrange):
            stack = stack[::-1]
            rearrange[i] = stack
            while rearrange[i] and rearrange[i][-1] == ' ':
                rearrange[i].pop()
    else:
        step = line.split()
        a, b, c = map(int, [step[1], step[3], step[5]])
        for _ in range(a):
          x = rearrange[b].pop()
          rearrange[c].append(x)
        # Part 2
        #y = rearrange[b][-a:]
        #rearrange[b] = rearrange[b][:-a]
        #rearrange[c].extend(y)

rearrange = rearrange[1:]
ans = ''
for stack in rearrange:
    ans += stack.pop()
print(ans)