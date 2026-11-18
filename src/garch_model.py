"""Estimation et prevision GARCH(1,1) avec la librairie arch."""
import numpy as np
from arch import arch_model

def simuler_garch(n=3000, omega=0.05, alpha=0.08, beta=0.90, seed=42):
    """Simule des rendements GARCH(1,1) (pour tester sans donnees reelles)."""
    rng = np.random.default_rng(seed)
    r = np.zeros(n)
    s2 = omega / (1 - alpha - beta)
    for t in range(n):
        r[t] = np.sqrt(s2) * rng.standard_normal()
        s2 = omega + alpha * r[t] ** 2 + beta * s2
    return r

def ajuster_garch(rendements, dist="t"):
    """Ajuste un GARCH(1,1) a moyenne constante. Rendements en %."""
    am = arch_model(rendements, mean="Constant", vol="GARCH", p=1, q=1, dist=dist)
    return am.fit(disp="off")

def extraire_parametres(res):
    """Retourne mu, omega, alpha, beta sous forme de dictionnaire."""
    p = res.params
    return {"mu": float(p["mu"]), "omega": float(p["omega"]),
            "alpha": float(p["alpha[1]"]), "beta": float(p["beta[1]"])}

def prevoir_volatilites(res, horizon=10):
    """Volatilites prevues a 1, 5 et 10 jours + annualisee (en %)."""
    var_h = res.forecast(horizon=horizon).variance.iloc[-1].values
    return {"vol_1j": float(np.sqrt(var_h[0])),
            "vol_5j": float(np.sqrt(var_h[:5].sum())),
            "vol_10j": float(np.sqrt(var_h[:10].sum())),
            "vol_annualisee": float(np.sqrt(var_h[0] * 252))}
