from blockchain import Blockchain

blockchain = Blockchain()

print("Starting work...")

while True:

    blockchain.mine()
    blockchain.update()
    print(blockchain.height)
    print(blockchain.get_tip().header.hashid)
