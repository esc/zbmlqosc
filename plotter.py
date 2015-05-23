from matplotlib import pyplot as plt
import matplotlib.animation as animation
import bcolz

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    b = bcolz.open('db')
    xar = [j[0] for j in b[-10:]]
    yar = [j[1] for j in b[-10:]]
    ax1.clear()
    ax1.plot(xar, yar)
    print(yar, xar)

ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()
