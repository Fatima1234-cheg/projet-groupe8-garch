import numpy as np
import pytest
from src.garch_model import (simuler_garch, ajuster_garch,
                             extraire_parametres, prevoir_volatilites)
from src.garch_utils import est_stationnaire

@pytest.fixture(scope="module")
def res():
    return ajuster_garch(simuler_garch(n=3000), dist="normal")

def test_parametres_stationnaires(res):
    p = extraire_parametres(res)
    assert est_stationnaire(p["omega"], p["alpha"], p["beta"])

def test_persistance_proche_du_vrai_modele(res):
    p = extraire_parametres(res)
    # vrai modele : alpha + beta = 0.98
    assert abs(p["alpha"] + p["beta"] - 0.98) < 0.05

def test_volatilites_croissantes_avec_horizon(res):
    v = prevoir_volatilites(res)
    assert 0 < v["vol_1j"] < v["vol_5j"] < v["vol_10j"]

def test_annualisation(res):
    v = prevoir_volatilites(res)
    assert abs(v["vol_annualisee"] - v["vol_1j"] * np.sqrt(252)) < 1e-9
