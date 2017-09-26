import block, threading

def hash_worker(blockchain):
    prev_block = blockchain.get_tip()
    new_block = block.Block(prev_block.header.get_hash(), prev_block.header.difficulty, blockchain.mempool)
    while True:
        if blockchain.append_block(new_block):
            break
        else:
            new_block.header.increment_nonce()
        

def start_mining(blockchain):
    thread = threading.Thread(target=hash_worker, args=(blockchain, ))
    thread.start()
