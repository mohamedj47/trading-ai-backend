import os
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from config import TEST_DATA, MODELS_DIR


def load_test_data():
    if not os.path.exists(TEST_DATA):
        raise FileNotFoundError(f"❌ ملف الاختبار غير موجود: {TEST_DATA}")

    df = pd.read_csv(TEST_DATA)
    X_test = df.drop(columns=["target"])
    y_test = df["target"]
    return X_test, y_test


def evaluate_model(model_path, X_test, y_test):
    model = joblib.load(model_path)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"📊 {os.path.basename(model_path)} - الدقة: {acc:.2%}")
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    X_test, y_test = load_test_data()

    for filename in os.listdir(MODELS_DIR):
        if filename.endswith(".pkl"):
            model_path = os.path.join(MODELS_DIR, filename)
            evaluate_model(model_path, X_test, y_test)

