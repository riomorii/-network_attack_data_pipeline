import pandas as pd
import os

def load_and_combine_files(file_paths):
    dfs = []
    for path in file_paths:
        print(f"Loading {path}...")
        df = pd.read_csv(path)
        
        # CIC-IDS2017 often has hidden spaces in column names (e.g., ' Destination Port').
        # This strips those spaces so we can call them reliably.
        df.columns = df.columns.str.strip()
        
        # Tag each row with its source file name. We will use this later to 
        # guarantee we never build a sequence that crosses two different days.
        df['file_id'] = os.path.basename(path)
        dfs.append(df)
        
    # Combine them all vertically into one big table
    return pd.concat(dfs, ignore_index=True)