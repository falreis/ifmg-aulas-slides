import numpy as np
import matplotlib.pyplot as plt

def plot_funcao(interv, f_, titulo=''):
    plt.rcParams["figure.figsize"] = (10,10)
    plt.rcParams["axes.labelsize"] = 14
    plt.rcParams["axes.titlesize"] = 24

    plt.plot(interv, f_(interv))

    plt.title(titulo)
    plt.grid(); 
    plt.show()

def plot_grafico(values, scores, mark='x'):
    plt.rcParams["figure.figsize"] = (10,10)
    plt.plot(values, scores, mark)

    plt.rcParams["axes.titlesize"] = 24
    
    if(len(values) < 500):
        plt.grid()
        
    plt.show()

def plot_cities(x, y):
    plt.rcParams["figure.figsize"] = (10,10)
    plt.plot(x, y, 'or', markersize=12)
    plt.rcParams["axes.titlesize"] = 24
    plt.show()

def plot_3d(f_, x=None, y=None, interval=0, type='surface'):
    if(interval>0):
        x = np.linspace(-interval, interval, 100)
        y = np.linspace(-interval, interval, 100)

    if(type == 'scatter' and interval<=0):
        xx = x
        yy = y
    else:
        xx, yy = np.meshgrid(x, y)

    zz = f_(xx, yy)

    plt.rcParams["figure.figsize"] = (15,15)
    fig = plt.figure()
    
    ax = plt.axes(projection ='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    if(type == 'contour'):
        ax.contour3D(xx, yy, zz)
    elif(type == 'wireframe'):
        ax.plot_wireframe(xx, yy, zz)
    elif(type == 'scatter'):
        if(interval>0):
            ax.scatter(xx, yy, zz)
        else:
            aran = np.arange(0,len(xx),1)
            img = ax.scatter(xx, yy, zz, c=aran)
            fig.colorbar(img)
    else:
        ax.plot_surface(xx, yy, zz)
    plt.show()
        
#Fonte: https://github.com/chncyhn/simulated-annealing-tsp

def plotTSP(paths, coords, num_iters=1):
    x = []; y = []
    for i in paths[0]:
        x.append(coords[i][0])
        y.append(coords[i][1])

    plt.plot(x, y, 'co')

    # Set a scale for the arrow heads (there should be a reasonable default for this, WTF?)
    a_scale = float(max(x))/float(100)

    # Draw the older paths, if provided
    if num_iters > 1:

        for i in range(1, num_iters):

            # Transform the old paths into a list of coordinates
            xi = []; yi = [];
            for j in paths[i]:
                xi.append(coords[j][0])
                yi.append(coords[j][1])

            plt.arrow(xi[-1], yi[-1], (xi[0] - xi[-1]), (yi[0] - yi[-1]),
                    head_width = a_scale, color = 'r',
                    length_includes_head = True, ls = 'dashed',
                    width = 0.001/float(num_iters))
            for i in range(0, len(x) - 1):
                plt.arrow(xi[i], yi[i], (xi[i+1] - xi[i]), (yi[i+1] - yi[i]),
                        head_width = a_scale, color = 'r', length_includes_head = True,
                        ls = 'dashed', width = 0.001/float(num_iters))

    # Draw the primary path for the TSP problem
    plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width = a_scale,
            color ='g', length_includes_head=True)
    
    for i in range(0,len(x)-1):
        plt.arrow(x[i], y[i], (x[i+1] - x[i]), (y[i+1] - y[i]), head_width = a_scale,
                color = 'g', length_includes_head = True)

    #Set axis too slitghtly larger than the set of x and y
    plt.xlim(min(x)*1.1, max(x)*1.1)
    plt.ylim(min(y)*1.1, max(y)*1.1)
    plt.show()