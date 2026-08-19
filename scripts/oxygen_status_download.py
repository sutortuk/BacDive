import json
import bacdive
import pandas as pd
client = bacdive.BacdiveClient()
sp_list = []
with open("data/species.txt", "r", encoding="utf-8") as f:
    for line in f:
        tur_adi = line.strip()
        if tur_adi:
            sp_list.append(tur_adi)

rows = []

for sp in sp_list:
    client.search(taxonomy = sp)
    all_data = list(client.retrieve())
    
    for i in range(len(all_data)):
        tur = all_data[i].get("Name and taxonomic classification").get("species")
        phy = all_data[i].get("Physiology and metabolism")
        
        if phy is not None and "oxygen tolerance" in phy:
            oxy_raw = all_data[i].get("Physiology and metabolism").get("oxygen tolerance")
            
            if isinstance(oxy_raw, list):
                degerler = [item.get("oxygen tolerance") for item in oxy_raw if isinstance(item, dict) and item.get("oxygen tolerance")]
                oxy = ", ".join(set(degerler))
            elif isinstance(oxy_raw, dict):
                oxy = oxy_raw.get("oxygen tolerance")
            elif isinstance(oxy_raw, str):
                oxy = oxy_raw
            else:
                oxy = None
            
            if tur and oxy:
                strain_dict = {
                    "species": tur,
                    "oxygen_tolerance": oxy
                }
                rows.append(strain_dict)

son_tablo = pd.DataFrame(rows)
son_tablo.to_csv("data/tum_bakteriler_oxygen_tablosu.csv", index=False, encoding="utf-8-sig")
print(son_tablo)
