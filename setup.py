from setuptools import setup, find_packages


setup(
    name='twdump',
    version='0.0.1',
    description='Dump twitter top words',
    author='Dmi Baranov',
    author_email='dmi.baranov@gmail.com',
    packages=find_packages(),
    install_requires=[
    	'gevent >= 1.0rc2', 'requests',
    	'requests-oauthlib', 'numpy', 'pyyaml', 'nltk'],
    dependency_links=['http://gevent.googlecode.com/files/gevent-1.0rc2.tar.gz'],
)