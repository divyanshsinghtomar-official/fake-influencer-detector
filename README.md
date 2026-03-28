<h1 align="center">Fake Influencer Detector</h1>

<p align="center">
  Detect fake and suspicious Instagram influencers using data analysis.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-green?style=for-the-badge&logo=pandas">
</p>

---

## 📌 Overview

Fake Influencer Detector is a data analysis project built using Python and Pandas that identifies fake or suspicious Instagram accounts based on engagement patterns and follower behavior.

The system analyzes:
- Engagement Rate
- Like Ratio
- Follower Count

and classifies influencers into:
- Genuine Influencer
- Suspicious Influencer
- Fake Influencer

---

## ⚡ Key Features

- 📊 Data Cleaning & Preprocessing
- 📈 Engagement Rate Analysis
- ❤️ Like Ratio Calculation
- 🧠 Rule-Based + Score-Based Classification
- 🎯 Adaptive logic for small to mega influencers

---

## 🧠 Detection Logic

The system uses a **multi-factor scoring approach**:

- Engagement rate (likes + comments vs followers)
- Like ratio (likes vs followers)
- Follower size segmentation

Larger influencers are evaluated differently to avoid bias due to naturally lower engagement rates.

---

## 📂 Project Structure
