import block, proofofwork, consensus

blockchain = [block.Block(0, 0)]

print("Starting work...")

while True:
    
    print(len(blockchain), blockchain[len(blockchain)-1].header.hashid)
    proofofwork.start_mining(blockchain)
    #print(blockchain)
