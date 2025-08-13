import pandas as pd
import os

# تحديد المسار
TEST_DATA = "data/test_data.csv"

# إنشاء المجلد لو مش موجود
os.makedirs("data", exist_ok=True)

# بيانات تجريبية
data = {
    "feature1": [0.5, 0.8, 0.3, 0.9],
    "feature2": [1.2, 0.7, 1.8, 0.5],
    "target": [0, 1, 0, 1]
}

# حفظ البيانات
df = pd.DataFrame(data)
df.to_csv(TEST_DATA, index=False)

print(f"✅ تم إنشاء ملف الاختبار: {TEST_DATA}")
