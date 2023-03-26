import requests
from config import SOAP_URL

def makeSoapRequest():
    #headers = {'content-type': 'application/soap+xml'}
    headers = {'content-type': 'text/xml'}
    with open('SOAP_requests/requestBodies/TestBodyRequest.xml', 'r')\
            as body_xml:
        body = body_xml.read()
        with open('STORAGE/GetExample.xml', 'w') as getExample:
            getExample.write(requests.request("POST", SOAP_URL, headers=headers,
                                              data=body).text)
