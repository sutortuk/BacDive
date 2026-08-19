import json
import bacdive
import pandas as pd
client = bacdive.BacdiveClient()
sp_list = ["Bacillus subtilis"]

rows = []

for sp in sp_list:
    client.search(taxonomy = sp)
    all_data = list(client.retrieve())
    for i in range(len(all_data)):
        tur = all_data[i].get("Name and taxonomic classification").get("species")
        phy = all_data[i].get("Physiology and metabolism")
        
        if phy is not None and "oxygen tolerance" in phy:
            oxy = all_data[i].get("Physiology and metabolism").get("oxygen tolerance")
            if isinstance(oxy, dict):
                oxy = oxy.get("oxygen tolerance")
            
            if tur and oxy:
                print(tur, oxy)
                
                strain_dict = {
                    "species": tur,
                    "oxygen_tolerance": oxy
                }
                rows.append(strain_dict)

son_tablo = pd.DataFrame(rows)
print(son_tablo.head())
son_tablo.to_csv("bacdive_subtilis_tablo.csv", index=False, encoding="utf-8-sig")
