import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

strikes = np.linspace(0.6, 1.4, 30)
maturities = np.linspace(0.1, 2.0, 30)
S, T = np.meshgrid(strikes, maturities)

vol = 0.2 + 0.1 * np.sqrt(T) + 0.15 * (5 - 1)**2 / (1 + 5*T)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(S, T, vol, cmap='viridis', edgecolor='none', alpha=0.9)

ax.set_xlabel("Strike Price")
ax.set_ylabel("Maturity(Years)")
ax.set_zlabel("Implied Volatility")
ax.set_title("Volatility Surface")

fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)
plt.show()