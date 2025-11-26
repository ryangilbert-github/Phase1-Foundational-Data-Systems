# Data Analysis Dashboard (Streamlit)
# Project 3: Demonstrates EDA, Statistical Visualization, and Data Wrangling

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. DATA WRANGLING AND PREPARATION ---
@st.cache_data
def load_data():
    """Simulates complex data loading and cleaning (Data Wrangling)."""
    data = {
        'Category': np.random.choice(['CPU', 'GPU', 'RAM', 'Storage'], 100),
        'Price': np.random.uniform(50, 800, 100),
        'Performance': np.random.uniform(10, 100, 100),
        'Release_Year': np.random.randint(2018, 2024, 100)
    }
    df = pd.DataFrame(data)
    
    # Simulate data cleaning
    df.loc[df['Performance'] > 95, 'Price'] *= 1.5
    
    st.sidebar.success("Data Wrangling Complete: 100 records loaded.")
    return df

df = load_data()

# --- 2. EXPLORATORY DATA ANALYSIS (EDA) ---
st.title("Interactive Data Visualization & Statistical Dashboard")
st.markdown("---")

st.header("Exploratory Data Analysis (EDA)")

# Filter by Category
selected_category = st.sidebar.multiselect(
    "Filter by Component Category",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

filtered_df = df[df['Category'].isin(selected_category)]

st.subheader(f"Data Distribution for {', '.join(selected_category)}")
st.dataframe(filtered_df.head(10))

# --- 3. STATISTICAL VISUALIZATION ---
st.header("Statistical Visualization (Matplotlib & Seaborn)")

# Visualization 1: Scatter Plot (Price vs Performance)
fig, ax = plt.subplots(figsize=(8, 4))
sns.scatterplot(x='Price', y='Performance', hue='Category', data=filtered_df, ax=ax)
ax.set_title("Price vs. Performance by Component (Seaborn)")
st.pyplot(fig)

# Visualization 2: Distribution Plot (Feature Engineering Check)
st.subheader("Performance Distribution")
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.histplot(filtered_df['Performance'], kde=True, ax=ax2)
ax2.set_title("Performance Histogram")
st.pyplot(fig2)


# --- 4. DATA INSIGHTS ---
st.header("Key Insights")
avg_price = filtered_df['Price'].mean()
st.info(f"The average price for the selected components is **£{avg_price:.2f}**. This analysis provides the foundational data for later **Feature Engineering** in LLM/AI model training.")
