from hash import hash256
import time

class BlockHeader():
    def __init__(self, hash_prev_block, hash_merkle_root, diff, nonce):
        self.hash_prev_block = hash_prev_block
        self.hash_merkle_root = hash_merkle_root
        self.time = int(time.time())
        self.difficulty = diff
        self.nonce = nonce
        self.hashid = self.get_hash()
        
    def get_hash(self):
        if self.hash_prev_block == 0:
            prev_hash = 0
        else:
            prev_hash = int(self.hash_prev_block.decode(), 16)
        
        header = prev_hash + self.hash_merkle_root + self.time + self.difficulty + self.nonce
        return hash256(header)
    
    def increment_nonce(self):
        self.nonce += 1
        self.hashid = self.get_hash()

class Block():
    def __init__(self, hash_prev_block, diff, transactions = []):
        self.transactions = transactions
        self.hash_merkle_root = 0;
        self.header = BlockHeader(hash_prev_block, self.hash_merkle_root, diff, 0)
        
    #def get_merkle_root():
        #iterate over transactions to generate a merkle root
    
    def validate(self, prev_block):
        # TODO validate a block (just does header right now)
        #      requires: previous block
        #      effect: checks hash_prev_block
        #              checks block timestamp
        #              checks proof of work
        if prev_block == 0:
            prev_hash = 0
            prev_time = 0
        else:
            prev_hash = prev_block.header.hashid
            prev_time = prev_block.header.time
        
        curr_hash = int(self.header.hashid, 16)
        return prev_hash == self.header.hash_prev_block and prev_time < self.header.time and curr_hash < (2**(256-self.header.difficulty)) 

    def contains_txid(self, txid):
        for transaction in self.transactions:
            if txid == transaction.hashid:
                return True
        return False

    def genesis_block():
        return Block(0, 0, [[], []])
