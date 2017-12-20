from setuptools import setup

import lookupindict

setup(
    name=lookupindict.__title__,
    version=lookupindict.__version__,
    description='Look up a word/phrase from dict.cn and save it locally',
    packages=['lookupindict'],
    include_package_data=True,
    zip_safe=False,
    author=lookupindict.__author__,
    author_email=lookupindict.__author_email__,
    url='http://github.com/lixia/lookupindict',
    license=lookupindict.__license__,
    platforms=['any'],
    keywords=[
        'look up',
        'word',
        'phrase',
        'dictionary'
    ],
    install_requires=['requests', 'bs4'],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Development Status :: testing',
        'Operating System :: linux ',
        'Topic :: Look up a word or a phrase'
    ],
    long_description='''\
Look up a word or a phrase from dict.cn and save it a local place.
''',
    entry_points={
        'console_scripts': [
            'lookupindict = lookupindict.main:main',
        ]
    },
)
