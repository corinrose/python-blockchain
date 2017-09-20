from block import Block
from transaction import TransactionOutput, TransactionInput
import consensus

class Blockchain():
    def __init__(self):
        self.blocks = [Block.genesis_block()]
        self.height = len(self.blocks)
        #elf.utxo_set = self.update_utxo_set()
        
    def get_tip(self):
        return self.blocks[self.height-1]
    
    def append_block(self, block):
        if block.validate(self.get_tip()):
            self.blocks.append(block)
            return True
        else:
            return False
        
    def update(self):
        self.height = len(self.blocks)
    
    def update_utxo_set(self):
        return True
        
    def mine(self):
        consensus.start_mining(self)
