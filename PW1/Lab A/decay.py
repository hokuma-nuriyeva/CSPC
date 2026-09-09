import numpy as np

def simulate(N0, lam, t=1.0):
    if lam < 0:
        raise ValueError("Rate lambda cannot be negative")
    p = np.exp(-lam * t)
    return [N0, np.random.binomial(N0, p)]

def simulate_loop(N0, lam, t=1.0):
    if lam < 0:
        raise ValueError("Rate lambda cannot be negative")
    p = np.exp(-lam * t)
    count = 0
    for _ in range(N0):
        if np.random.rand() < p:
            count += 1
    return [N0, count]
