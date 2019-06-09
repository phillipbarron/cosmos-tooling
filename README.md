# cosmos-tooling

## usage

### log in to a cosmos-deployed ec2 instance

```bash
cosmos.py [component] [environment]
```

## Requires

location of BBC dev cert exported

```bash
export CERT_LOCATION=/path/to/unencrypted/combined/cert
```

* Python 3
* pyOpenSSL
* requests

```bash
pip3 install pyOpenSSL requests
```

### build executable

```bash
pyinstaller --onefile -n cssh cosmos.py
```

### todo

* look at aliasing (like Nate's [issh, tssh, lssh])
* create dev cert PEM builder / exporter
* find and use testing library
* look at how pipenv works across OSs and update install istructions accoridingly - we'd like a single install command - this sucks a bit
* add an .ssh config checker or at least a link to the .ssh instructions
* look at https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df for ideas regarding cli
