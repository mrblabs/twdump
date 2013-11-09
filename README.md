$ git clone <url>

$ virtualenv --no-site-packages twdump_sandbox

$ cd twdump_sandbox/ && source bin/activate

$ pip install -e ../twdump

$ python -c "import nltk;nltk.download('maxent_treebank_pos_tagger');"

$ python -m twdump.run

...

$ deactivate

$ cd .. && rm -rf twdump_sandbox

$ rm -rf ~/nltk_data
