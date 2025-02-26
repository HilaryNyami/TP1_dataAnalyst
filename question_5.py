import pandas as pd



# Étape 1 : Séparer les données valides et les NaN
valid_rows = []
nan_rows = []

for index, row in df.iterrows():
    age = row['Age']
    if pd.isna(age):
        nan_rows.append(row.to_dict())  # Stocker les NaN séparément
    else:
        valid_rows.append(row.to_dict())

# Étape 2 : Implémenter le tri à bulles sur les âges valides
n = len(valid_rows)
for i in range(n):
    for j in range(0, n - i - 1):
        # Comparer les âges
        if valid_rows[j]['Age'] > valid_rows[j + 1]['Age']:
            # Échanger les lignes
            valid_rows[j], valid_rows[j + 1] = valid_rows[j + 1], valid_rows[j]

# Étape 3 : Combiner les données triées et les NaN
sorted_data = valid_rows + nan_rows

# Recréer un DataFrame à partir des données triées
df_tri = pd.DataFrame(sorted_data)
