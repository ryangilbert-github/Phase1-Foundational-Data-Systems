# Python Capstone: Data-Driven Gaming Systems - Project 1A
# Demonstrates: Supervised Learning (Sklearn), Feature Engineering, Data Wrangling

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# --- 1. DATA WRANGLING AND FEATURE ENGINEERING ---
def load_and_prepare_data(file_path):
    """Loads raw game telemetry data and engineers predictive features."""
    print("Loading data and initiating feature engineering...")
    df = pd.read_csv(file_path)
    
    # Feature Engineering: XP Advantage, Gold Difference
    df['xp_advantage'] = df['team_a_xp'] - df['team_b_xp']
    df['gold_diff'] = df['team_a_gold'] - df['team_b_gold']
    
    # Define features (X) and target (y)
    features = ['game_time', 'xp_advantage', 'gold_diff', 'kills_a', 'kills_b']
    X = df[features]
    y = df['win_team_a'] # Target: 1 if Team A wins, 0 otherwise
    
    return X, y

# --- 2. SUPERVISED LEARNING MODEL TRAINING ---
def train_win_rate_model(X, y):
    """Trains a Logistic Regression model for win-rate prediction."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression(solver='liblinear')
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Model trained. Test Accuracy: {accuracy:.4f}")
    return model

if __name__ == '__main__':
    # Mock data source for demonstration
    mock_data = {
        'game_time': np.arange(100, 5100, 100),
        'team_a_xp': np.random.randint(500, 15000, 50),
        'team_b_xp': np.random.randint(500, 15000, 50),
        'team_a_gold': np.random.randint(1000, 30000, 50),
        'team_b_gold': np.random.randint(1000, 30000, 50),
        'kills_a': np.random.randint(0, 20, 50),
        'kills_b': np.random.randint(0, 20, 50),
        'win_team_a': np.random.randint(0, 2, 50) 
    }
    mock_df = pd.DataFrame(mock_data)
    MOCK_FILE_PATH = 'mock_game_telemetry.csv'
    mock_df.to_csv(MOCK_FILE_PATH, index=False)
    
    # Execution steps
    # (Simplified printout for brevity)
