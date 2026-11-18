
"""Fonctions de chargement et de nettoyage des donnees MASI."""

import numpy as np
import pandas as pd


def charger_masi(chemin="data/raw/masi_historique.csv"):
    """Charge le CSV et trie par date croissante."""

    df = pd.read_csv(chemin, thousands=",")

    df["Date"] = pd.to_datetime(
        df["Date"],
        format="%m/%d/%Y"
    )

    df = df.sort_values("Date").reset_index(drop=True)

    return df


def nettoyer_masi(df):
    """Supprime Vol., convertit Change %, retire doublons et NaN."""

    df = df.copy()

    if "Vol." in df.columns:
        df = df.drop(columns=["Vol."])

    if "Change %" in df.columns:
        df["Change %"] = (
            df["Change %"]
            .astype(str)
            .str.replace("%", "", regex=False)
            .astype(float)
        )

    df = df.drop_duplicates(subset="Date")
    df = df.dropna(subset=["Date", "Price"])

    return df.sort_values("Date").reset_index(drop=True)



def calculer_rendements(df):
    """Calcule les rendements logarithmiques en pourcentage."""

    df = df.copy()

    df["ret"] = 100 * np.log(
        df["Price"] / df["Price"].shift(1)
    )

    return df.dropna(subset=["ret"]).reset_index(drop=True)



def decouper_train_test(df, ratio=0.8):
    """Decoupage chronologique des donnees."""

    coupure = int(len(df) * ratio)

    train = df.iloc[:coupure].copy()
    test = df.iloc[coupure:].copy()

    return train, test
