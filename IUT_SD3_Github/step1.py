import pandas as pd 

veh = pd.read_csv('data/veh.csv', sep=";", error_bad_lines=False)
vict = pd.read_csv('data/vict.csv', sep=";", error_bad_lines=False)
lieux = pd.read_csv('data/lieux.csv', sep=";", error_bad_lines=False)
carac = pd.read_csv('data/carac.csv', sep=";", error_bad_lines=False)

merged = pd.merge(veh, vict, on='Num_Acc', how='outer') 
merged = pd.merge(merged, lieux, on='Num_Acc', how='outer') 
merged = pd.merge(merged, carac, on='Num_Acc', how='outer') 

merged.to_csv('data/merged_data.csv', index=False)
