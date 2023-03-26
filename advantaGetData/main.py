import time

import schedule as sched
from projectInfoUpdate import projectInfoUpdate
from SOAP_requests.request import makeSoapRequest

sched.every().second.do(makeSoapRequest)
sched.every().second.do(projectInfoUpdate)


if __name__ == '__main__':
    while True:
        sched.run_pending()
        time.sleep(2)
