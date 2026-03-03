# ⚽ PL Scouting Tool

> ML-powered player profiling for the Premier League — unsupervised archetype discovery + supervised classification, deployed as a Streamlit web app.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4+-orange?style=flat-square&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red?style=flat-square&logo=streamlit)
![Status](https://img.shields.io/badge/Status-In_Progress-yellow?style=flat-square)

---

## Concept

Instead of manually defining player profiles, this tool **learns them from the data**:

1. **K-Means** clusters PL players into archetypes (e.g. *Target Striker*, *Deep-lying Playmaker*)
2. **Random Forest** classifies any new player into an archetype
3. **Streamlit app** — search a player → archetype + similar players + radar chart

## Pipeline

```
FBref Stats → Preprocessing → PCA → K-Means → Random Forest → UMAP + Radar
               (per-90, scale)  (denoise)  (archetypes)  (classify)    (viz)
```

## Structure

```
pl-scouting-tool/
├── data/raw/               # FBref CSVs (gitignored)
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_clustering.ipynb
│   └── 04_classifier.ipynb
├── src/
│   ├── data.py             # scraping
│   ├── features.py         # per-90, filters
│   ├── model.py            # PCA + KMeans + RF
│   └── viz.py              # radar, UMAP
├── app.py                  # Streamlit app
└── requirements.txt
```

## Quickstart

```bash
pip install -r requirements.txt
python src/data.py          # fetch FBref data
jupyter notebook notebooks/ # run 01 → 04
streamlit run app.py
```

## Stack

`soccerdata` · `scikit-learn` · `umap-learn` · `mplsoccer` · `streamlit`

## Roadmap

- [x] Project setup
- [ ] EDA & preprocessing
- [ ] Clustering & archetype naming
- [ ] Classifier training
- [ ] Streamlit app
- [ ] Deploy on Streamlit Cloud

## License

MIT