import matplotlib.pyplot as plt

year = [1950, 1951, 1952]
pop = [3.032, 3.682, 4.440]


plt.plot(year, pop)

plt.xlabel('Year')     # X and Y labels
plt.ylabel('Population')

plt.title('This is a title')  # Title

plt.yticks([0, 2, 4, 6, 8, 10],
           ['0', '2B', '4B', '6B', '8B', '10B'])

plt.show()