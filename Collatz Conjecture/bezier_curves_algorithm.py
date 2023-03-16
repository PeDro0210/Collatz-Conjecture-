import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import math as math


int=0
x=[]
y=[]
xx=[]
yy=[]

for x3 in range(-100,101,1):
    # if x3 < 0:
    #     print("negative")
    #     x3+=1
    # else:
        y2=  x3**3
        y.append(y2)
        x.append(x3)
        xx.append(x3)
        yy.append(y2)
        

        

        
   

print(len(x)/2)

intercep=((len(x)/2))
intercep=math.floor(intercep)
refence_point_one=math.floor(len(x)/7.5)
refence_point_two= math.floor(len(x)/3.75)
reference_point_three=math.floor(len(x)/2)

# After intercep
#each point goes from end to end 
reference_point2_one2=math.floor(len(x)/-7.5)
reference_point2_two2=math.floor(len(x)/-3.75)
reference_point2_three3=math.floor(len(x)/-2)





x=[x[0],
   
   x[refence_point_one]
   
   ,x[refence_point_two]
   
   ,x[reference_point_three]
   

   
   ,x[intercep]
   

   
   ,x[reference_point2_three3]
   
   ,x[reference_point2_two2]
   
   ,x[reference_point2_one2]
   
   ,x[len(x)-1]]
print(x)

y=[y[0]
   ,y[refence_point_one]
   
   ,y[refence_point_two]
   
   ,y[reference_point_three]

   
   ,y[intercep]
   

   ,y[reference_point2_three3]
   
   ,y[reference_point2_two2]
   
   ,y[reference_point2_one2]
   
   ,y[len(y)-1]]
print(y)


verts_list = []
codes_list = []
for i in range(0, len(x) - 1):
    washi=2
    x1, y1 = x[i], y[i]
    x2, y2 = x[i+1], y[i+1]
    x_mid = (x1 + x2) /washi
    y_mid = (y1 + y2) /washi
    verts = np.array([(x1, y1), (x_mid, y1), (x_mid, y2), (x2, y2)], dtype=float)
    codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    verts_list.append(verts)
    codes_list.append(codes)
    print(i)

# Plot Bezier curve patches
fig, ax = plt.subplots()

print("patching the graph")
for verts, codes in zip(verts_list, codes_list):
    path = Path(verts, codes)
    patch = PathPatch(path, facecolor='none', lw=1)
    ax.add_patch(patch)



# Plot data points
ax.plot(x, y, 'ro', markersize=5)
# ax.plot(xx, yy)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title("Function predictions (ONLY CURVES, TRYGONOMETRIC DON'T WORK) ")

plt.show()