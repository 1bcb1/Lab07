# CC: Brooks Brickley and Hector Hernandez 2019 
import matplotlib.pyplot as plt

name = (input('What is the name of the file you want to open? : ')) + '.csv'

file = open(name, 'r')

data = []
firstline = file.readline()
nextline = file.readline()

while nextline != '':
    data.append(nextline.split(','))
    nextline = file.readline()

time = []
rx = []
ry = []
vx = []
vy = []
ax = []
ay = []

for i in range(len(data)):
    time.append(float(data[i][0])/1000)
    rx.append(float(data[i][1])/100)
    ry.append(float(data[i][2])/100)
    vx.append(float(data[i][3])/100)
    vy.append(float(data[i][4])/100)
    ax.append(float(data[i][5])/100)
    ay.append(float(data[i][6])/100)

ax1 = plt.subplot(3, 2, 1)
ax1.plot(time, rx, 'b')
ax1.set(ylabel='Position (meters)')
ax1.set(xlabel='Time (s)')
ax1.set_title('Position In X Direction')

ax2 = plt.subplot(3, 2, 2)
ax2.plot(time, ry, 'b')
ax2.set(ylabel='Position (meters)')
ax2.set(xlabel='Time (s)')
ax2.set_title('Position In Y Direction')

ax3 = plt.subplot(3, 2, 3)
ax3.plot(time, vx, 'r')
ax3.set(ylabel='Velocity (m/s)')
ax3.set(xlabel='Time (s)')
ax3.set_title('Velocity In X Direction')

ax4 = plt.subplot(3, 2, 4)
ax4.plot(time, vy, 'r')
ax4.set(ylabel='Velocity (m/s)')
ax4.set(xlabel='Time (s)')
ax4.set_title('Velocity In Y Direction')

ax5 = plt.subplot(3, 2, 5)
ax5.plot(time, ax, 'g')
ax5.set(ylabel='Acceleration (m/s\u00B2)')
ax5.set(xlabel='Time (s)')
ax5.set_title('Acceleration In X Direction')

ax6 = plt.subplot(3, 2, 6)
ax6.plot(time, ay, 'g')
ax6.set(ylabel='Acceleration (m/s\u00B2)')
ax6.set(xlabel='Time (s)')
ax6.set_title('Acceleration In Y Direction')

title = input('What do you want the title to be? : ')
plt.suptitle(title)
plt.show()
