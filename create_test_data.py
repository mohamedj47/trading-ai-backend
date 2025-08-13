import pandas as pd
import numpy as np
import os

# تحديد المسار
os.makedirs("data", exist_ok=True)
file_path = "data/test_data.csv"

# إنشاء بيانات عشوائية للتجربة
np.random.seed(42)
df = pd.DataFrame({
    "feature1": np.random.rand(50),
    "feature2": np.random.rand(50),
    "feature3": np.random.rand(50),
    "target": np.random.randint(0, 2, size=50)  # 0 أو 1
})

# حفظ الملف
df.to_csv(file_path, index=False, encoding="utf-8-sig")
print(f"✅ تم إنشاء ملف الاختبار: {file_path}")
