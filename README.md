$ git clone url

$ virtualenv --no-site-packages twdump_sandbox

$ cd twdump_sandbox/ && source bin/activate

$ pip install -e ../twdump

$ python -m twdump.run

...

$ deactivate

$ cd .. && rm -rf twdump_sandbox

