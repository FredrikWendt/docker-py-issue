#!/usr/bin/env bash

set -e

if [ ! -d .venv ] ; then
    virtualenv --distribute --no-site-packages .venv
    source .venv/bin/activate
    pip install -r requirements.txt
else
    source .venv/bin/activate
fi

if [ -f issue.tar ] ; then rm issue.tar ; fi
if [ -d untarred ] ; then rm -rf untarred ; fi
mkdir untarred

./issue.py
