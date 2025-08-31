# NumberEvaluation

Bu proje, bir Excel dosyasındaki telefon numaralarını tespit etmek ve farklı algoritmaların başarı oranlarını karşılaştırmak için geliştirilmiştir.

## Kurulum

1. **Python Kurulumu**  
   Eğer bilgisayarınızda Python yoksa, [python.org/downloads](https://www.python.org/downloads/) adresinden Python 3.x sürümünü indirip kurun.  
   Kurulum sırasında **"Add Python to PATH"** seçeneğini işaretlemeyi unutmayın.

2. **Gerekli Kütüphanelerin Kurulumu**  
   Terminal veya Komut İstemcisine aşağıdaki komutu yazın:
   ```sh
   pip install pandas openpyxl
   ```

**Gereksinimler**
```
Python 3.x
pandas
openpyxl
```

## Klasör Yapısı
```
NumberEvaluation/
├── data/
│   └── sample_phone_number.xlsx
│
├── output/
│   ├── find_number_v1.xlsx
│   └── find_number_v2.xlsx
│
└── src/
    ├── number-scanner-v1.py
    ├── number-scanner-v2.py
    └── achievement.py
```
## Kullanım

1. **Girdi Dosyasını Hazırlayın:**  
   `data/sample_phone_number.xlsx` dosyasında, en azından `Phone Number` adında bir sütun bulunmalıdır.

2. **Telefon Numaralarını Tespit Et:**
   - V1 için:
     ```sh
     python src/number-scanner-v1.py
     ```
   - V2 için:
     ```sh
     python src/number-scanner-v2.py
     ```

   Çıktılar [output](http://_vscodecontentref_/3) klasörüne kaydedilecektir.

3. **Başarı Analizi ve Karşılaştırma:**
   ```sh
   python src/achievement.py
   ```
Bu adımda, her iki versiyonun bulduğu numaralar ile orijinal veri karşılaştırılır ve başarı oranları ekrana yazdırılır.

## Açıklamalar
1. number-scanner-v1.py:
Basit bir regex ile Türk telefon numaralarını bulur.

2. number-scanner-v2.py:
Daha esnek ve kapsamlı bir regex ile farklı formatlardaki numaraları bulur.

3. achievement.py:
Her iki versiyonun sonuçlarını karşılaştırır, normalize eder ve başarı oranlarını hesaplar.