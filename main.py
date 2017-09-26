#!/usr/bin/python3

from pychain import Blockchain, Transaction

blockchain = Blockchain()

# test comment

print("Starting work...")

while True:

    blockchain.mine()
    
    cur_block = blockchain.get_tip()
    coinbase = cur_block.transactions[0]
    
    newtx = Transaction([Transaction.make_input(coinbase.hashid, 0)], [Transaction.make_output(50)])
    
    blockchain.update([newtx])

        
    print(blockchain.get_tip().header.hashid)
    
