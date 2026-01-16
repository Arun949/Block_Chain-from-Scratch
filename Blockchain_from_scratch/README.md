# Blockchain from Scratch

This project demonstrates a basic blockchain protocol implemented from scratch using Python.

## Features
- Block creation
- SHA-256 hashing
- Proof of Work
- Transaction pool
- Chain validation


🧱 Blockchain From Scratch (Upgraded Implementation)

📌 Project Description

This project is an educational implementation of a blockchain protocol built completely from scratch using Python.
Instead of using existing blockchain frameworks, we implemented the core protocol mechanisms manually to understand how blockchains work internally.

The project demonstrates:
	•	How blocks are structured
	•	How cryptographic hashing ensures immutability
	•	How Proof of Work (PoW) provides security
	•	How transactions are grouped and confirmed
	•	How miners are incentivized
	•	How tampering is detected

This project is not a cryptocurrency, but a protocol-level simulation designed for learning and academic purposes.

⸻

🎯 Project Objectives
	•	Understand the internal architecture of a blockchain
	•	Implement Proof of Work consensus from scratch
	•	Demonstrate trustless verification without a central authority
	•	Show how economic incentives secure a blockchain
	•	Simulate attacks and observe blockchain immutability

⸻

📁 Project Structure

Blockchain_from_scratch/
│
├── blockchain/
│   ├── __init__.py
│   ├── block.py              # Block structure and hashing
│   ├── blockchain.py         # Core blockchain logic
│   ├── proof_of_work.py      # Proof of Work algorithm
│   └── transaction.py        # Transaction model
│
├── main.py                   # Demo & execution script
└── README.md                 # Project documentation


⸻

🧩 Core Components Explained

⸻

1️⃣ Block (block.py)

Each block represents a single unit in the blockchain.

Block attributes:
	•	index – Position of the block in the chain
	•	timestamp – Time at which the block is created
	•	transactions – List of confirmed transactions
	•	previous_hash – Hash of the previous block
	•	nonce – Value used for Proof of Work
	•	hash – SHA-256 hash of the block contents

Key concept:
The block hash is computed without including the hash field itself, ensuring deterministic validation and preventing hash recursion errors.

⸻

2️⃣ Transaction (transaction.py)

A transaction represents a transfer of value.

Transaction attributes:
	•	sender
	•	receiver
	•	amount

Transactions are first stored in a pending transaction pool and become permanent only after a block is mined.

⸻

3️⃣ Proof of Work (proof_of_work.py)

Proof of Work (PoW) is the consensus mechanism used to secure the blockchain.

How PoW works:
	•	A miner must find a nonce such that the block hash starts with a fixed number of leading zeros
	•	This requires computational effort
	•	Verification of the solution is fast and easy

Purpose of PoW:
	•	Prevents spam
	•	Prevents tampering
	•	Protects against Sybil attacks

⸻

4️⃣ Blockchain (blockchain.py)

The Blockchain class manages the entire protocol logic.

Responsibilities:
	•	Create the genesis block
	•	Maintain the blockchain
	•	Store pending transactions
	•	Mine new blocks
	•	Validate the blockchain

⸻

🚀 Protocol Upgrades Implemented

⸻

✅ Upgrade 1: Mining Rewards (Coinbase Transaction)

Motivation

In real blockchains, miners are rewarded for securing the network.
Without incentives, miners would have no reason to participate honestly.

Implementation
	•	A fixed mining reward is defined in the blockchain protocol
	•	Each mined block includes a coinbase transaction:
	•	sender = "NETWORK"
	•	receiver = miner address
	•	amount = mining reward

Result
	•	Introduces economic incentives
	•	Makes the protocol closer to real-world blockchains like Bitcoin

⸻

✅ Upgrade 2: Blockchain Validation

Every node can independently verify the blockchain.

Validation checks:
	•	Block hash integrity
	•	Correct previous hash linkage

Outcome:
	•	Any modification to a block invalidates the entire chain

⸻

⚠️ Tampering Attack Demonstration

To demonstrate immutability, the project includes a simulated attack.

Attack:
	•	Modify a transaction in a previously mined block

Result:
	•	Blockchain validation fails immediately

This proves that historical data cannot be altered without redoing Proof of Work for all subsequent blocks.

⸻

▶️ Execution Flow (main.py)

The main script demonstrates the following:
	1.	Blockchain initialization
	2.	Transaction creation
	3.	Block mining with rewards
	4.	Blockchain state printing
	5.	Blockchain validation
	6.	Tampering attack simulation
	7.	Re-validation to show failure

⸻

🧪 Example Output (Simplified)

⛏ Mining block by Miner-1...
⛏ Mining block by Miner-2...

Block # 1
Transactions:
[
  {'sender': 'Alice', 'receiver': 'Bob', 'amount': 50},
  {'sender': 'Bob', 'receiver': 'Charlie', 'amount': 25},
  {'sender': 'NETWORK', 'receiver': 'Miner-1', 'amount': 50}
]

Blockchain valid? True
⚠️ Tampering with blockchain...
Blockchain valid after attack? False


⸻

🧠 Key Blockchain Concepts Demonstrated

Concept	Implemented
Blocks & hashing	
Proof of Work	
Mining process	
Incentive mechanism	
Immutability	
Tamper detection	
Decentralized verification	


⸻

⚠️ Limitations

This project is designed for learning purposes, so the following are not included:
	•	Peer-to-peer networking
	•	Digital signatures
	•	Wallet balance tracking
	•	Transaction fees
	•	Difficulty adjustment
	•	Scalability optimizations

⸻

📌 Learning Outcomes

Through this project, we gained:
	•	Deep understanding of blockchain internals
	•	Practical experience implementing consensus mechanisms
	•	Insight into economic security in distributed systems
	•	Hands-on knowledge of immutability and cryptographic trust

⸻

🏁 Conclusion

This project demonstrates how trustless systems can be built using cryptography, computation, and incentives.
By incrementally upgrading a basic blockchain, we achieved a realistic and educational protocol implementation.
