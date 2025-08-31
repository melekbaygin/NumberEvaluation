import pandas as pd
import re
import os

# Proje klasörü
BASE_DIR = os.path.dirname(__file__)

# Dosya yolları
input_file = os.path.join(BASE_DIR, "..", "data","sample_phone_number.xlsx")
output_file = os.path.join(BASE_DIR,"..", "output", "find_number_v1.xlsx")

# Excel'i oku (girdi dosyası)
df = pd.read_excel(input_file)

# Telefon numarası deseni (basit)
pattern = re.compile(r'0?5\d{2}[\s]?\d{3}[\s]?\d{2}[\s]?\d{2}')

def find_phone_numbers(cell):
    if pd.isna(cell):
        return None
    match = pattern.search(str(cell))
    return match.group() if match else None

# Telefon numaralarını bul ve yeni sütuna yaz
df["Find Number"] = df["Phone Number"].apply(find_phone_numbers)

# Yeni Excel'e kaydet (çıktı dosyası)
df.to_excel(output_file, index=False)
print(f"✅ V1 scan is complete. Output: {output_file}")
