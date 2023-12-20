import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer




fname = "PS_2023.12.19_19.48.27.csv"
data = pd.read_csv(fname, on_bad_lines='skip')
# Convert 'releasedate' to datetime
data['releasedate'] = pd.to_datetime(data['releasedate'])
# Sort the DataFrame by 'releasedate' in descending order
sorted_data = data.sort_values(by='releasedate', ascending=False)
# Keep only the first occurrence (most recent) of each 'pl_name'
deduplicated_data = sorted_data.drop_duplicates('pl_name', keep='first')
data = deduplicated_data.sort_values(by='pl_name')
data.reset_index(drop=True, inplace=True)

# Planet Information
planet_info_columns = [
    'pl_name', 'sy_snum', 'sy_pnum', 'discoverymethod', 'disc_year',
    'disc_facility', 'soltype', 'pl_controv_flag', 'pl_refname',
    'pl_orbper', 'pl_orbsmax', 'pl_rade', 'pl_radj', 'pl_bmasse',
    'pl_bmassj', 'pl_orbeccen', 'pl_insol', 'pl_eqt', 'ttv_flag'
]

# Stellar Information
stellar_info_columns = [
    'hostname', 'st_refname', 'st_spectype', 'st_teff', 'st_rad',
    'st_mass', 'st_met', 'st_metratio', 'st_logg'
]

# System Information
system_info_columns = [
    'sy_refname', 'rastr', 'ra', 'decstr', 'dec', 'sy_dist',
    'sy_disterr1', 'sy_disterr2', 'sy_vmag', 'sy_vmagerr1',
    'sy_vmagerr2', 'sy_kmag', 'sy_kmagerr1', 'sy_kmagerr2',
    'sy_gaiamag', 'sy_gaiamagerr1', 'sy_gaiamagerr2'
]

# Temporal Information
temporal_info_columns = [
    'rowupdate', 'pl_pubdate', 'releasedate'
]

# Combine into a dictionary for easy reference
category_columns = {
    'Planet Information': planet_info_columns,
    'Stellar Information': stellar_info_columns,
    'System Information': system_info_columns,
    'Temporal Information': temporal_info_columns
}


# Check the data after preprocessing
print(data.info())
nPlanets = len(data)
print(f"Total Number of planets: {nPlanets}")

pd.set_option('display.max_rows', None)
for category, columns in category_columns.items():
    print(f"\n\n{category}\n")
    # Assuming data is your DataFrame
    df = data[columns]
    missing_values_series = pd.Series(df.isnull().sum()).sort_values(ascending=False)
    print(missing_values_series)


print(pd.reset_option('display.max_rows'))


print("TOO MUCH MISSING DATA")
