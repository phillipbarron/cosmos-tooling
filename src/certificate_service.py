import os


def certificatesExist():
    requiredCertificateValues = ["CERT_LOCATION", "CERT_PASSPHRASE"]
    requiredValuesAreSet = True
    for value in requiredCertificateValues:
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
