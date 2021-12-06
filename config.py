import os
import hashlib

from Crypto.PublicKey import RSA

class Config():

    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    MINING_COMPLEXITY = "0"
    IDSTR = 'z01x00'
    MINEADDR = 'z01x0000000000000000000000000000000000000000000000000000000000'

    NATIVE_TOKEN_NAME = 'zsh'
    MIN_COMISSION = 1
    MAX_CHAIN_SIZE = 2831155
    REQUIRED_TX_FIELDS = ['sender', 'type']
    REQUIRED_TX_TYPE = ['common', 'trade']

    DEFAULT_VALID_NODES = ['localhost:5001']
    DEFAULT_HOST = 'localhost'
    DEFAULT_PORT = '5000'

    UPLOAD_FOLDER = os.path.join(BASEDIR, 'chain')

    REMOTE_NODES = ['https://zanshin-node.ngrok.io', 'http://localhost:5001', 'http://localhost:5002']
