# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['D:/mygit/zanshin-wallet-windows/zanshin-wallet.py'],
             pathex=[],
             binaries=[],
             datas=[('D:/mygit/zanshin-wallet-windows/templates', 'templates/'), ('D:/mygit/zanshin-wallet-windows/static', 'static/')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='zanshin-wallet',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='D:\\mygit\\zanshin-wallet-windows\\zsh.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='zanshin-wallet')
