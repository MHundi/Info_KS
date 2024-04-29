import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter

# Defintionsmenge und Funktion
# ----------------------------
a= -0.1 # untere x-Intervallgrenze 
b= 5.1 # obere x-Intervallgrenze
c = -5.1# untere y-Intervallgrenze
d = 0.1 # obere y-Intervallgrenze
#x = np.linspace(a, b,1000)
#y1= x**3-x**2-x+1
# ----------------------------

# Einstellung des Graphen
fig=plt.figure(figsize=(4,4))
ax= fig.add_subplot(1,1,1, aspect =1)

# Definiton der Haupteinheiten, reele Zahlen ohne die 0 
def major_tick(x, pos):
    if x==0:
        return ""
    return int(x)

# Achsenskalierung
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(AutoMinorLocator(20))
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_minor_locator(AutoMinorLocator(20))
ax.xaxis.set_major_formatter(FuncFormatter(major_tick))
ax.yaxis.set_major_formatter(FuncFormatter(major_tick))

# Position der Achsen im Schaubild
ax.spines[['top','right']].set_visible(False)
ax.spines[['bottom','left']].set_position('zero')

# Pfeile für die Achsen
ax.plot((1),(0), ls="", marker= ">", ms=7, color="k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot((0),(0), ls="", marker= "v", ms=7, color="k", transform=ax.get_xaxis_transform(), clip_on=False)

# Achsenlänge und Beschriftung
ax.set_xlim(a,b)
ax.set_ylim(c, d)
#ax.set_xlabel("x", loc="right")
#ax.set_ylabel("y", loc="bottom", rotation=0)

# Kästchen
ax.grid(linestyle="-", which="major",linewidth=0.7, zorder=-10)
ax.grid(linestyle="-", which="minor",linewidth=0.5, zorder=-10)

plt.text(1, 0.1, "1", fontdict=None,horizontalalignment='center', fontsize = 12)
plt.text(2, 0.1, "2", fontdict=None,horizontalalignment='center',fontsize = 12)
plt.text(3, 0.1, "3", fontdict=None,horizontalalignment='center',fontsize = 12)
plt.text(4, 0.1, "4", fontdict=None,horizontalalignment='center',fontsize = 12)
plt.text(5, 0.1, "x", fontdict=None,horizontalalignment='center',fontsize = 12)


plt.text(-0.4, -1, "1", fontdict=None,verticalalignment='center',fontsize = 12)
plt.text(-0.4, -2, "2", fontdict=None,verticalalignment='center',fontsize = 12)
plt.text(-0.4, -3, "3", fontdict=None,verticalalignment='center',fontsize = 12)
plt.text(-0.4, -4, "4", fontdict=None,verticalalignment='center',fontsize = 12)
plt.text(-0.4, -5, "y", fontdict=None,verticalalignment='center',fontsize = 12)

# Plot der Funktion
#ax.plot(x,y1, zorder=10)
#ax.plot(np.e, 1/np.e, "bo") #Punkt einzeichnen
plt.show()