# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
    conda env create -f PW<n>/Lab<X>/environment.yml
    conda activate cspc

---

## PW1 --- Lab A: Reproducible Foundations

**What I built:**
- Radioactive decay simulation with NumPy and pure-Python loop implementations, along with pytest test suites.

**Speed comparison (loop vs NumPy):**
- loop : 0.0849 s
- numpy : 0.0000 s
- speed-up: 2053.28 x faster

**Tests:** all passing? yes

**Conclusion:**
- Successfully configured a reproducible Conda environment and Git repository. Built tests to verify physical decay laws and optimized performance using NumPy vectorization.

---

## PW1 --- Lab B: Data, Plotting, and Automation

**What I built:**
- Data analysis script (`plot.py`) comparing observed decay data against the analytical model $N_0 e^{-\lambda t}$.
- Automated build pipeline using Snakemake.

**Data & Model Agreement:**
- The observed data points closely match the exponential analytical curve with $\lambda = 0.3$.

**Snakemake Pipeline:**
- Automatically tracks timestamps of inputs (`decay_observed.csv`, `plot.py`) and rebuilds `figure.png` only when source files change.

---

## PW2 --- Lab A: Motion from Tracking Data

**Results:**
- Mean Acceleration: ~ -8.58 m/s² (close to theoretical -9.81 m/s²).
- Standard deviation of acceleration is high due to noise amplification.

**Why Acceleration is Noisy:**
- Numerical differentiation calculates small differences between neighboring points, which greatly magnifies random measurement noise present in the raw position data.

**Integrating Back:**
- Integrating noisy acceleration back to velocity and position suppresses the noise because integration accumulates values and sums random errors, effectively averaging them out.
- The recovered position matches the original position within less than a meter.

---

## PW2 --- Lab A: Motion from Tracking Data

**Results & Analysis:**
- Mean Acceleration: ~ -8.58 m/s² (closely matching theoretical $g \approx -9.81$ m/s²).
- Standard deviation of acceleration is high due to noise amplification.

**Why Acceleration is Noisy:**
- Numerical differentiation compares nearby position measurements, which greatly magnifies random noise. Differentiating twice (from position to acceleration) severely amplifies measurement errors.

**Integrating Back:**
- Integration suppresses noise because it accumulates values step-by-step, naturally canceling out random errors. The reconstructed position matched the original data within less than a meter.

**Bonus (2D Trajectory):**
- Analyzed 2D plane motion from `trajectory.csv` using $v_x = \frac{dx}{dt}$ and $v_y = \frac{dy}{dt}$.
- Computed total speed $s = \sqrt{v_x^2 + v_y^2}$ over time and plotted the spatial trajectory.
