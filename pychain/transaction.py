from hash import hash256

class TransactionInput():
    def __init__(self, hash_prev_tx, prev_tx_index):
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
        
    def make_output(value, script = None):
        return TransactionOutput(value, script)
    
    def make_input(hash_prev_tx, prev_tx_index):
        return TransactionInput(hash_prev_tx, prev_tx_index)
        
    def get_hash(self):
        preimage = 0
        for txin in self.inputs:
            if type(txin.hash_prev_tx) is int:
                preimage += txin.hash_prev_tx
            else:
                preimage += int(txin.hash_prev_tx.decode(), 16)
            preimage += txin.prev_tx_index

        for txout in self.outputs:
            preimage += txout.value
        
        return hash256(preimage)
    
    @staticmethod
    def get_coinbase():
        coinbase = Transaction([TransactionInput(0, 0)], [TransactionOutput(50)])
        return coinbase
