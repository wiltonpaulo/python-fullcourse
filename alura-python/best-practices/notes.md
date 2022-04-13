## PEP8 useful information

[PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

## Install and configure git to lock commits with flake8 errors

```
pip install flake8
flake8 --install-hook git
git config--bool flake8.strict true
```
