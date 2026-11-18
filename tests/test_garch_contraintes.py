import numpy as np
import pytest
from src.garch_utils import (persistance, est_stationnaire, variance_long_terme,
                             variance_prevue, volatilite_cumulee, annualiser)

def test_variance_long_terme():
    assert abs(variance_long_terme(0.1, 0.1, 0.8) - 1.0) < 1e-9

def test_persistance():
    assert abs(persistance(0.1, 0.8) - 0.9) < 1e-12

def test_stationnarite():
    assert est_stationnaire(0.1, 0.1, 0.8)
    assert not est_stationnaire(0.1, 0.2, 0.8)   # alpha + beta = 1
    assert not est_stationnaire(-0.1, 0.1, 0.8)  # omega <= 0

def test_non_stationnaire_leve_erreur():
    with pytest.raises(ValueError):
        variance_long_terme(0.1, 0.5, 0.6)

def test_prevision_horizon_1():
    assert abs(variance_prevue(1, 0.1, 0.1, 0.8, 2.5) - 2.5) < 1e-12

def test_prevision_converge_vers_long_terme():
    v = variance_prevue(500, 0.1, 0.1, 0.8, 5.0)
    assert abs(v - 1.0) < 1e-6

def test_volatilite_cumulee():
    assert abs(volatilite_cumulee([1, 1, 1, 1]) - 2.0) < 1e-12

def test_annualisation():
    assert abs(annualiser(1.0) - np.sqrt(252)) < 1e-12
