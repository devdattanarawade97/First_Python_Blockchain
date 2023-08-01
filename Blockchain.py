import datetime
import hashlib
import json


class Blockchain():

    # genesis block
    def __init__(self):
        self.chain = []
        self.create_blockchain(proof=1, previous_hash=0)

    # create blockchain which returns generated block

    def create_blockchain(self, proof, previous_hash):
        block = {

            'previous_hash': previous_hash,   # previous hash
            'timestamp': str(datetime.datetime.now()),  # timestamp
            'proof': proof,                            # proof
            'index': len(self.chain)+1                   # index

        }
        self.chain.append(block)
        return block

    # get previous block
    def get_previous_block(self):
        last_block = self.chain[-1]
        return last_block

    # proof of work function
    def proof_of_work(self, previous_proof):

        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2-previous_proof**2).encode()).hexdigest()
            if hash_operation[0:4] == '0000':
                check_proof = True
            else:
                new_proof = new_proof+1
        return new_proof

    # hashing block
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()


    # is chain valid
    def is_chain_valid(self, chain):
        previous_block = chain[0]

        block_index = 1
        while block_index < len(chain):

            current_block = chain[block_index]

            if current_block["previous_hash"] != self.hash(previous_block):
                return False

            previous_proof = previous_block['proof']
            current_proof = current_block['proof']
            hash_operation = hashlib.sha256(
                str(current_proof**2-previous_proof**2).encode()).hexdigest()

            if hash_operation[0:4] != '0000':
                return False

            previous_block = current_block
            block_index = block_index+1
        return True
