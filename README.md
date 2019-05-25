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
* we need a dev cert PEM builder / exporter
* find and use testing library
* look at how pipenv works across OSs and update install istructions accoridingly
