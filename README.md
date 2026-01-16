

# 🚀 Blockchain from Scratch (Python)

This project is a **complete implementation of a blockchain from scratch using Python**, built for educational and academic purposes.  
It demonstrates the **core principles of blockchain technology** without using any external blockchain frameworks.

The project includes **Proof of Work**, **mining rewards**, **transaction handling**, **fork simulation**, **performance analysis**, and **tamper detection**.

---

📌 Features

- Genesis block creation
- Block structure with cryptographic hashing (SHA-256)
- Transaction handling with fees
- Pending transaction pool (mempool concept)
- Proof of Work mining mechanism
- Mining rewards (coinbase transactions)
- Multiple miner simulation
- Blockchain validation
- Fork simulation using longest-chain rule
- Mining time performance analysis
- Tamper resistance demonstration


🧩 File Responsibilities (High-Level)
	•	block.py
Defines the structure of a block, including hashing logic.
	•	transaction.py
Defines transactions (sender, receiver, amount, fee).
	•	proof_of_work.py
Implements the Proof of Work algorithm for mining.
	•	blockchain.py
Manages the blockchain, mining, rewards, validation, and protocol rules.
	•	main.py
Runs the simulation and demonstrates the complete blockchain flow.



🔄 Blockchain Flow (Simplified)
	1.	Genesis block is created automatically
	2.	Users create transactions
	3.	Transactions go into a pending pool
	4.	Miners select transactions and perform Proof of Work
	5.	A new block is created and added to the chain
	6.	Miner receives a reward
	7.	Blockchain validates integrity
	8.	Forks are resolved using the longest-chain rule
	9.	Tampering is detected automatically



⛏️ Mining & Rewards
	•	Uses Proof of Work with adjustable difficulty
	•	Miners must find a nonce such that block hash starts with 0000
	•	Each block contains:
	•	User transactions
	•	A mining reward (coinbase transaction)
	•	Rewards incentivize miners to secure the network



🔐 Security & Validation
	•	Cryptographic hashing ensures immutability
	•	Each block references the previous block’s hash
	•	Any modification to past data invalidates the chain
	•	Validation checks:
	•	Block hash correctness
	•	Hash linkage between blocks



🔀 Fork Simulation
	•	Simulates temporary blockchain forks
	•	Applies longest-chain rule (Nakamoto Consensus)
	•	Demonstrates eventual consistency in decentralized systems

⸻

📊 Performance Analysis
	•	Measures mining time for each block
	•	Displays mining time graph
	•	Demonstrates probabilistic nature of Proof of Work





🎓 Educational Purpose

This project is intended for:
	•	Learning blockchain fundamentals
	•	Academic presentations
	•	Demonstrating protocol-level blockchain design
	•	Understanding security, incentives, and decentralization

This is not a production blockchain, but a conceptual and educational implementation.
