# Fake Influencer Detector

<p align="center">
  Detect fake and suspicious Instagram influencers using data analysis.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-green?style=for-the-badge&logo=pandas">
</p>

---

## 📌 Overview

**Fake Influencer Detector** is a data analysis project built using **Python** and **Pandas** that identifies fake or suspicious Instagram influencers based on engagement patterns and follower behavior.

The system analyzes:

* Engagement Rate
* Like Ratio
* Follower Count

Based on these metrics, influencers are classified into:

* ✅ Genuine Influencer
* ⚠️ Suspicious Influencer
* ❌ Fake Influencer

---

## ⚡ Key Features

* 📊 Data Cleaning & Preprocessing
* 📈 Engagement Rate Analysis
* ❤️ Like Ratio Calculation
* 🧠 Rule-Based + Score-Based Classification
* 🎯 Adaptive logic for small to mega influencers
* 🗂 CSV Dataset Processing
* ⚡ Lightweight and fast execution

---

## 🧠 Detection Logic

The system uses a **multi-factor scoring approach**:

* Engagement Rate (likes + comments vs followers)
* Like Ratio (likes vs followers)
* Follower size segmentation
* Score-based classification rules

Larger influencers are evaluated differently to avoid bias due to naturally lower engagement rates.

---

## 📂 Project Structure

```
Fake Influencer Detector/
│
├── main.py
├── top_insta_influencers_data.csv
└── README.md
```

---

## ▶️ Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/divyanshsinghtomar-official/fake-influencer-detector.git
cd fake-influencer-detector
```

### 2️⃣ Install dependencies

```bash
pip install pandas numpy
```

### 3️⃣ Run the project

```bash
python main.py
```

---

## 📊 Example Output

The script processes influencer data and classifies them as:

* Genuine
* Suspicious
* Fake

You will see results printed in the terminal after execution.

<img width="472" height="154" alt="image" src="https://github.com/user-attachments/assets/e210eae3-bd01-4a0c-9611-dc8ad7e3c3f6" />


---

## 📈 Future Improvements

* Add data visualization using Matplotlib
* Integrate machine learning model
* Real-time Instagram data integration

---

## ⚠️ Disclaimer

This project is for **educational and analytical purposes only**.
The classification is based on heuristic rules and may not reflect real-world accuracy.

---

## 🙌 Author

**Divyansh Singh Tomar**

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

* Fork the repository
* Create a new branch
* Submit a pull request

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

---

## 📜 License

This project is open-source and available under the **MIT License**.
