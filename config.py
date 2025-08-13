import os

# إعدادات API Keys (من environment variables)
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY", "")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET", "")

# مجلدات البيانات والنماذج
DATA_DIR = "data"
MODELS_DIR = "models"

# ملف بيانات الاختبار
TEST_DATA = os.path.join(DATA_DIR, "test_data.csv")  # << هنا الإضافة المهمة

# نطاق البيانات التاريخية
START_DATE = "2015-01-01"

# إعدادات التدريب
TEST_SIZE = 0.2
RANDOM_STATE = 42

