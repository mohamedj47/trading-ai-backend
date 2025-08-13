import os

# إعدادات API Keys
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY", "")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET", "")

# مجلدات البيانات والنماذج
DATA_DIR = "data"
MODELS_DIR = "models"

# إنشاء المجلدات لو مش موجودة
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)

# ملف بيانات الاختبار
TEST_DATA = os.path.join(DATA_DIR, "test_data.csv")

if not os.path.exists(TEST_DATA):
    with open(TEST_DATA, "w") as f:
        f.write("date,open,high,low,close,volume\n")

# نطاق البيانات التاريخية
START_DATE = "2015-01-01"

# إعدادات التدريب
TEST_SIZE = 0.2
RANDOM_STATE = 42




