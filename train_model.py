import pandas as pd
import joblib
import glob
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier

# مجلد تخزين البيانات اللي تم تحميلها
DATA_DIR = "historical_data"
MODELS_DIR = "models"
os.makedirs(MODELS_DIR, exist_ok=True)

# دالة تجهيز البيانات
def prepare_data(df):
    df['Return'] = df['Close'].pct_change()
    df['Target'] = (df['Return'].shift(-1) > 0).astype(int)  # 1 صعود، 0 هبوط
    df = df.dropna()
    features = ['Open', 'High', 'Low', 'Close', 'Volume']
    X = df[features]
    y = df['Target']
    return X, y

# قائمة النماذج
models = {
    "RandomForest": RandomForestClassifier(n_estimators=200),
    "GradientBoosting": GradientBoostingClassifier(),
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "KNN": KNeighborsClassifier(),
    "DecisionTree": DecisionTreeClassifier(),
    "SVC": SVC(probability=True),
    "XGBoost": XGBClassifier(eval_metric='logloss'),
    "LightGBM": LGBMClassifier(),
    "CatBoost": CatBoostClassifier(verbose=0)
}

# تدريب كل زوج عملة على النماذج
for file_path in glob.glob(f"{DATA_DIR}/*.csv"):
    pair_name = os.path.basename(file_path).replace(".csv", "")
    print(f"\n--- Training models for {pair_name} ---")
    
    df = pd.read_csv(file_path)
    X, y = prepare_data(df)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )
    
    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        print(f"{name} Accuracy: {acc:.4f}")
        
        # حفظ النموذج
        model_filename = f"{MODELS_DIR}/{pair_name}_{name}.pkl"
        joblib.dump(model, model_filename)

print("\n✅ All models trained and saved successfully.")
