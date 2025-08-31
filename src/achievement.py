import pandas as pd
import re
import os


# Proje klasörü
BASE_DIR = os.path.dirname(__file__)

# Dosya yolları
dosya_v1_yolu = os.path.join(BASE_DIR,"..", "output", "find_number_v1.xlsx")
dosya_v2_yolu = os.path.join(BASE_DIR,"..", "output", "find_number_v2.xlsx")
ana_dosya_yolu = os.path.join(BASE_DIR,"..", "data", "sample_phone_number.xlsx")

# Dosyaları oku
df_ana = pd.read_excel(ana_dosya_yolu)
df_v1 = pd.read_excel(dosya_v1_yolu)
df_v2 = pd.read_excel(dosya_v2_yolu)

try:
    # Tüm dosyaları Excel (XLSX) formatında oku
    df_ana = pd.read_excel(ana_dosya_yolu)
    df_v1 = pd.read_excel(dosya_v1_yolu)
    df_v2 = pd.read_excel(dosya_v2_yolu)
    print("All files successfully read.")
except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Please make sure that the file paths and names are correct.")
    exit()

def normalize_phone_number(number):
    """Standardizes the phone number."""
    if pd.isna(number):
        return ''
    
    # Numarayı string'e çevir
    s = str(number)
    
    # +90, 0090, parantez, tire, boşluk gibi karakterleri temizle
    s = re.sub(r'[\s\(\)\-+]', '', s)
    s = s.replace('+90', '').replace('0090', '')
    
    # Eğer numara 0 ile başlıyorsa (ülke kodu yerine), 0'ı kaldır
    if s.startswith('0') and len(s) > 10:
        s = s[1:]
    
    # Son 10 haneyi al (varsayılan Türkiye numarası formatı)
    if len(s) > 10:
        s = s[-10:]
        
    return s.strip()

# Ana verisetindeki telefon numaralarını normalize et
df_ana['Normalized'] = df_ana['Phone Number'].apply(normalize_phone_number)

# V1 ve V2 dosyalarındaki bulunan telefon numaralarını normalize et
df_v1['Normalized'] = df_v1['Find Number'].apply(normalize_phone_number)
df_v2['Normalized'] = df_v2['Find Number'].apply(normalize_phone_number)

# Ana verisetini (doğru cevapları) bir sete çevir
ana_set = set(df_ana['Normalized'])

# Metrikleri hesaplayan fonksiyon
def calculate_performance(df, correct_set):
    found = 0
    correctly_found = 0
    
    for number in df['Normalized']:
        if number: # Eğer numara boş değilse (bir şeyler bulunmuşsa)
            found += 1
            if number in correct_set:
                correctly_found += 1
    
    not_found = len(correct_set) - correctly_found
    total_to_find = len(correct_set)
    success_rate = (correctly_found / total_to_find) * 100 if total_to_find > 0 else 0
    
    return total_to_find, correctly_found, found, not_found, success_rate

# Versiyonların performansını hesapla
total_ana, correctly_found_v1, found_v1, not_found_v1, success_rate_v1 = calculate_performance(df_v1, ana_set)
total_ana, correctly_found_v2, found_v2, not_found_v2, success_rate_v2 = calculate_performance(df_v2, ana_set)

# Sonuçları ekrana yazdır
print("\n--- Analysis Results ---")
print(f"Total Phone Number: {total_ana}\n")

print("--- Version 1 ---")
print(f"Phone Numbers Successfully Found: {correctly_found_v1}")
print(f"Missing or Incorrectly Found: {not_found_v1}")
print(f"Success Rate: %{success_rate_v1:.2f}")

print("\n--- Version 2 ---")
print(f"Phone Numbers Successfully Found: {correctly_found_v2}")
print(f"Missing or Incorrectly Found: {not_found_v2}")
print(f"Success Rate: %{success_rate_v2:.2f}")

# Karşılaştırma ve Sonuç
print("\n--- Comparison ---")
if success_rate_v1 > success_rate_v2:
    print("Version 1 has better performance.")
elif success_rate_v2 > success_rate_v1:
    print("Version 2 has better performance.")
else:
    print("Both versions have the same performance.")