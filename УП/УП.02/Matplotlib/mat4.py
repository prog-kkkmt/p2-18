import matplotlib.pyplot as plt

d = {}
with open("data.txt", "r") as f:
    for line in f:
        for c in line:
            if c != ' ' and c != '\n':
                if c not in d:
                    d.update({c: 1})
                else:
                    d[c] += 1

fig, ax = plt.subplots()
plt.bar(d.keys(), d.values())
plt.show()