import os

def listeyi_guncelle():
    # Asistanın bakacağı odalar
    odalar = {
        "Mimari": "data/mimari",
        "Bonsai": "data/bonsai",
        "Frekans": "data/frekans"
    }
    
    rapor = "## Proje Durum Raporu\n\n"
    
    for oda_adi, yol in odalar.items():
        if os.path.exists(yol):
            dosyalar = os.listdir(yol)
            # .gitkeep dosyasını listede gösterme
            liste = [d for d in dosyalar if d != ".gitkeep"]
            
            rapor += f"### {oda_adi} ({len(liste)} Dosya)\n"
            if not liste:
                rapor += "- Bu oda henüz boş.\n"
            for d in liste:
                rapor += f"- ✅ {d}\n"
            rapor += "\n"
            
    # Bu raporu bir dosyaya yazalım ki Dashboard'da görelim
    with open("rapor.md", "w", encoding="utf-8") as f:
        f.write(rapor)
    print("Asistan: Rapor hazırlandı!")

if __name__ == "__main__":
    listeyi_guncelle()
