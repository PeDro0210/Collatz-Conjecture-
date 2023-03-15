import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from matplotlib.path import Path
from matplotlib.patches import PathPatch

#global variables

x=[]
y=[]
def collatz_variant(num, power):
        intermediate_nums = []
        
        while num != 1:
            if num in intermediate_nums:
                break
            intermediate_nums.append(num)
            if num % 2 == 0:
                num2 = num // 2
                x.append(num)
                y.append(num2)
                num = num2
            else:
                num1 = (num * 3 * power) + power
                x.append(num)
                y.append(num1)
                num = num1

while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Enter a valid integer.")
            
for i in range(1, 100):
    power = 2**i
    result = collatz_variant(num, power)

x=np.array(x, dtype=float)
y=np.array(y, dtype=float)

print(x.dtype)
print(y.dtype)

# Create Bezier curve paths between the points
verts_list = []
codes_list = []

for i in range(0, len(x) - 1):
    x1, y1 = x[i], y[i]
    x2, y2 = x[i+1], y[i+1]
    x_mid = (x1 + x2) / 2
    y_mid = (y1 + y2) / 2
    verts = np.array([(x1, y1), (x_mid, y1), (x_mid, y2), (x2, y2)], dtype=float)
    codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    verts_list.append(verts)
    codes_list.append(codes)

# Plot Bezier curve patches
fig, ax = plt.subplots()

for verts, codes in zip(verts_list, codes_list):
    path = Path(verts, codes)
    patch = PathPatch(path, facecolor='none', lw=2)
    ax.add_patch(patch)

# Plot data points
ax.plot(x, y, 'ro', markersize=5)

ax.set_xlabel('Transformed Number')
ax.set_ylabel('Result Number by the Function')
ax.set_title('Collatz Conjecture with all the powers of 2 in a range from 1 to 100')

plt.show()
