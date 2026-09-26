def get_15_features():
    # The exact 15 numeric columns you specified
    return [
        "Destination Port", "Flow Duration", "Total Fwd Packets",
        "Total Backward Packets", "Total Length of Fwd Packets",
        "Total Length of Bwd Packets", "Fwd Packet Length Mean",
        "Bwd Packet Length Mean", "Flow IAT Mean", "Flow IAT Std",
        "SYN Flag Count", "ACK Flag Count", "Average Packet Size",
        "Init_Win_bytes_forward", "Active Mean"
    ]