# Projet 8 — Prévision de la volatilité du MASI/MADEX

**Module :** Finance des Marchés et ERP  
**Formation :** Cycle Ingénieur Informatique Décisionnelle et IA  
**Établissement :** ENSA Safi — Université Cadi Ayyad Marrakech  
**Encadrant :** Pr. Abdelilah JRAIFI  
**Année universitaire :** 2026–2027

---

##  Équipe — Groupe 8

- CHIGUER Touria
- BOUZARMIN Siham
- EL HOUMA Chayma
- CHEGDANI Fatima

---

##  Objectif du projet

L'objectif est de **prévoir la volatilité de l'indice MASI/MADEX** de la Bourse de Casablanca à l'aide d'un modèle **GARCH(1,1)**.

Les prévisions seront réalisées à **1, 5 et 10 jours**, puis intégrées dans **Odoo 17** sous forme de jauge.

Une comparaison avec un modèle **LSTM** permettra également d'étudier la réactivité des deux approches face aux chocs du marché.

---

##  Approche

Le projet est organisé autour de cinq axes :

1. **Théorie** — étude de la volatilité et du modèle GARCH.
2. **Données** — collecte et préparation des données du MASI/MADEX.
3. **Modélisation Python** — estimation et prévision avec GARCH.
4. **Intégration Odoo** — affichage des résultats dans Odoo 17.
5. **IA** — comparaison entre GARCH et LSTM.

---

##  Technologies

- **Python**
- **Pandas / NumPy**
- **SciPy**
- **Matplotlib**
- **Scikit-learn**
- **ARCH**
- **TensorFlow / Keras**
- **Odoo 17**
- **PostgreSQL**
- **Docker**
- **Git / GitHub**

---

##  Structure du projet

```text
projet-groupe8/
├── README.md
├── docs/
├── notebooks/
├── src/
├── tests/
├── odoo_addons/
├── docker-compose.yml
└── requirements.txt
```

---

##  Résultats attendus

Le projet doit permettre de :

- Estimer la volatilité du MASI/MADEX avec **GARCH(1,1)**.
- Prévoir la volatilité à **1, 5 et 10 jours**.
- Visualiser les prévisions dans **Odoo 17**.
- Développer une approche **LSTM**.
- Comparer **GARCH et LSTM** face aux différents mouvements du marché.

---

## Avancement

- [x] Création du dépôt GitHub
- [ ] Préparation des données
- [ ] Modèle GARCH
- [ ] Intégration Odoo
- [ ] Modèle LSTM
- [ ] Comparaison GARCH / LSTM
- [ ] Tests et validation
- [ ] Rapport final
- [ ] Soutenance

---

## 📄 Documentation

Les documents du projet sont disponibles dans le dossier `docs/`.

```text
docs/
├── fiche_lecture.pdf
├── gantt_previsionnel.png
├── gantt_realise.png
└── rapport.pdf
```

---

## 📌 Contexte

Projet réalisé dans le cadre du module **Finance des Marchés et ERP** — ENSA Safi, année universitaire **2026–2027**.

**Groupe 8 — Projet GARCH MASI/MADEX**