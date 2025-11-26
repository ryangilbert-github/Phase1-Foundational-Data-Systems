# 📊 E-Sports Win-Rate Engine - ARCHITECTURE DOCUMENT

This document outlines the high-level Machine Learning (ML) pipeline for the E-Sports Win-Rate Engine, demonstrating the full flow from data ingestion to predictive output.

## 1. Pipeline Overview (Flowchart)

The system operates in a sequential, four-stage pipeline:

**Data Acquisition** $\rightarrow$ **Data Preprocessing/Feature Engineering** $\rightarrow$ **Model Training & Persistence** $\rightarrow$ **Real-Time Prediction**

## 2. Pipeline Stages

### Stage 1: Data Acquisition (`src/pipeline/data_fetcher.py`)

**Goal:** Secure raw game telemetry (time-series data) from a public API (e.g., specific game statistics API).

|**Component**|**Description**|
|---|---|
|**API Connector**|Handles HTTP requests to the external E-Sports data API (a skill covered around **Day 33** of your Python course).|
|**Ingestion**|Parses raw JSON/XML data into a structured **Pandas DataFrame**.|
|**Storage**|Saves the raw, time-stamped data into `data/raw/raw_match_data.json` for historical analysis.|

### Stage 2: Data Preprocessing & Feature Engineering (`src/pipeline/feature_eng.py`)

**Goal:** Clean the raw data and create predictive features necessary for the model.

|**Component**|**Description**|
|---|---|
|**Cleaning**|Handles missing values (NaNs) and ensures data consistency (using **Pandas/NumPy** skills).|
|**Feature Creation**|**CRITICAL STEP.** Generates predictive signals (features) like: **Gold Difference, XP Advantage per Minute, Objective Control Rate,** and **Team Fight Win Percentage**.|
|**Labeling**|Assigns the final outcome label (`Win` or `Loss`) for supervised learning.|
|**Storage**|Saves the finalized feature set to `data/processed/features_v1.csv`.|

### Stage 3: Model Training & Persistence (`src/pipeline/model_trainer.py`)

**Goal:** Train a robust classification model and save the optimized version for deployment.

|**Component**|**Description**|
|---|---|
|**Model Selection**|Uses **Scikit-learn** to select and tune a classifier (e.g., Random Forest, Logistic Regression) suitable for time-series classification.|
|**Training**|Trains the model on the preprocessed feature data.|
|**Evaluation**|Assesses model performance using metrics like **Accuracy, F1-Score, and AUC (Area Under the Curve)**.|
|**Persistence**|Saves the trained model object using Python's `pickle` library into the `models/` directory for fast loading during predictions.|

### Stage 4: Real-Time Prediction (`src/predict_match.py`)

**Goal:** Load the saved model and use new, incoming game data to generate an immediate win-rate probability.

| **Component**       | **Description**                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------- |
| **Model Loader**    | Loads the persisted model from `models/winrate_model_v1.pkl`.                                         |
| **Feature Adapter** | Converts new, incoming live game data into the _exact_ same feature format used during training.      |
| **Predictor**       | Calls the model's `.predict_proba()` method to output the **current Win Probability** (a percentage). |
| **Output**          | Sends the probability to the user interface/dashboard for visualization.                              |
