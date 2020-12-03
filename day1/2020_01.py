from aocd import data
h=[]
for line in data.splitlines():
        for p in h:
            hE = 2020 - int(line) - p
            if hE in h:
                a2= p*hE*int(line)
        h.append(int(line))
print(a2)
