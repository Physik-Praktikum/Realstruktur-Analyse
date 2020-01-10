import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0,1,100)


fig = plt.figure()
ax1 = fig.add_subplot(122,projection="3d")
ax2 = fig.add_subplot(121,projection="3d")

ax1.plot(x,0*x,0*x,linewidth=5,color="black")
ax1.plot(x,np.ones_like(x),0*x,linewidth=5,color="black")
ax1.plot(0*x,x,0*x,linewidth=5,color="black")
ax1.plot(np.ones_like(x),x,0*x,linewidth=5,color="black")

ax1.plot(x,0*x,np.ones_like(x),linewidth=5,color="black")
ax1.plot(x,np.ones_like(x),np.ones_like(x),linewidth=5,color="black")
ax1.plot(0*x,x,np.ones_like(x),linewidth=5,color="black")
ax1.plot(np.ones_like(x),x,np.ones_like(x),linewidth=5,color="black")

ax1.plot(0*x,0*x,x,linewidth=5,color="black")
ax1.plot(np.ones_like(x),0*x,x,linewidth=5,color="black")
ax1.plot(0*x,np.ones_like(x),x,linewidth=5,color="black")
ax1.plot(np.ones_like(x),np.ones_like(x),x,linewidth=5,color="black")

ax1.plot(x,x,x,color="black")
ax1.plot(x,-x+np.ones_like(x),-x+np.ones_like(x),color="black")
ax1.plot(x,x,-x+np.ones_like(x),color="black")
ax1.plot(x,-x+np.ones_like(x),x,color="black")


ax1.plot([0],[0],[0],"o",markersize=20,color="red")
ax1.plot([0],[0],[1],"o",markersize=20,color="red")
ax1.plot([0],[1],[0],"o",markersize=20,color="red")
ax1.plot([0],[1],[1],"o",markersize=20,color="red")
ax1.plot([1],[0],[0],"o",markersize=20,color="red")
ax1.plot([1],[0],[1],"o",markersize=20,color="red")
ax1.plot([1],[1],[0],"o",markersize=20,color="red")
ax1.plot([1],[1],[1],"o",markersize=20,color="red")
ax1.plot([0.5],[0.5],[0.5],"o",markersize=20,color="red")
ax1.axis("scaled")
ax1.set_title(r"bcc-Gitter des $\beta$-Messings",fontsize=20)

ax2.plot(x,0*x,0*x,linewidth=5,color="black")
ax2.plot(x,np.ones_like(x),0*x,linewidth=5,color="black")
ax2.plot(0*x,x,0*x,linewidth=5,color="black")
ax2.plot(np.ones_like(x),x,0*x,linewidth=5,color="black")

ax2.plot(x,0*x,np.ones_like(x),linewidth=5,color="black")
ax2.plot(x,np.ones_like(x),np.ones_like(x),linewidth=5,color="black")
ax2.plot(0*x,x,np.ones_like(x),linewidth=5,color="black")
ax2.plot(np.ones_like(x),x,np.ones_like(x),linewidth=5,color="black")

ax2.plot(0*x,0*x,x,linewidth=5,color="black")
ax2.plot(np.ones_like(x),0*x,x,linewidth=5,color="black")
ax2.plot(0*x,np.ones_like(x),x,linewidth=5,color="black")
ax2.plot(np.ones_like(x),np.ones_like(x),x,linewidth=5,color="black")

ax2.plot(x,x,0*x,color="black")
ax2.plot(-x + np.ones_like(x),x,0*x,color="black")
ax2.plot(x,x,np.ones_like(x),color="black")
ax2.plot(-x + np.ones_like(x),x,np.ones_like(x),color="black")
ax2.plot(0*x,x,x,color="black")
ax2.plot(0*x,x,-x+np.ones_like(x),color="black")
ax2.plot(np.ones_like(x),x,x,color="black")
ax2.plot(np.ones_like(x),x,-x+np.ones_like(x),color="black")
ax2.plot(x,0*x,x,color="black")
ax2.plot(x,0*x,-x + np.ones_like(x),color="black")
ax2.plot(x,np.ones_like(x),x,color="black")
ax2.plot(x,np.ones_like(x),-x + np.ones_like(x),color="black")

ax2.plot([0],[0],[0],"o",markersize=20,color="red")
ax2.plot([0],[0],[1],"o",markersize=20,color="red")
ax2.plot([0],[1],[0],"o",markersize=20,color="red")
ax2.plot([0],[1],[1],"o",markersize=20,color="red")
ax2.plot([1],[0],[0],"o",markersize=20,color="red")
ax2.plot([1],[0],[1],"o",markersize=20,color="red")
ax2.plot([1],[1],[0],"o",markersize=20,color="red")
ax2.plot([1],[1],[1],"o",markersize=20,color="red")
ax2.plot([0.5],[0],[0.5],"o",markersize=20,color="red")
ax2.plot([0.5],[1],[0.5],"o",markersize=20,color="red")
ax2.plot([0],[0.5],[0.5],"o",markersize=20,color="red")
ax2.plot([1],[0.5],[0.5],"o",markersize=20,color="red")
ax2.plot([0.5],[0.5],[0],"o",markersize=20,color="red")
ax2.plot([0.5],[0.5],[1],"o",markersize=20,color="red")
ax2.set_title(r"fcc-Gitter des $\alpha$-Messings",fontsize=20)
ax2.axis("scaled")
plt.show()
