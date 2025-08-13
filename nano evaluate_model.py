import os
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

# مسار مجلد الموديلات المحفوظة
MODELS_DIR = "models"

# مسار بيانات الاختبار
TEST_DATA = "data/test_data.csv"  # غيّره لو عندك ملف تاني

def load_test_data():
    if not os.path.exists(TEST_DATA):
        raise FileNotFoundError(f"❌ ملف الاختبار غير موجود: {TEST_DATA}")
    df = pd.read_csv(TEST_DATA)
    X = df.drop("target", axis=1)
    y = df["target"]
    return X, y

def evaluate_model(model_path, X, y):
    model = joblib.load(model_path)
    preds = model.predict(X)
    acc = accuracy_score(y, preds)
    print(f"📊 {os.path.basename(model_path)} - الدقة: {acc:.2%}")
    print(classification_report(y, preds))

if __name__ == "__main__":
    X_test, y_test = load_test_data()

    if not os.path.exists(MODELS_DIR):
        raise FileNotFoundError(f"❌ مجلد الموديلات غير موجود: {MODELS_DIR}")

    for file in os.listdir(MODELS_DIR):
        if file.endswith(".pkl"):
            model_path = os.path.join(MODELS_DIR, file)
            evaluate_model(model_path, X_test, y_test)
