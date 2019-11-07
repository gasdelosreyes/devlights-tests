# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

ui_file =  [
('main.ui', './ui/main.ui', 'DATA'),
('second.ui', './ui/second.ui', 'DATA')
]

a = Analysis(['main.py'],
             pathex=['C:\\Users\\Gaston\\projects\\Python\\devlights'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas + ui_file,
          [],
          name='Main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False)