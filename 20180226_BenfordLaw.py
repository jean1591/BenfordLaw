import matplotlib.pyplot as plt

"""
Benford Law:
The law states that in many naturally occurring collections of numbers, the leading significant digit is likely to be small.
"""

def create_law():
    tab = {}

    for row in range(2, 100):
        tab.setdefault(row, [])
        for col in range(1, 100):
            print(str(row) + "\t" + str(col))
            tab[row].append(row ** col)

    return tab

test = create_law()

result = {}

for element in range(1, 10):
    result.setdefault(element, 0)

for lst in test.values():
    for element in lst:
        first = int(str(element)[0])
        result[first] += 1


plt.plot(list(result.values()))
plt.ylabel("Nr of appearances")
plt.xlabel("First digit")
plt.show()
