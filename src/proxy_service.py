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


print(isProxyServerSet())
