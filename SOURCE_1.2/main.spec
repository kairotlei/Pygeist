# -*- mode: python ; coding: utf-8 -*-

from kivy_deps import sdl2, glew

block_cipher = None


a = Analysis(['main.py'],
             pathex=["C:\\Users\\jason\\Documents\\zla\\", "C:\\Users\\jason\\Documents\\zla\\kv"],
             binaries=[],
             datas=[
			 ('C:\\Users\\jason\\Documents\\zla\\res\\*.*', 'res' ),
			 ('C:\\Users\\jason\\Documents\\zla\\py\\*.*', 'py' ),
			 ('C:\\Users\\jason\\Documents\\zla\\kv\\*.*', 'kv' )],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=["cv2", "gfortran", "libopenblas", "enchant"],
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
          a.datas,  
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )