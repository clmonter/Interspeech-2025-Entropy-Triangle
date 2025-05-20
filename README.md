# Interspeech 2025 — Entropy Triangle for Acoustic Scene Classification

🥳 Welcome to our repo!!

This repository accompanies our **Interspeech 2025 paper**:  
**"Beyond Conventional Metrics: using Entropic Triangles to Explain Balancing Methods in Acoustic Scene Classification"**

🤗 It's an easy and visual way to **understand how data imbalance and different loss-weighting functions affect model training** through the **Entropic Triangle** framework.  
We share all the details of our work — including **code, custom dataset partitions, and examples** — so you can reproduce the experiments and explore the results yourself.


## 🔍 Overview

Understanding soundscapes is essential for real-world AI systems — but imbalanced data can severely harm model performance.

In this work, we analyze the **impact of data imbalance** on the training dynamics of SOTA models using the **Entropic Triangle framework**.

We use:

- 🧠 **Dataset**: [TAU Urban Acoustic Scenes 2022 Mobile](https://zenodo.org/records/6337421)
- 🌐 **Model**: [CP-Mobile](https://github.com/fschmid56/cpjku_dcase23)
- 🔺 **Analysis**: Entropic Triangle to understand learning under imbalance

## 📁 Repository structure

- `data/partitions/`: Custom train/val/test splits for balanced and imbalanced setups
- `src/`: Training pipeline, evaluation code, entropic triangle computation
- `notebooks/`: Jupyter notebooks for plotting and exploring the results
- `results/`: Saved figures and result summaries

## 🚀 Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/clmonter/interspeech2025-entropy-triangle.git
cd interspeech2025-entropy-triangle
```

### 2. Set up environment

* Option 1 — with pip

```bash
pip install -r requirements.txt
```

* Option 2 — with conda

```bash
conda env create -f environment.yml
conda activate entropy-asc
```

## 📜 Citation

If you use this repo, please cite our paper:

```mathematica
@inproceedings{montero-ramirez2025,
  title={Beyond Conventional Metrics: using Entropic Triangles to Explain Balancing Methods in Acoustic Scene Classification},
  author={C. Montero-Ramirez et al.},
  booktitle={Proceedings of Interspeech 2025},
  year={2025}
}
```
