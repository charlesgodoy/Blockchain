import hashlib
import requests
import json
import blockchain

import sys


# TODO: Implement functionality to search for a proof 

def proof_of_work(block):
        """
        Simple Proof of Work Algorithm
        Find a number p such that hash(last_block_string, p) contains 6 leading
        zeroes
        :return: A valid proof for the provided block
        """
        # TODO
        block_string = json.dumps(block, sort_keys=True).encode()

        proof = 0
        while blockchain.valid_proof(block_string, proof) is False:
            proof += 1

        return proof


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server and look for a new one
        r1 = requests.get(url = node + '/last_block').json()['last_block']
        new_proof = proof_of_work(r1)

        post_proof = {'proof': new_proof}
        r2 = requests.post(url = node + '/mine', json = post_proof)

        # TODO: When found, POST it to the server {"proof": new_proof}
        # TODO: We're going to have to research how to do a POST in Python
        # HINT: Research `requests` and remember we're sending our data as JSON
        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        if r2.json()['message'] == 'New Block Forged':
            coins_mined += 1
            print(r2.json()['message'])
            print ("Coins = " + coins_mined)
        pass