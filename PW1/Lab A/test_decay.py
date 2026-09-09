"""
Tests for the decay simulation.
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop

def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000

def test_rejects_negative_rate():
    # TODO 1: Check that calling simulate with a negative lam raises a ValueError
    with pytest.raises(ValueError):
        simulate(1000, -0.4)

def test_matches_law():
    # TODO 2: Check that the simulation's AVERAGE over many seeds is close to N0 * exp(-lam * t)
    N0 = 1000
    lam = 0.4
    t = 1.0
    runs = [simulate(N0, lam, t)[-1] for _ in range(100)]
    avg_result = np.mean(runs)
    expected = N0 * np.exp(-lam * t)
    assert avg_result == pytest.approx(expected, rel=0.1)
