import block, threading

def hash_worker(blockchain):
    prev_block = blockchain[len(blockchain)-1]
    new_block = block.Block(prev_block.header.get_hash(), prev_block.header.difficulty)
    while True:
        if new_block.validate(prev_block):
            break
        else:
            new_block.header.increment_nonce()
    blockchain.append(new_block)
        

def start_mining(blockchain):
    thread = threading.Thread(target=hash_worker, args=(blockchain, ))
    thread.start()
