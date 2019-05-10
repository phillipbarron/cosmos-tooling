# cosmos-tooling

## usage

### log in to a cosmos deployed ec2 instance

```bash
cosmos.py [component] [environment]
```

## Requires

location of BBC dev cert set

```bash
export CERT_LOCATION=/path/to/unencrypted/combined/cert
```

Python 3

### todo

* look at aliasing (like Nate's [issh, tssh, lssh])
* we need a dev cert PEM builder / exporter - do this next & revisit the logic in the cert_service cause it's wrong
