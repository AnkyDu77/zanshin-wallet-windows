import os
import hashlib
# from zipfile import ZipFile as zf

from Crypto.PublicKey import RSA
from config import Config

def authoriseUser(password):

    """
    Gets user password and opens prKey file which suits for the password.
    Returns:
        (a) public key, private key and wallet address if password is correct;
        (b) False, False, False if password is incorrect or there is no wallets files.

    """
    fileNames = os.listdir(os.path.join(Config().BASEDIR, 'keys'))
    # # Working with ZIP
    # fileNames = []
    # with zf(Config().BASEDIR, 'r') as zip:
    #     for filename in zip.namelist():
    #         if filename.startswith("keys/"):
    #             if ".der" in filename:
    #                 fileNames.append(filename.split('/')[1])

    try:
        prKeyNames = [name for name in fileNames if name.split('_')[1] == 'prKey.der']

    except:
        return False, False, False

    for prKeyName in prKeyNames:
        try:
            with open(os.path.join(os.path.join(Config().BASEDIR, 'keys'), prKeyName), 'rb') as keyFile:
                key = RSA.import_key(keyFile.read(), passphrase=password)
            # # Working with ZIP
            # with zf(Config().BASEDIR, 'r') as zip:
            #     keyFile = zip.open(f'keys/{prKeyName}')
            # key = RSA.import_key(keyFile.read(), passphrase=password)
            prKey = key.export_key()
            pubKey = key.public_key().export_key(format='DER')

            pubHash = hashlib.sha3_224(pubKey).hexdigest()
            address = Config().IDSTR+pubHash

            return pubKey, prKey, address

        except:
            pass

    return False, False, False
