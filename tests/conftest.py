import pytest
from src.data_utils import charger_masi, nettoyer_masi, calculer_rendements

@pytest.fixture
def df_brut():
    return charger_masi("data/raw/masi_historique.csv")

@pytest.fixture
def df():
    d = nettoyer_masi(charger_masi("data/raw/masi_historique.csv"))
    return calculer_rendements(d)
