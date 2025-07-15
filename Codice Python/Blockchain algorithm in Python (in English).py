# Importing the necessary library
import hashlib

# Creating a block class
class Block:
    # Creating a constructor for the block class
    def __init__(self, data, previous_hash):
        self.data=data
        self.previous_hash=previous_hash
        self.hash=self.calculate_hash()
    # Creating a method to calculate hash using SHA-256 encryption system
    def calculate_hash(self):
        sha=hashlib.sha256() # SHA-256 = Secure Hash Algoritm 256 bit
        sha.update(self.data.encode("utf-8")) # Transform the data in a Unicode format in 8 bit
        return sha.hexdigest() # Returns the hash of a given input as a hexadecimal string

# Creating a blockchain class
class Blockchain:
    # Creating a constructor for the blockchain class
    def __init__(self):
        self.chain=[] # Initialize the blockchain block list
        self.chain.append(self.genesis_block()) # Insert the genesis block as the first one
    # Creating a method to creates the "Genenis block", meaning what is the first block of a blockchain
    def genesis_block(self):
        return Block("The genesis block", "0")
    # Creating a method to create a new block and adds it to for the blockchain (the list)
    def add_new_block(self, data):
        previous_block=self.chain[-1]
        new_block=Block(data, previous_block.hash)
        self.chain.append(new_block)
        
# Testing the blockchain
blockchain=Blockchain()

# Adding data to the blockchain
def num_data_blocks_blockchain():
    # Adding a specific number of blocks to the blockchain
    num_input_blocks=int(input("How many blocks do you want to add to the blockchain: "))
    print()
    # Entering individual data for each block
    for i in range(num_input_blocks):
        data=input(f"Enter the data for the block number {i+1}: ")
        blockchain.add_new_block(data)
    print()

# Counting the number of blocks present in the blockchain
def count_blocks_blockchain():
    num_tot_blocks=0
    for block in blockchain.chain:
        num_tot_blocks=num_tot_blocks+1
    print(f"In this blockchain there is/are in total {num_tot_blocks} block(s): (1 genesis block + {num_tot_blocks-1} normal block(s))")

# Printing all the elements of each block of the blockchain
def block_element_info_blockchain():
    i=-1
    print(f"In this blockchain there is/are the block(s):")
    print()
    for block in blockchain.chain:
        i+=1
        print(f"The block number {i} is composed of:")
        print(f"The data is: {block.data}")
        print(f"The previuos hash is: {block.previous_hash}")
        print(f"The hash of the block is: {block.hash}")
        print()

# Execution of all created functions
def final_blockchain():
    num_data_blocks_blockchain()
    block_element_info_blockchain()
    count_blocks_blockchain()
    print()
    input("Press Enter to exit the program... ")

# Executing the final summary function of the other functions
final_blockchain()