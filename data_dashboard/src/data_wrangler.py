# src/data_wrangler.py

import streamlit as st
import pandas as pd
import numpy as np

# --- 1. DATA WRANGLING AND PREPARATION ---
@st.cache_data
def load_and_clean_data():
    """Simulates complex data loading and cleaning (Data Wrangling)."""
    
    # 1. Simulate Data Ingestion
    data = {
        'Category': np.random.choice(['CPU', 'GPU', 'RAM', 'Storage'], 100),
        'Price': np.random.uniform(50, 800, 100),
        'Performance': np.random.uniform(10, 100, 100),
        'Release_Year': np.random.randint(2018, 2024, 100)
    }
    df = pd.DataFrame(data)
    
    # 2. Simulate Data Cleaning / Transformation
    # Adjust price based on high performance (Feature Engineering Check)
    df.loc[df['Performance'] > 95, 'Price'] *= 1.5
    
    return df
