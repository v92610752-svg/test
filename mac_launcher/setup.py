from setuptools import setup

APP = ['main.py']
OPTIONS = {
    'argv_emulation': False,
    'plist': {
        'CFBundleName': 'App Launcher',
        'CFBundleDisplayName': 'App Launcher',
        'CFBundleIdentifier': 'com.example.applauncher',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
    },
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
