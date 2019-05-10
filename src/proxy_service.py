import os

proxyServerEnvironmentKeys = [
    "http_server",
    "https_server",
    "HTTTP_SERVER",
    "HTTTPS_SERVER",
]


def isProxyServerSet():
    for value in proxyServerEnvironmentKeys:
        if value in os.environ:
            return True
    return False


def getProxies():
    proxies = {}
    for value in proxyServerEnvironmentKeys:
        if value in os.environ:
            proxies[value] = os.environ[value]
    return proxies
