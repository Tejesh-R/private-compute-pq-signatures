import pickle

def run_worker():
    print("=== WORKER NODE: Ingesting Payload ===")
    with open("payload_to_worker.pkl", "rb") as f:
        payload = pickle.load(f)
        
    encrypted_data = payload["encrypted_data"]
    print("[Worker Node] Ingested ciphertexts successfully.")
    print("[Worker Node] NOTE: Private key is absent from this environment (Zero-Trust).")

    print("[Worker Node] Executing homomorphic addition (adding scalar 10)...")
    # Blind computation on ciphertexts
    encrypted_result = [val + 10 for val in encrypted_data]

    # Package response back to client
    response = {
        "encrypted_result": encrypted_result
    }
    
    with open("payload_to_client.pkl", "wb") as f:
        pickle.dump(response, f)
        
    print("[Worker Node] Computation complete. Result saved to 'payload_to_client.pkl'.")

if __name__ == "__main__":
    run_worker()
