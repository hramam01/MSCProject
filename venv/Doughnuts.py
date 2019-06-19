import matplotlib.pyplot as plt

# Make data: I have 3 groups and 7 subgroups
layer1names = ['Integration', ' ']
layer1 = [88, 12]
layer2names = ['Security', '']
layer2 = [50, 50]
layer3names = ['Functional', '']
layer3 = [80, 20]
layer4names = ['Data', '']
layer4 = [90, 10]

# Create colors
a, b, c, d = [plt.cm.Reds, plt.cm.Blues, plt.cm.Greys, plt.cm.Greens]

# First Ring (outside)
fig, ax = plt.subplots()
ax.axis('equal')

plt.style.use('dark_background')
mypie, _ = ax.pie(layer1, radius=2, labels=layer1names, colors=['white', a(0.3)], startangle=90)
plt.setp(mypie, width=0.5)

# Second Ring (Inside)
mypie2, _ = ax.pie(layer2, radius=1.5, labels=layer2names, labeldistance=-.7, colors=['white', b(.6)], startangle=90)
plt.setp(mypie2, width=0.5)
plt.margins(0, 0)

# Third Ring (Inside)
mypie3, _ = ax.pie(layer3, radius=1, labels=layer3names, labeldistance=0.6, colors=['white', c(0.4)], startangle=90)
plt.setp(mypie2, width=0.5)
plt.margins(0, 0)

# Fourth Ring (Inside)
mypie4, _ = ax.pie(layer4, radius=.5, labels=layer4names, labeldistance=0.5, colors=['white', d(0.65)], startangle=90)
plt.setp(mypie2, width=0.5)
plt.margins(0, 0)
# show it

plt.show()

