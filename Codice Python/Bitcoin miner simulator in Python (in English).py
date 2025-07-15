import hashlib

NONCE_LIMIT=int(input("Enter the maximum number of attempts to find a valid hash (the higher the number, the longer it will take) (e.g., 1000000 for a quick test, 100000000000 for a real scenario): "))
zeroes_limit=int(input("How many leading zeros should the hash have to be considered valid? (The higher the number, the harder the difficulty) (e.g., 2 for an easy test, 6 for a more challenging computation): "))
block_number=int(input("Enter the block number. This is a unique identifier for the block in the blockchain (e.g., 24 for a test block, 100000 for a real blockchain scenario): "))
transactions=str(input("Enter the transaction data. This represents the transactions included in the block, written as a single string (e.g., '123abc' for a simple transaction, 'tx1_tx2_tx3' for multiple transactions separated by underscores): "))
previous_hash=str(input("Enter the previous block's hash. This is the unique hash of the previous block, ensuring the integrity of the chain (e.g., '0000abcd1234' for a simple hash, 'f3a5c6d7e8b9...' for a real blockchain hash): "))

def bitcoin_mining(block_number, transactions, previous_hash):
    global numberhashesfound
    valid_hashes_found_count=0 # Count the total number of valid hashes found
    for nonce in range(NONCE_LIMIT): # Iterate over possible nonce values up to the limit
        base_text=str(block_number)+transactions+previous_hash+str(nonce)
        hash_attempt=hashlib.sha256(base_text.encode()).hexdigest() # Generate the SHA-256 hash
        if hash_attempt.startswith("0"*zeroes_limit): # Check if the hash meets the difficulty target
            valid_hashes_found_count+=1 # Increment the counter for valid hashes
            print(f"The number of hashes found with the nonce is: {nonce}")
            numberhashesfound=nonce
            print(f"The valid hash found is: {hash_attempt}") # Display the hash that meets the required difficulty level
    print(f"The total number of valid hashes found is: {valid_hashes_found_count}")

bitcoin_mining(block_number, transactions, previous_hash)

combined_text=str(block_number)+transactions+previous_hash+str(numberhashesfound) # Create the data string to calculate the block's SHA-256 hash
final_hash_block=hashlib.sha256(combined_text.encode()).hexdigest() # Calculate the final SHA-256 hash of the block
print(f"The SHA-256 hash of the mined block is: {final_hash_block}")
print()
program_exit=input("Press ENTER to exit the program...")