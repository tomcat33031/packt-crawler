import datetime
import os
from packt import Packt
from logs import *
from utils import ip_address, config_file
from noBookException import NoBookException
from alreadyClaimedException import AlreadyClaimedException

def main():
    now = datetime.datetime.now()
    log_info('[*] {date} - fetching today\'s eBooks'.format(date=now.strftime("%Y-%m-%d %H:%M")))
    
    packt = None

    try:
        dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.path.sep
        config = config_file(dir_path + "config\prod.cfg")
        packt = Packt(config)
        log_info(packt)

        ip_address()
        log_info('[*] Getting daily free eBook')
        try:
            packt.runDaily()
        except NoBookException as e:
            log_info('[*] ' + e.message)
        except Exception as e:
            log_debug(e)

    except KeyboardInterrupt:
        log_error('[-] Interrupted manually')
            
    except Exception as e:
        log_debug(e)

    log_info('[*] Done')

if __name__ == '__main__':
    print ("""
                      __   __                                 __         
    ____  ____ ______/ /__/ /_      ______________ __      __/ /__  _____
   / __ \/ __ `/ ___/ //_/ __/_____/ ___/ ___/ __ `/ | /| / / / _ \/ ___/
  / /_/ / /_/ / /__/ ,< / /_/_____/ /__/ /  / /_/ /| |/ |/ / /  __/ /    
 / .___/\__,_/\___/_/|_|\__/      \___/_/   \__,_/ |__/|__/_/\___/_/     
/_/                                                                      
Download FREE eBook every day from www.packtpub.com
@see github.com/tomcat33031/packt-crawler
        """)
    main()