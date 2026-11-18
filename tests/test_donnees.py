import numpy as np
from src.data_utils import decouper_train_test, nettoyer_masi, calculer_rendements

def test_dates_croissantes(df):
    assert df["Date"].is_monotonic_increasing

def test_pas_de_doublons(df):
    assert not df["Date"].duplicated().any()

def test_prix_positifs(df):
    assert (df["Price"] > 0).all()

def test_rendements_finis(df):
    assert np.isfinite(df["ret"]).all()

def test_pas_de_nan(df):
    assert not df[["Date", "Price", "ret"]].isna().any().any()

def test_colonne_vol_supprimee(df):
    assert "Vol." not in df.columns

def test_profondeur_historique(df):
    # 250 = un an minimum. Avec 4 ans ou plus de donnees, mettez 1000.
    assert len(df) >= 250

def test_rendement_premier_jour(df_brut):
    p0, p1 = df_brut["Price"].iloc[0], df_brut["Price"].iloc[1]
    attendu = 100 * np.log(p1 / p0)
    d = calculer_rendements(nettoyer_masi(df_brut))
    assert abs(d["ret"].iloc[0] - attendu) < 1e-9

def test_split_chronologique(df):
    train, test = decouper_train_test(df, 0.8)
    assert train["Date"].max() < test["Date"].min()
    assert len(train) + len(test) == len(df)
