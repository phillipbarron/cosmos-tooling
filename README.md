# cosmos-tooling

## usage

### log in to a cosmos deployed ec2 instance

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

```bash
pip3 install pyOpenSSL
```

### todo

* look at aliasing (like Nate's [issh, tssh, lssh])
* create dev cert PEM builder / exporter
* find and use testing library
* look at how pipenv works across OSs and update install istructions accoridingly
* perhaps looks at integration with VDT (basically a node implementation) - could event extend the cosmos CLI verison