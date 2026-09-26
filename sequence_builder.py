import numpy as np

def build_sequences(states, labels):
    print("Building sequences: 5 states input -> 6th state target...")
    X = []
    y = []

    # Stop 5 steps before the end so we always have a 6th state to predict
    for i in range(len(states) - 5):
        sequence_X = states[i:i+5] # Grabs states [0,1,2,3,4]
        target_y = labels[i+5]     # Grabs state [5]

        X.append(sequence_X)
        y.append(target_y)

    return np.array(X), np.array(y)