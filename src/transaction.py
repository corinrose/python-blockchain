from block import Block
from hash import hash256

class TransactionInput():
    def __init__(self, hash_prev_tx, prev_tx_index)
    self.hash_prev_tx = hash_prev_tx
    self.prev_tx_index = prev_tx_index
    

class TransactionOutput():
    def __init__(self, value, script = None):
        # script will be implemented later
        self.value = value
        self.script = script

class Transaction():
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
        self.hashid = self.get_hash()
        
        def get_hash(self):
            preimage = 0
            for txin in self.inputs:
                preimage += int(self.hash_prev_tx.decode(), 16) + self.prev_tx_index
            for txout in self.outputs:
                preimage += txout.value
            
            return hash265(preimage)
                
        
        def validate(self, chain):
            for txin in self.inputs:
                for block in chain:
                    if block.contains_txin(txin)
