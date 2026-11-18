# Formules du modele GARCH(1,1)

## 1. Rendements logarithmiques

$$r_t = 100 \times \ln\left(\frac{S_t}{S_{t-1}}\right)$$

(en %, pour faciliter la convergence de l'optimiseur).

Modele de moyenne constante :

$$r_t = \mu + \varepsilon_t, \qquad \varepsilon_t = \sigma_t z_t, \qquad z_t \sim i.i.d.(0,1)$$

## 2. Equation GARCH(1,1)

$$\sigma_t^2 = \omega + \alpha\,\varepsilon_{t-1}^2 + \beta\,\sigma_{t-1}^2$$

- $\omega > 0$ : constante ;
- $\alpha \ge 0$ : reactivite aux chocs recents ;
- $\beta \ge 0$ : persistance de la volatilite passee.

Le clustering de volatilite se traduit par une autocorrelation de $r_t^2$ ;
il est teste par le test d'Engle (ARCH-LM).

## 3. Stationnarite

$$\alpha + \beta < 1$$

La quantite $\alpha+\beta$ mesure la persistance : proche de 1, les chocs
de volatilite se dissipent lentement.

## 4. Variance de long terme

$$V_L = \frac{\omega}{1-\alpha-\beta}$$

Niveau vers lequel la variance conditionnelle revient a long terme.

## 5. Prevision a h jours

$$E[\sigma_{t+h}^2] = V_L + (\alpha+\beta)^{h-1}\left(\sigma_{t+1}^2 - V_L\right)$$

## 6. Volatilite cumulee sur h jours

$$\sigma(h) = \sqrt{\sum_{k=1}^{h} E[\sigma_{t+k}^2]}$$

Utilisee pour les horizons 1, 5 et 10 jours.

## 7. Annualisation

$$\sigma_{ann} = \sigma_{jour} \times \sqrt{252}$$

(252 jours de bourse par an).

## 8. Estimation par maximum de vraisemblance

Les parametres $\theta = (\mu,\omega,\alpha,\beta)$ maximisent la log-vraisemblance.

Innovations Normales :

$$\ell(\theta) = -\frac{1}{2}\sum_{t=1}^{T}\left[\ln(2\pi) + \ln\sigma_t^2 + \frac{\varepsilon_t^2}{\sigma_t^2}\right]$$

Innovations Student-t ($\nu > 2$ degres de liberte) :

$$\ell(\theta,\nu) = \sum_{t=1}^{T}\Big[\ln\Gamma\!\left(\tfrac{\nu+1}{2}\right) - \ln\Gamma\!\left(\tfrac{\nu}{2}\right) - \tfrac{1}{2}\ln\big(\pi(\nu-2)\big) - \tfrac{1}{2}\ln\sigma_t^2 - \tfrac{\nu+1}{2}\ln\!\left(1+\frac{\varepsilon_t^2}{(\nu-2)\sigma_t^2}\right)\Big]$$

La loi de Student est preferee si les rendements ont des queues epaisses
(kurtosis eleve, rejet de Jarque-Bera).

## 9. Hypotheses

- Moyenne quasi constante, variance conditionnelle dependant du passe.
- Processus stationnaire, parametres constants sur la fenetre d'estimation.
- La volatilite realisee n'etant pas observable, on utilise le proxy $r_t^2$
  (ou la volatilite glissante sur 5 jours).