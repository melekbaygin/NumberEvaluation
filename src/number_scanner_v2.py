import pandas as pd
import re
import os

# Proje klasörü
BASE_DIR = os.path.dirname(__file__)

# Dosya yolları
input_file = os.path.join(BASE_DIR,"..", "data", "sample_phone_number.xlsx")
output_file = os.path.join(BASE_DIR,"..", "output", "find_number_v2.xlsx")

# Excel'i oku
df = pd.read_excel(input_file)

# Telefon numarası olabilecek formatları kapsayan gelişmiş regex
pattern = re.compile(
    r'''
    (?:(?:\+|00)\d{1,3}[\s\-\.]?)?    # +90, 0090 gibi uluslararası kod
    (?:\(?\d{3,4}\)?[\s\-\.]?)        # (312), 312, (0555) gibi alan kodu
    \d{2,3}[\s\-\.]?                  # numaranın ilk kısmı
    \d{2,3}[\s\-\.]?                  # numaranın ikinci kısmı
    \d{2,3}                           # numaranın son kısmı
    ''',
    re.VERBOSE
)

def find_phone_numbers(cell):
    if pd.isna(cell):
        return None
    match = pattern.search(str(cell))
    return match.group() if match else None

# Telefon numaralarını bul ve yeni sütuna yaz
df["Find Number"] = df["Phone Number"].apply(find_phone_numbers)

df.to_excel(output_file, index=False)
print(f"✅ V2 scan is complete. Output: {output_file}")
