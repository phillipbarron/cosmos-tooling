# Cosmos tooling

Like logging on the cosmos services? Then you'll *love* this.

## Usage

### log in to a cosmos-deployed instance

```bash
./cosmos.py [component] [environment]
```

## Requires

location of BBC dev cert exported

```bash
export DEV_CERT_PEM=/path/to/unencrypted/combined/cert
```

* Python 3
* pyOpenSSL
* requests

```bash
pip3 install pyOpenSSL requests
```

### todo

* create dev cert PEM builder / exporter - could just run the bash script here right?
* look at how pipenv works across OSs and update install instructions accoridingly - we'd like a single install command - this sucks a bit :/
* add an .ssh config checker or at least a link to the .ssh instructions
* look at https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df for ideas regarding cli
* have it work for p12 / PEM

### example alias

```bash
pythonLogin(){
  $HOME/workspace/cosmos-tooling/cosmos.py $2 $1 $3
}

alias cssh='$HOME/workspace/cosmos-tooling/cosmos.py'

alias issh='pythonLogin $1 int $2'
alias tssh='pythonLogin $1 test $2'
alias lssh='pythonLogin $1 live $2'
```
