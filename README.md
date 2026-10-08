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
