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