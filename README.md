# NumberEvaluation

Bu proje, bir Excel dosyasındaki telefon numaralarını tespit etmek ve farklı algoritmaların başarı oranlarını karşılaştırmak için geliştirilmiştir.

## 🚀 Kurulum ve Çalıştırma
1. **Projeyi Klonla**
```sh
git clone https://github.com/melekbaygin/NumberEvaluation.git
cd NumberEvaluation
```
## 📂 Çıktılar Hakkında

Projeyi klonladıktan sonra scriptleri çalıştırmak istemeyen veya kurulum adımlarıyla uğraşmak istemeyen kullanıcılar için, **önceden üretilmiş sonuç dosyaları** `output/` klasörü altında hazır olarak bulunmaktadır.  

Bu dosyalar şunlardır:  
- `find_number_v1.xlsx` → Version 1 algoritması tarafından tespit edilen telefon numaraları  
- `find_number_v2.xlsx` → Version 2 algoritması tarafından tespit edilen telefon numaraları  
- `analysis_report.xlsx` → Version 1 ve Version 2 sonuçlarının karşılaştırmalı başarı metrikleri

Böylece projeyi derinlemesine incelemek isteyen kullanıcılar kurulum yapmadan doğrudan `output/` klasöründeki dosyalardan sonuçları analiz edebilirler.

## Excel Formulu 

=COUNTIF(C2:C99999,"<>") : C2 ile C99999 arasındaki boş olmayan hücreleri sayar.

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

## ⚠️ Önemli Not
Karşılaştırma scripti (`achievement.py`) çalıştırılmadan **önce** aşağıdaki adımlar yapılmalıdır:

1. `number_scanner_v1.py` çalıştır → `output/find_number_v1.xlsx` oluşturur.  
2. `number_scanner_v2.py` çalıştır → `output/find_number_v2.xlsx` oluşturur.  
3. Son olarak `achievement.py` çalıştır → bu dosyaları ve `data/sample_phone_number.xlsx` dosyasını kullanarak başarı oranlarını hesaplar.  

Eğer 1 ve 2. adımlar yapılmadan doğrudan `achievement.py` çalıştırılırsa, gerekli dosyalar bulunamayacağı için hata alırsınız.

## Klasör Yapısı
```
NumberEvaluation/
 ├── data/
 │    └── sample_phone_number.xlsx
 │
 ├── output/
 │    ├── find_number_v1.xlsx
 │    ├── find_number_v2.xlsx
 │    └── analysis_report.xlsx
 │
 └── src/
      ├── number-scanner-v1.py
      ├── number-scanner-v2.py
      ├── achievement.py

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