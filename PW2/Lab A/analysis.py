import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# Part 2: Read data and numerical differentiation
data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]
y = data[:, 1]

v = np.gradient(y, t)
a = np.gradient(v, t)

# Part 3: Noise analysis
mean_a = np.mean(a)
std_a = np.std(a)
print(f"Mean Acceleration: {mean_a:.2f} m/s^2")
print(f"Standard Deviation of Acceleration: {std_a:.2f} m/s^2")

# Part 4: Integrating back
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

max_diff = np.max(np.abs(y - y_rec))
print(f"Max difference between original and recovered position: {max_diff:.4f} m")

# Part 5: Plotting
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 10))

# Position
ax1.plot(t, y, label='Original Position', color='blue')
ax1.set_ylabel('Position (m)')
ax1.set_title('Motion Analysis: Freefall')
ax1.grid(True)
ax1.legend()

# Velocity
ax2.plot(t, v, label='Velocity', color='green')
ax2.set_ylabel('Velocity (m/s)')
ax2.grid(True)
ax2.legend()

# Acceleration
ax3.plot(t, a, label='Acceleration', color='orange', alpha=0.7)
ax3.axhline(-9.81, color='red', linestyle='--', label='Theoretical -9.81 m/s²')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Acceleration (m/s²)')
ax3.grid(True)
ax3.legend()

plt.tight_layout()
plt.savefig('motion.png')
print("Figure successfully saved to motion.png")
