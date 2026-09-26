import os
import json
import numpy as np
from data_loader import load_and_combine_files
from preprocess import clean_data
from feature_engineering import get_15_features
from state_builder import build_states_for_file
from sequence_builder import build_sequences

def main():
    # 1. Ensure folders exist
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)

    # 2. Load data
    files = [
        "data/raw/Monday-WorkingHours.pcap_ISCX.csv",
        "data/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
        "data/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv"
    ]
    df = load_and_combine_files(files)

    # 3. Preprocess data (cleaning only, NO scaling)
    features = get_15_features()
    df = clean_data(df, features)

    all_X = []
    all_y = []

    # 4. Process each file independently so sequences do not cross over boundaries
    for file_id in df['file_id'].unique():
        print(f"\n--- Processing boundaries for: {file_id} ---")
        df_file = df[df['file_id'] == file_id]

        # Build 10-flow states
        states, labels = build_states_for_file(df_file, features)

        # Build 5-state sequences
        X, y = build_sequences(states, labels)

        all_X.append(X)
        all_y.append(y)

    # 5. Combine and Save final unscaled outputs
    final_X = np.concatenate(all_X)
    final_y = np.concatenate(all_y)

    print("\n--- FINAL PIPELINE REPORT ---")
    print(f"X Data Shape (Unscaled): {final_X.shape}") 
    print(f"y Label Shape: {final_y.shape}") 
    
    np.save('data/processed/X_sequences.npy', final_X)
    np.save('data/processed/y_labels.npy', final_y)

    with open('outputs/feature_names.json', 'w') as f:
        json.dump(features, f)

    print("Success! Unscaled data successfully saved to data/processed/")

if __name__ == "__main__":
    main()