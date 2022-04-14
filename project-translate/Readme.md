# google_trans_new

## Github repo

https://github.com/lushan88a/google_trans_new

## The module changed the name from googletrans to google_trans_new

```
pip3 install google_trans_new
```

## Workaround

The module has a bug to decode json and you have to fix manually by doing:

```
Change line 151 in google_trans_new/google_trans_new.py which is: response = (decoded_line + ']') to response = decoded_line
```

https://stackoverflow.com/questions/68214591/python-google-trans-new-translate-raises-error-jsondecodeerror-extra-data

## Required modules

```
import json, requests, random, re
```

## Command example

The command bellow will print both text - translated 'pt' and original 'en'

```
for i in `cat files/subtitle_test.srt | grep "^[a-z]"`; do  python ../main.py "${i}" ; echo " | ${i}" ; done
```
