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
- 🎯 Adaptive logic for small to mega (I saved them!!!!)
influencershttps://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTljNDYzdWFwNDhqaTdma2VtOWF2YzVhajkweDBlNzc0dHoydGhkYiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/5xtDarwEPSrmbvS0dHy/giphy.gif

---

## 🧠 Detection Logic

The system uses a **multi-factor scoring approach**:

- Engagement rate (likes + comments vs followers)
- Like ratio (likes vs followers)
- Follower size segmentation

Larger influencers are evaluated differently to avoid bias due to naturally lower engagement rates.

---

## 📂 Project Structure

Fake Influencer Detector/
│
├── main.py
├── top_insta_influencers_data.csv
└── README.md

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/divyanshsinghtomar-official/fake-influencer-detector.git
cd fake-influencer-detector

---

## ▶️ Getting Started

1. Clone the repository
git clone https://github.com/YOUR_USERNAME/fake-influencer-detector.git
cd fake-influencer-detector

2. Install dependencies
pip install pandas numpy

3. Run the project
python main.py

<img width="464" height="159" alt="image" src="https://github.com/user-attachments/assets/8e56724d-188a-4d2a-8069-2464c86ebd9e" />

📈 Future Improvements
Add data visualization (matplotlib)
Integrate machine learning model
Real-time Instagram data integration

⚠️ Disclaimer

This project is for educational and analytical purposes only.
The classification is based on heuristic rules and may not reflect real-world accuracy.

🙌 Author

Divyansh Singh Tomar 

⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
