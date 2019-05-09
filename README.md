# cosmos-tooling

## usage

### log in to a cosmos deployed ec2 instance

```bash
cosmos.py [component] [environment]
```

## Requires

location of BBC dev cert set

Python 3

### todo

* add proxy support - needs dict - create proxies module for checking env value - see https://stackoverflow.com/questions/8287628/proxies-with-python-requests-module
* look at aliasing (like Nate's [issh, tssh, lssh])
* we need a dev cert PEM builder / exporter - do this next & revisit the logic in the cert_service cause it's wrong
