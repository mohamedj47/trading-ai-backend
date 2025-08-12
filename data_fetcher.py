import os
import pandas as pd
from binance.client import Client
from config import BINANCE_API_KEY, BINANCE_API_SECRET, DATA_DIR, START_DATE

# إنشاء مجلد البيانات إذا مش موجود
os.makedirs(DATA_DIR, exist_ok=True)

# تهيئة عميل Binance
client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

def fetch_historical_data(symbol="BTCUSDT", interval=Client.KLINE_INTERVAL_1DAY):
    """تحميل البيانات التاريخية من Binance"""
    print(f"جاري تحميل البيانات لـ {symbol}...")
    klines = client.get_historical_klines(symbol, interval, START_DATE)

    # تحويل البيانات إلى DataFrame
    df = pd.DataFrame(klines, columns=[
        "timestamp", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
    ])

    # تحويل التواريخ
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit='ms')
    df.set_index("timestamp", inplace=True)

    # حفظ الملف
    file_path = os.path.join(DATA_DIR, f"{symbol}.csv")
    df.to_csv(file_path)
    print(f"تم حفظ البيانات في {file_path}")

if __name__ == "__main__":
    fetch_historical_data()
