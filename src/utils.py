import requests

def ip_address():
    """
    Gets current IP address
    """
    response = requests.get('http://www.ip-addr.es')
    print ('[-] GET {0} | {1}').format(response.status_code, response.url)


if __name__ == '__main__':
    ip_address()
    pass