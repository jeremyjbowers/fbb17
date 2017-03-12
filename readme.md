# FBB 2017

## Getting started
```
git clone git@github.com:jeremyjbowers/fbb17.git && cd fbb17
mkvirtualenv fbb17 && pip install -r requirements.txt
./get.sh
./load.sh
python scrape.py
```

## Secrets
You need to have a `secrets.py` that defines a few constants:
* `secrets.YAHOO_COOKIE`: Should be a dictionary with all of the keys / values matching your session cookie from Yahoo.
