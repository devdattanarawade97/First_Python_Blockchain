
from flask import Flask, jsonify

from Blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()


@app.route("/mine_block", methods=["GET"])
def mine_block():

    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    block = blockchain.create_blockchain(proof, previous_hash)
    response = {

        'message': 'Block mined!',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']

    }
    return jsonify(response), 200


@app.route("/get_chain", methods=["GET"])
def get_chain():
    response = {

        'chain': blockchain.chain,
        'length': len(blockchain.chain)

    }
    return jsonify(response), 200


@app.route("/is_blockchain_valid",methods=["GET"])
def is_blockchain_valid():

    valid = blockchain.is_chain_valid(blockchain.chain)

    if valid:
        response = {'message': 'Yes, Blockchain is valid'}

    else:
        response = {'message': 'No , Blockchain is invalid'}

    return jsonify(response), 200


app.run(host="0.0.0.0", port=5000)
