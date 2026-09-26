import pandas as pd
import numpy as np

def map_labels(label):
    # Convert label to lowercase text to avoid capitalization errors
    label = str(label).strip().lower()
    
    if label == 'benign':
        return 'BENIGN'
    elif 'dos' in label or 'ddos' in label: 
        return 'DOS_DDOS'
    elif 'portscan' in label:
        return 'RECONNAISSANCE'
    return 'DROP' 

def clean_data(df, features_to_keep):
    print("Mapping attack labels...")
    df['Label'] = df['Label'].apply(map_labels)
    
    # Remove rows that didn't match our 3 categories
    df = df[df['Label'] != 'DROP'].copy()

    print("Cleaning missing or invalid numbers...")
    # Convert Infinity (inf) values to NaN, then drop all NaNs in the required columns
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(subset=features_to_keep, inplace=True)

    return df