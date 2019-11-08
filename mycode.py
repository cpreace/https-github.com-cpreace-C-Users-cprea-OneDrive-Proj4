x = 0
with open('zoneCheck', 'r') as f1, open('zonecpy_a', 'w') as f2:
    for line in f1:
        f2.write(str(x)+": "+line)
        x = x+1


