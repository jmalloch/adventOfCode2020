f = open("data.txt", "r")
data = f.read().splitlines()

a1 = a2 = 0
for line in data:
    bt, char, pas = line.split()
    b, t = bt.split('-')
    char = char[0]
    
    a1 += int(b) <= pas.count(char) <= int(t)
    a2 += (pas[int(b)-1] + pas[int(t)-1]).count(char)==1

print(a1,a2)
