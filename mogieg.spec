# -*- mode: python ; coding: utf-8 -*-
# MogiEgg 단일 실행 파일(onefile) 빌드 스펙
# 빌드: pyinstaller --clean --noconfirm mogieg.spec  ->  dist/MogiEgg(.exe)

a = Analysis(
    ['gui.py'],
    pathex=[],
    binaries=[],
    datas=[('templates', 'templates'), ('static', 'static')],
    hiddenimports=['server'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='MogiEgg',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,      # 콘솔 창 없이 깔끔하게 실행
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
