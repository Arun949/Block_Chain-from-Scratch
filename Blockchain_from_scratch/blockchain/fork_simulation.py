from copy import deepcopy

def simulate_fork(original_blockchain):
    # Two competing chains from same state
    chain_A = deepcopy(original_blockchain)
    chain_B = deepcopy(original_blockchain)

    return chain_A, chain_B


def resolve_fork(chain_A, chain_B):
    if len(chain_A.chain) > len(chain_B.chain):
        return chain_A
    else:
        return chain_B