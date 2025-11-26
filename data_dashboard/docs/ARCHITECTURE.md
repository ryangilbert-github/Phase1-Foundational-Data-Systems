# 📊 Data Visualization Dashboard - ARCHITECTURE DOCUMENT

This document outlines the pipeline architecture for the Streamlit dashboard, emphasizing the foundational steps of data preparation and analysis required before any data is passed to a Machine Learning or Generative AI training process.

## 1. Data Flow Architecture

The dashboard follows a standard three-stage pipeline: **Ingestion & Wrangling $\rightarrow$ Analysis $\rightarrow$ Visualization.** 

| Stage | Component | Core Function |
| :--- | :--- | :--- |
| **1. Ingestion & Wrangling** | `src/data_wrangler.py` | Load raw data, handle missing values, and perform feature transformations (e.g., creating derived metrics like Price/Performance ratio). Utilizes `@st.cache_data` for performance optimization. |
| **2. Analysis & Filtering** | `app.py` / Streamlit Sidebar | Apply user-defined filters (`Category` multiselect) to focus the analysis on specific component subsets, enabling targeted EDA. |
| **3. Visualization** | `app.py` / Matplotlib/Seaborn | Generate statistical charts (scatter plots, histograms) to identify data distribution, outliers, and potential biases in the dataset. |

## 2. Visualization Strategy (EDA Focus)

The primary goal of this dashboard is **Exploratory Data Analysis (EDA)**. The visualization choices are intentional:

* **Scatter Plot (Price vs. Performance):** Used to check for **correlation** and identify **outliers** (components that are too expensive or too poorly performing). In an AI context, outliers need to be handled carefully or removed before training.
* **Histogram (Performance Distribution):** Used to check the **distribution** of a key feature. This helps determine if the data is normally distributed, which is an assumption for many classical ML algorithms.

## 3. Security and Optimization

* **Caching:** The use of `st.cache_data` ensures the **data wrangling logic only runs once**, improving load times and reducing computational overhead, a critical consideration for large-scale data systems.
