# 🏆 Predictive E-Sports Win-Rate Engine

## Project Summary

This project demonstrates the application of **predictive machine learning** to time-series game telemetry data. The goal is to build a robust model capable of calculating the real-time probability of an E-Sports team winning a match, based on in-game events and metrics (like gold advantage, objective control, and kill/death ratios).

This serves as a foundational project showcasing proficiency in **data engineering, feature creation, and model deployment**, which are crucial skills for working with generative AI pipelines in the gaming industry.

## Technical Highlights

|Feature|Description|Relevant Skill / Technology|
|---|---|---|
|**Data Pipeline**|Uses an API to ingest high-frequency, time-series data streams (game logs).|Python, HTTP Requests (API Integration)|
|**Feature Engineering**|Transforms raw in-game metrics into predictive features, such as **Momentum Index** and **Gold-per-Minute Differential.**|Pandas, NumPy|
|**Model**|Implements a **Classification Model** (e.g., Random Forest or Logistic Regression from Scikit-learn) trained to predict the final outcome from mid-game states.|Scikit-learn, Supervised Learning|
|**Architecture**|Follows a strict ML pipeline (Acquisition $\rightarrow$ Processing $\rightarrow$ Prediction) documented in `docs/ARCHITECTURE.md`.|Modular Code Design|

## Repository Structure

The project follows a clean, modular structure for scalability and maintenance:

```
esports-winrate-engine/
├── docs/                 # Design and Architecture documents
├── src/                  # Core Python source code
│   ├── pipeline/         # Modules for data fetching, feature engineering, and model training
│   └── predict_match.py  # Main entry point for running a prediction
├── data/                 # Raw and processed datasets
└── models/               # Saved, trained machine learning models (.pkl files)
```

## Setup and Installation

### Requirements

This project requires **Python 3.8+** and the following packages, detailed in `requirements.txt`:

- `pandas`
    
- `numpy`
    
- `scikit-learn`
    
- `requests` (for API calls)
    
- `matplotlib` (for visualizations)
    

### How to Run

1. **Clone the Repository:**
    
    ```
    git clone [https://github.com/ryangilbert-github/Phase1-Foundational-Data-Systems/esports-winrate-engine.git](https://github.com/ryangilbert-github/Phase1-Foundational-Data-Systems/esports-winrate-engine.git)
    cd Phase1-Foundational-Data-Systems/esports-winrate-engine
    ```
    
2. **Install Dependencies:**
    
    ```
    pip install -r requirements.txt
    ```
    
3. **Run the Pipeline (WIP):** _[Instructions for running data fetch/model training will be added here upon completion of **Day 34** of the 100 Days of Code Bootcamp.]_
    

## Status: Work in Progress 🛠️

This project is actively being developed. The design architecture is complete, and the coding phase will commence upon mastery of the relevant **Python Data Science (Pandas/NumPy)** and **API integration** modules in the current learning roadmap.
