from blockchain import Blockchain
from validate import validate_block

blockchain = Blockchain()

print("validate_block ", validate_block(12))


print("Starting work...")

while True:

    blockchain.mine()
    blockchain.update()
    
    print(blockchain.transactions)
    print(blockchain.get_tip().header.hashid)
