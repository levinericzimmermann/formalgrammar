from setuptools import setup

setup(
    name='formalgrammar',
    version='0.0.02',
    license='GPL',
    description='Python Module for context free formal grammar',
    author='Levin Eric Zimmermann',
    author_email='levin-eric.zimmermann@folkwang-uni.de',
    url='https://github.com/uummoo/formalgrammar',
    packages=['formalgrammar', 'formalgrammar.grammar', 'formalgrammar.utils'],
    setup_requires=[''],
    tests_require=['nosetests'],
    install_requires=[''],
    extras_require={},
    python_requires='>=3.6'
)
