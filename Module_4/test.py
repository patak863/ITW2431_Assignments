numberGames = {}
numberGames[(1,2,3)] = 8
numberGames[(2,3)] = 10
numberGames[(1,2)] = 12
sum = 0
for k in numberGames:
    sum += numberGames[k]
print(len(numberGames) + sum)
