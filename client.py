import pickle
from phe import paillier

def run_client():
    print("=== CLIENT: Initializing Keys & Encrypting ===")
    public_key, private_key = paillier.generate_paillier_keypair()

    sensitive_data = [15, 25, 35, 45]
    print(f"[Client] Sensitive Data to Process: {sensitive_data}")
    
    # Encrypt the data
    encrypted_data = [public_key.encrypt(val) for val in sensitive_data]

    # Package the public key and encrypted payload for the worker
    payload = {
        "public_key": public_key,
        "encrypted_data": encrypted_data
    }
    
    with open("payload_to_worker.pkl", "wb") as f:
        pickle.dump(payload, f)
    print("[Client] Sent encrypted payload to worker node via 'payload_to_worker.pkl'.\n")

    print("=== CLIENT: Waiting for Worker Computation... ===")
    input("Press [Enter] AFTER you have run 'python3 worker_node.py' in your second terminal...")

    # Read back results from the worker
    with open("payload_to_client.pkl", "rb") as f:
        response = pickle.load(f)
        
    encrypted_result = response["encrypted_result"]

    print("\n=== CLIENT: Decrypting Final Results ===")
    decrypted_result = [private_key.decrypt(val) for val in encrypted_result]
    print(f"[Client] Successfully Decrypted Result: {decrypted_result}")

if __name__ == "__main__":
    run_client()
