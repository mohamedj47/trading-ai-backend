import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
from config import DATA_DIR, MODEL_PATH

def load_data(symbol="BTCUSDT"):
    """تحميل البيانات التاريخية"""
    file_path = os.path.join(DATA_DIR, f"{symbol}.csv")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"ملف البيانات {file_path} غير موجود.")
    
    df = pd.read_csv(file_path)
    df["close"] = df["close"].astype(float)
    
    # إنشاء إشارات (صعود / هبوط)
    df["target"] = np.where(df["close"].shift(-1) > df["close"], 1, 0)
    
    return df.dropna()

def train_model(symbol="BTCUSDT"):
    """تدريب نموذج التنبؤ"""
    df = load_data(symbol)
    
    X = df[["open", "high", "low", "close", "volume"]]
    y = df["target"]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"دقة النموذج: {acc * 100:.2f}%")
    
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"تم حفظ النموذج في {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
