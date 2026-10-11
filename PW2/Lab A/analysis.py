import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# ==========================================
# Part 2, 3, 4: Freefall (1D) Analysis
# ==========================================
data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]
y = data[:, 1]

v = np.gradient(y, t)
a = np.gradient(v, t)

# Print metrics
mean_a = np.mean(a)
std_a = np.std(a)
print(f"--- 1D Freefall Analysis ---")
print(f"Mean Acceleration: {mean_a:.2f} m/s^2")
print(f"Standard Deviation of Acceleration: {std_a:.2f} m/s^2")

# Integration back
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]
max_diff = np.max(np.abs(y - y_rec))
print(f"Max position reconstruction error: {max_diff:.4f} m\n")

# Plot Motion (1D)
fig1, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 10))

ax1.plot(t, y, label='Original Position', color='blue')
ax1.set_ylabel('Position (m)')
ax1.set_title('1D Motion Analysis: Freefall')
ax1.grid(True)
ax1.legend()

ax2.plot(t, v, label='Velocity', color='green')
ax2.set_ylabel('Velocity (m/s)')
ax2.grid(True)
ax2.legend()

ax3.plot(t, a, label='Acceleration', color='orange', alpha=0.7)
ax3.axhline(-9.81, color='red', linestyle='--', label='Theoretical -9.81 m/s²')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Acceleration (m/s²)')
ax3.grid(True)
ax3.legend()

plt.tight_layout()
fig1.savefig('motion.png')
print("Saved 1D plot to motion.png")

# ==========================================
# Bonus Part: 2D Trajectory Analysis
# ==========================================
traj_data = np.loadtxt('trajectory.csv', delimiter=',', skiprows=1)
t_2d = traj_data[:, 0]
x_2d = traj_data[:, 1]
y_2d = traj_data[:, 2]

# Compute velocities in both dimensions
vx = np.gradient(x_2d, t_2d)
vy = np.gradient(y_2d, t_2d)
speed = np.sqrt(vx**2 + vy**2)

# Plot 2D Trajectory and Speed
fig2, (ax_traj, ax_speed) = plt.subplots(1, 2, figsize=(12, 5))

# 2D Path (x vs y)
ax_traj.plot(x_2d, y_2d, color='purple', label='Path')
ax_traj.set_xlabel('X (m)')
ax_traj.set_ylabel('Y (m)')
ax_traj.set_title('2D Trajectory (X vs Y)')
ax_traj.grid(True)
ax_traj.legend()

# Speed over time
ax_speed.plot(t_2d, speed, color='crimson', label=r'Speed $\sqrt{v_x^2 + v_y^2}$')
ax_speed.set_xlabel('Time (s)')
ax_speed.set_ylabel('Speed (m/s)')
ax_speed.set_title('Speed over Time')
ax_speed.grid(True)
ax_speed.legend()

plt.tight_layout()
fig2.savefig('trajectory.png')
print("Saved 2D plot to trajectory.png")
