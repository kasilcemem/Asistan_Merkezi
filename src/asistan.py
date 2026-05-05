import os
import shutil

# 1. HEDEFLERİ BELİRLE (Odalarımız)
MIMARI_YOL = "data/mimari"
BONSAI_YOL = "data/bonsai"
GELEN_KUTUSU = "gelen_kutusu" # Buraya gelenleri asistan ayıklayacak

def asistan_ayikla():
    # Eğer gelen kutusu yoksa oluştur
    if not os.path.exists(GELEN_KUTUSU):
        os.makedirs(GELEN_KUTUSU)
        print("Gelen kutusu oluşturuldu. Dosyalarını oraya atabilirsin.")
        return

    # Gelen kutusundaki dosyaları tara
    dosyalar = os.listdir(GELEN_KUTUSU)
    
    for dosya in dosyalar:
        dosya_adi = dosya.lower()
        eski_yol = os.path.join(GELEN_KUTUSU, dosya)
        
        # AKILLI AYIRMA MANTIĞI
        if "mimari" in dosya_adi or ".dwg" in dosya_adi:
            yeni_yol = os.path.join(MIMARI_YOL, dosya)
            shutil.move(eski_yol, yeni_yol)
            print(f"✅ {dosya} -> Mimari klasörüne yerleştirildi.")
            
        elif "bonsai" in dosya_adi or "agac" in dosya_adi:
            yeni_yol = os.path.join(BONSAI_YOL, dosya)
            shutil.move(eski_yol, yeni_yol)
            print(f"✅ {dosya} -> Bonsai notlarına eklendi.")
            
        else:
            print(f"❓ {dosya} için ne yapacağımı bilemedim, dokunmuyorum.")

if __name__ == "__main__":
    asistan_ayikla()
