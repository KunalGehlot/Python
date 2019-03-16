step = 0
while(step < 20):
    if(step == 5 or step == 10 or step == 15):
        break
    print(step+1)
    step += 1

for j in range(0, 20):
    if(j == 5 or j == 10 or j == 15):
        continue
    print(j+1)
