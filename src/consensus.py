def validate_chain(chain):
    for block in chain:
        if block.validate() == False:
            return False
    return True
