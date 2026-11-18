"""Formules GARCH(1,1) utilisees par les tests et le module Odoo."""
import numpy as np

def persistance(alpha, beta):
    return alpha + beta

def est_stationnaire(omega, alpha, beta):
    return omega > 0 and alpha >= 0 and beta >= 0 and (alpha + beta) < 1

def variance_long_terme(omega, alpha, beta):
    """V_L = omega / (1 - alpha - beta)."""
    if (alpha + beta) >= 1:
        raise ValueError("Modele non stationnaire : alpha + beta >= 1")
    return omega / (1 - alpha - beta)

def variance_prevue(h, omega, alpha, beta, sigma2_suivant):
    """E[sigma2_{t+h}] = V_L + (alpha+beta)^(h-1) * (sigma2_{t+1} - V_L)."""
    vl = variance_long_terme(omega, alpha, beta)
    return vl + (alpha + beta) ** (h - 1) * (sigma2_suivant - vl)

def volatilite_cumulee(variances):
    """sigma(h) = sqrt(somme des variances journalieres prevues)."""
    return float(np.sqrt(np.sum(variances)))

def annualiser(vol_jour):
    """Volatilite annualisee = vol_jour * sqrt(252)."""
    return vol_jour * np.sqrt(252)
