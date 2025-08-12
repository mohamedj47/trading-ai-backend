import os
import pandas as pd
import yfinance as yf
import ccxt
from config import DATA_DIR, START_DATE

# الأزواج الأساسية
BASE_PAIRS = [
    "BTC-USD",
    "ETH-USD",
    "EURUSD=X",
    "GBPUSD=X",
    "USDJPY=X",
    "XAUUSD=X",
    "AUDUSD=X",
    "USDCAD=X",
    "NZDUSD=X"
]

# إنشاء مجلد البيانات لو مش موجود
os.makedirs(DATA_DIR, exist_ok=True)

def get_top_binance_pairs(limit=20):
    """جلب أعلى الأزواج تداولاً من Binance"""
    exchange = ccxt.binance()
    markets = exchange.load_markets()
    
    # ترتيب حسب الحجم
    pairs_sorted = sorted(
        markets.values(),
        key=lambda x: x['info'].get('quoteVolume', 0),
        reverse=True
    )
    
    top_pairs = []
    for p in pairs_sorted[:limit]:
        symbol = p['symbol'].replace("/", "-")
        # نحافظ على نفس تنسيق Yahoo Finance (USDT → USD)
        if symbol.endswith("-USDT"):
            symbol = symbol.replace("-USDT", "-USD")
        top_pairs.append(symbol)
    
    return top_pairs

def fetch_data():
    # ضم الأزواج الأساسية + الأعلى تداولاً
    top_pairs = get_top_binance_pairs()
    all_pairs = list(set(BASE_PAIRS + top_pairs))
    
    print(f"[+] إجمالي الأزواج التي سيتم تحميلها: {len(all_pairs)}")
    
    for pair in all_pairs:
        try:
            print(f"[+] جاري تحميل البيانات: {pair}")
            data = yf.download(pair, start=START_DATE)
            if not data.empty:
                file_path = os.path.join(DATA_DIR, f"{pair.replace('=', '').replace('-', '')}.csv")
                data.to_csv(file_path)
                print(f"    ✅ تم الحفظ: {file_path}")
            else:
                print(f"    ⚠ لا توجد بيانات لـ {pair}")
        except Exception as e:
            print(f"    ❌ خطأ في {pair}: {e}")

if __name__ == "__main__":
    fetch_data()
