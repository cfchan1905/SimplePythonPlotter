import numpy as np
import matplotlib.pyplot as plt

def func2plot_1D(x):
    val = x**2         # exmaple : quadratic 1D plot
    return val

def func2plot_2D(x,y):
#     val = x**2 + yy**2 # exmaple : quadratic 2D plot
#     val = (x**2/(x**2+y**2))*np.sin(np.sqrt(x**2+y**2)*1)**2  # Rabi drive : amplitude versus detuning
    val = (1/(1+y**2))*np.sin(np.sqrt(1+y**2)*x)**2             # Rabi oscillation : time versus detuning
    return val

# set x and y range ; then create meshgrid for 2D plot
lx    = np.linspace(0,2*np.pi,100)
ly    = np.linspace(-3,3,100)
xx,yy = np.meshgrid(lx,ly)

plot_opt = '2D'

if plot_opt == '1D':
    plt.plot(lx,func2plot_1D(lx))
    # Change axes labels
    plt.xlabel('t/(1/$\Omega_R$)',fontsize=16)
    plt.ylabel('$\Delta$/$\Omega_R$',fontsize=16)
elif plot_opt == '2D':
    plt.imshow(
        func2plot_2D(xx,yy),
        extent = [np.min(lx),np.max(lx),np.min(ly),np.max(ly)],
        aspect = 'auto',
    ); plt.colorbar();
    # Change axes labels
    plt.xlabel('t/(1/$\Omega_R$)',fontsize=16);
    plt.ylabel('$\Delta$/$\Omega_R$',fontsize=16)

print("Finnished plotting.")
print("Yeah,oh")