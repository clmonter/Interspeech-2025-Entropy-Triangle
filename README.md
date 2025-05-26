# Interspeech 2025 — Entropy Triangle to understand Acoustic Scene Classification

🥳 Welcome to our repo!!

This repository accompanies our **Interspeech 2025 paper**:  
**"Beyond Conventional Metrics: using Entropic Triangles to Explain Balancing Methods in Acoustic Scene Classification"**

🤗 It's an easy and visual way to **understand how data imbalance and different loss-weighting functions affect model training** through the **Entropic Triangle** framework.  
We share all the details of our work — including **code, custom dataset partitions, and examples** — so you can reproduce the experiments and explore the results yourself.

🌐 You just need to save all the confussion matrices during your training.

## 🔍 Overview

Understanding soundscapes is essential for real-world AI systems — but imbalanced data can severely harm model performance.

In this work, we analyze the **impact of different loss-weighting functions** to combat the imbalance, on the training dynamics of CP-Mobile using the **Entropic Triangle framework**.

We use:

- 🧠 **Dataset**: [TAU Urban Acoustic Scenes 2022 Mobile](https://zenodo.org/records/6337421)
- 🌐 **Model**: [CP-Mobile](https://github.com/fschmid56/cpjku_dcase23)
- 🔺 **Analysis**: Entropic Triangle to understand learning under imbalance

## 📁 Repository structure

- `labels/`: Custom train/val/test splits for balanced and imbalanced setups
- `src/`: Information theory functions, plots and other utils in order to use the entropic triangle framework
- `notebooks/`: Jupyter notebooks for understanding, plotting and exploring the results and the entropic triangle
- `results/`: Saved confussion matrices during training and evaluation

## 🚀 Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/clmonter/interspeech2025-entropy-triangle.git
cd interspeech2025-entropy-triangle
```

### 2. Understand how to use the entropic triangle framework easily!

🤗 Go to `notebooks/Part1_easy_entropy_introduction.ipynb` to better understand this framework! It's easy and quick

### 3. See and understand all our results

🤔 Go to `notebooks/Part2_triangle_for_ASC.ipynb` and play by visualizing all the results! You can also use your own confussion matrices

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
