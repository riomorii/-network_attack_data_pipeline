import numpy as np

def build_states_for_file(df_file, features):
    print("Grouping every 10 flows into 1 state...")
    states = []
    labels = []

    # Calculate how many rows divide perfectly by 10. 
    # We drop the tiny remainder at the very end to avoid incomplete groups.
    total_rows = len(df_file)
    rows_to_keep = total_rows - (total_rows % 10)
    df_file = df_file.iloc[:rows_to_keep]

    # Step through the file in chunks of 10
    for i in range(0, rows_to_keep, 10):
        chunk = df_file.iloc[i:i+10]

        # Calculate the mathematical average (mean) of the 15 features across the 10 rows
        state_features = chunk[features].mean().values
        states.append(state_features)

        # Label priority: check all 10 labels in this chunk
        chunk_labels = chunk['Label'].unique()
        
        if 'DOS_DDOS' in chunk_labels:
            labels.append('DOS_DDOS')
        elif 'RECONNAISSANCE' in chunk_labels:
            labels.append('RECONNAISSANCE')
        else:
            labels.append('BENIGN')

    return np.array(states), np.array(labels)