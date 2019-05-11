import os
from OpenSSL import crypto


def certificatesExist(certificateType="PEM"):
    requiredCertificateValues = {
        "PEM": ["CERT_LOCATION"],
        "P12": ["CERT_LOCATION", "CERT_PASSPHRASE"]
    }
    requiredValuesAreSet = True
    for value in requiredCertificateValues[certificateType]:
        try:
            os.environ[value]
        except KeyError:
            requiredValuesAreSet = False
            print(f"required value {value} is not set\nset with export {value}=\"[value]\"")

    return requiredValuesAreSet


def getCertificateLocation(certificateType="PEM"):
    locationHash = {
        "PEM": "DEV_CERT_PEM",
        "P12": "CERT_LOCATION",
    }
    return os.environ[locationHash[certificateType]]


def buildCombinedCertificate(cert_location):
    p12Certificate = crypto.load_pkcs12(
        open(cert_location, 'rb').read(),
        os.environ["CERT_PASSPHRASE"]
    )
    print(p12Certificate)


# buildCombinedCertificate(os.environ["DEV_CERT_P12"])
