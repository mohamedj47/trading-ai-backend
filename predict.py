import pandas as pd
import joblib
from datetime import datetime
import pytz

# الأزواج اللي هنشتغل عليها
symbols = [
    "BTC/USDT", "ETH/USDT", "EUR/USD", "GBP/USD", "USD/JPY",
    "XAU/USD", "AUD/USD", "USD/CAD", "NZD/USD"
]

# تحميل النماذج والتنبؤ
def load_and_predict():
    results = []
    for symbol in symbols:
        try:
            model = joblib.load(f"models/{symbol.replace('/', '_')}_model.pkl")
            latest_data = pd.read_csv(f"data/{symbol.replace('/', '_')}.csv").tail(1)
            X_latest = latest_data.drop(columns=["Date", "Close"])
            pred = model.predict(X_latest)[0]
            proba = model.predict_proba(X_latest)[0].max()

            direction = "صعود" if pred == 1 else "هبوط"
            color = "🟢" if pred == 1 else "🔴"

            # التوقيت بتوقيت مصر
            egypt_tz = pytz.timezone("Africa/Cairo")
            now_egypt = datetime.now(egypt_tz).strftime("%Y-%m-%d %H:%M:%S")

            results.append({
                "زوج": symbol,
                "إشارة": direction,
                "ثقة": f"{proba*100:.2f}%",
                "لون": color,
                "وقت": now_egypt
            })
        except Exception as e:
            results.append({"زوج": symbol, "خطأ": str(e)})
    return results

if __name__ == "__main__":
    signals = load_and_predict()
    for sig in signals:
        print(sig)
