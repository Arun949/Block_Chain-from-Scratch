from blockchain.blockchain import Blockchain
from blockchain.transaction import Transaction
from copy import deepcopy
import matplotlib.pyplot as plt


def main():
    # 1. Initialize Blockchain
    
    blockchain = Blockchain()

    miners = ["Miner-1", "Miner-2", "Miner-3"]

    transactions = [
        ("Alice", "Bob", 50),
        ("Bob", "Charlie", 25),
        ("Charlie", "Dave", 10),
        ("Dave", "Eve", 12),
        ("Eve", "Frank", 30),
        ("Frank", "Alice", 20),
    ]

    print("\n🚀 Starting blockchain mining simulation...\n")


    for i, (sender, receiver, amount) in enumerate(transactions):
        blockchain.add_transaction(Transaction(sender, receiver, amount))
        miner = miners[i % len(miners)]
        print(f"⛏ Mining block by {miner}...")
        blockchain.mine(miner_address=miner)

 
    print("\n📦 Final Blockchain State")
    for block in blockchain.chain:
        print(f"\nBlock #{block.index}")
        print("Hash:", block.hash)
        print("Previous Hash:", block.previous_hash)
        print("Transactions:", block.transactions)

   
    blockchain.visualize_chain()

    # ===============================
    # 5. Validate Blockchain
    # ===============================
    print("\n✅ Blockchain valid?", blockchain.is_chain_valid())

    # ===============================
    # 6. Miner Reward 
    # ===============================
    print("\n💰 Miner Reward Summary")
    print("----------------------")
    for miner, reward in blockchain.miner_rewards.items():
        print(f"{miner}: {reward} coins")

    # ===============================
    # 7. Block Time Graph
    # ===============================
    print("\n📊 Displaying block mining time graph...")
    plt.plot(blockchain.block_times, marker="o")
    plt.xlabel("Block Number")
    plt.ylabel("Mining Time (seconds)")
    plt.title("Block Mining Time")
    plt.show()

    # ===============================
    # 8. Fork Simulation
    # ===============================
    print("\n🔀 Simulating blockchain fork...")

    chain_A = deepcopy(blockchain)
    chain_B = deepcopy(blockchain)

    # Chain A mines 2 extra blocks
    chain_A.add_transaction(Transaction("Alice", "Bob", 1))
    chain_A.mine(miner_address="Miner-A")

    chain_A.add_transaction(Transaction("Bob", "Charlie", 1))
    chain_A.mine(miner_address="Miner-A")

    # Chain B mines 1 extra block
    chain_B.add_transaction(Transaction("Charlie", "Dave", 1))
    chain_B.mine(miner_address="Miner-B")

    # Longest chain wins
    winner = chain_A if len(chain_A.chain) > len(chain_B.chain) else chain_B
    print("🏆 Longest chain selected with length:", len(winner.chain))

    # ===============================
    # 9. Tampering Attack
    # ===============================
    print("\n⚠️ Tampering with blockchain (attack simulation)...")
    blockchain.chain[2].transactions[0]["amount"] = 9999
    print("❌ Blockchain valid after attack?", blockchain.is_chain_valid())


if __name__ == "__main__":
    main()