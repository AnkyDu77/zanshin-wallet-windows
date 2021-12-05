from distutils.core import setup
import py2exe

dataFiles = [('\static', '\templates')]

setup(
    console=['zanshin-wallet.py'],
    data_files = dataFiles,
    options={
        "py2exe":
            {
                "packages": ['flask', 'werkzeug', 'config', 'jinja2','requests','flask_cors','json', 'uuid', 'Crypto','blockchain','createWallet','authoriseUser','signTransaction'],

            }
    }

        )
