# app.py

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_wrangler import load_and_clean_data # Import the cleaning function

# --- 1. LOAD DATA ---
df = load_and_clean_data()
st.sidebar.success(f"Data Wrangling Complete: {len(df)} records loaded.")

# --- 2. EXPLORATORY DATA ANALYSIS (EDA) ---
st.title("Interactive Data Visualization & Statistical Dashboard")
st.markdown("---")

st.header("Exploratory Data Analysis (EDA)")

# Filter by Category (UI Element)
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
