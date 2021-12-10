from distutils.core import setup
from glob import glob
import py2exe
#D:/mygit/zanshin-wallet-windows

setup(
    console=['zanshin-wallet.py'],
    # zipfile=None,
    # data_files = [('static', glob("D:\\mygit\\zanshin-wallet-windows\\static\\*.*")), ('templates', glob("D:\\mygit\\zanshin-wallet-windows\\templates\\*.*")),('keys', glob("D:\\mygit\\zanshin-wallet-windows\\keys\\*.*")),('chain', glob("D:\\mygit\\zanshin-wallet-windows\\chain\\*.*")) ],
    options={
        "py2exe":
            {
                # "skip_archive": 1,
                # "compressed": True,
                # "bundle_files": 1,
                "packages": ['flask', 'werkzeug', 'config', 'jinja2','requests','flask_cors','json', 'uuid', 'Crypto','blockchain','createWallet','authoriseUser','signTransaction'],
                "includes": ['static','templates','keys','chain']

            }
    }

        )
