import time
from .block import Block
from .proof_of_work import proof_of_work


class Blockchain:
    MINING_REWARD = 10  # Mining incentive

    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        # 🔹 Upgrade additions
        self.block_times = []          # Track mining time per block
        self.miner_rewards = {}        # Track rewards per miner

        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, time.time(), [], "0")
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction.to_dict())

    def mine(self, miner_address="MINER"):
        if not self.pending_transactions:
            print("No transactions to mine")
            return False

        # ⛏ Coinbase transaction (mining reward)
        reward_tx = {
            "sender": "NETWORK",
            "receiver": miner_address,
            "amount": self.MINING_REWARD
        }
        self.pending_transactions.append(reward_tx)

        new_block = Block(
            index=self.last_block.index + 1,
            timestamp=time.time(),
            transactions=self.pending_transactions,
            previous_hash=self.last_block.hash
        )

        # ⏱ Measure mining time
        start_time = time.time()
        proof = proof_of_work(new_block)
        end_time = time.time()

        new_block.hash = proof
        self.chain.append(new_block)
        self.pending_transactions = []

        # Save mining statistics
        self.block_times.append(end_time - start_time)
        self.miner_rewards[miner_address] = \
            self.miner_rewards.get(miner_address, 0) + self.MINING_REWARD

        return new_block

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.compute_hash():
                return False

            if curr.previous_hash != prev.hash:
                return False

        return True

    # 🔍 Visualization of blockchain structure
    def visualize_chain(self):
        print("\n🧱 Blockchain Structure")
        for block in self.chain:
            print(f"[Block {block.index}]")
            print(f"  Hash      : {block.hash[:12]}...")
            print(f"  Prev Hash : {block.previous_hash[:12]}...\n")

    # 📊 Blockchain statistics
    def chain_stats(self):
        return {
            "total_blocks": len(self.chain),
            "total_transactions": sum(len(b.transactions) for b in self.chain),
            "chain_valid": self.is_chain_valid()
        }