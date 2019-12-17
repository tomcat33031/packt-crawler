import requests
import os , sys, itertools
import configparser
from logs import *
from bs4 import BeautifulSoup
from time import sleep
from clint.textui import progress

def ip_address():
    """
    Gets current IP address
    """
    response = requests.get('https://api.ipify.org?format=json')
    print ('[-] GET {0} | {1}'.format(response.status_code, response.url))
    log_success('  [+] Ip address is : {0}'.format(response.text.strip()))

def config_file(path):
    """
    Reads configuration file
    """
    if not os.path.exists(path):
        raise IOError('File configuation not found !')

    log_success('[*] Configuration file : {0}'.format(path))
    config = configparser.ConfigParser()
    config.read(path)
    return config

def make_soup(response, debug=False):
    """
    Makes soup from response
    """
    print('[*] fetching url... {0} | {1}'.format(response.status_code, response.url))
    soup = BeautifulSoup(response.text)
    if debug:
        print(type(soup))
        print(soup.prettify().encode('utf-8'))
    return soup

def wait(delay, isDev):
    if delay > 0:
        if isDev:
            print('[-] going to sleep  {0} seconds'.format(delay))
            sleep(delay)

def download_file(r , url , directory, filename, headers):
    """
    Downloads file with progress bar
    """
    if not os.path.exists(directory):
        # Creates directories recursively
        os.makedirs(directory)
        log_success('[+] create new dir : {0}'.format(directory))

    filename = filename.replace(':','-')
    path = os.path.join(directory, filename)

    print('[-] Downloading file from url: {0}'.format(url))
    response = r.get(url, headers = headers , stream = True)
    log_success(response.headers)
    total_length = 0
    test_length = response.headers.get('Content-length')
    if test_length is not None:
        total_length = int(test_length)
    with open(path, 'wb') as f:
        for chunk in progress.bar(response.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()
    log_success('[+] New download {0}'.format(path))

def thread_loader(function):
    """
    Starts a thread with loading bar
    """

    thread = Thread(target=function)
    thread.start()
    spinner = itertools.cycle(['-', '/', '|', '\\'])
    while thread.is_alive():
        sys.stdout.write(spinner.next())
        sys.stdout.flush()
        # erase the last written char
        sys.stdout.write('\b')    

if __name__ == '__main__':
    #config_file("C:\\Users\\ntvanh4\\Desktop\\packt-crawler\\config")
    #ip_address()
    #wait(10, 1)
    #make_soup(requests.get('https://api.ipify.org?format=json'),debug=True)
    #download_file(requests,"https://codeload.github.com/niqdev/packtpub-crawler/zip/master"
    #                    ,"C:\\Users\\ntvanh4\\Desktop\\packt-crawler\\config","abc.pdf", {})
    pass