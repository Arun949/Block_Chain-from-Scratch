import time

DIFFICULTY = 4
TARGET_TIME = 5  # seconds per block (educational)

def proof_of_work(block):
    global DIFFICULTY

    block.nonce = 0
    start_time = time.time()
    computed_hash = block.compute_hash()

    while not computed_hash.startswith("0" * DIFFICULTY):
        block.nonce += 1
        computed_hash = block.compute_hash()

    elapsed_time = time.time() - start_time

    # Difficulty adjustment
    if elapsed_time < TARGET_TIME:
        DIFFICULTY += 1
    elif DIFFICULTY > 1:
        DIFFICULTY -= 1

    return computed_hash