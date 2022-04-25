## Creating a new virtual enviroment for python

### Create a new python env

'''
mkdir \$HOME/venvs
python3 -m venv \$HOME/venvs/pg
'''

### Activate and check binary path

'''
source \$HOME/venvs/pg/bin/activate
(pg)
which python
\$HOME/venvs/pg/bin/python
deactivate # returns to previuous version
'''

### Pipenv

'''
mkdir database && cd database
python3 install pipenv
pipenv --python python3.7
cat Pipfile
pipenv shell
pipenv install psycopg2
Pipfile.lock
exit
'''

### Create requirements.txt

'''
python3 freeze > requirements.txt
'''

### Load requirements.txt

'''
python3 install -r requirements.txt
'''
