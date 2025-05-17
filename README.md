# 🕵️‍♂️ Fake Profile Detection using Machine Learning

## 📌 Overview

This project uses machine learning techniques to detect fake social media profiles based on profile features and behavioral attributes. It processes real and synthetic datasets to classify whether a user profile is genuine or fake.

## 🎯 Objectives

- Identify and classify fake social media profiles
- Train and evaluate machine learning models on labeled datasets
- Improve detection accuracy using engineered features

---

## 🗃️ Dataset

The project uses multiple datasets derived from Facebook-like social profiles:

- `Dataset.csv`, `Dataset1.csv`, etc. — mixed data of real and fake profiles
- `Dataset-real-260.csv` — authentic profile samples
- `Dataset-fake-250.csv` — generated/simulated fake profiles

Each dataset contains features such as:
- Number of friends
- Number of posts
- Profile activity patterns
- Bio length
- Mutual friends, etc.

---

## 🧠 Machine Learning

- Algorithms used: Likely Logistic Regression, Random Forest, or SVM
- Trained model saved in `classifier.pkl`
- Preprocessing includes label encoding, normalization, and feature engineering
- Performance evaluated using accuracy, precision, recall, and F1-score

---

## 🛠️ Project Structure

├── fpd.py # Core Python script for model training/testing
├── classifier.pkl # Trained ML model
├── Dataset.csv # Main dataset
├── Dataset-real-260.csv # Real profile samples
├── Dataset-fake-250.csv # Fake profile samples
├── fakeprofielist.docx # List or description of known fake profiles
├── Dataset1.xlsx # Supplementary data
![image](https://github.com/user-attachments/assets/afde9967-e8a8-4fe3-bc37-ce5e1aee3933)
![image](https://github.com/user-attachments/assets/d1301a7b-0321-4305-aeda-17128e966759)
![image](https://github.com/user-attachments/assets/c9188b36-f962-46a5-8d4d-9e8240bf2f3d)

📈 Future Enhancements
Integration with social media APIs for real-time detection

Deep learning models for improved accuracy

Web interface for online detection service
