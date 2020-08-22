import requests 
import datetime
import threading
import time 


def main():

    print('Waiting')
    thread = threading.Thread(target=waiting)
    thread.start()
    thread.join()
    
    curtime = datetime.datetime.now()
    print(f'Screening at {curtime.hour} : {curtime.minute} : {curtime.second}')
    
    thread = threading.Thread(target=screenpass)
    thread.start()
    thread.join()
    
    print('Screening completed!')
    main()

    
def waiting():

    now = datetime.datetime.now()
    compare = datetime.datetime.now()
    compare = compare.replace(hour=8)

    if now.hour == compare.hour:
        
        return

    elif compare.hour != now.hour:
        
        sleeptime = (abs(compare.hour - now.hour) - 2) * 60 * 60 - (now.minute * 60) - now.second
        print(f'Sleeping for {sleeptime} seconds')
        time.sleep(sleeptime)


def screenpass():

    url = 'https://apps.northeaststate.edu/covidscreen/'

    fnames = ['firstname']
    lnames = ['lastnames']
    emails = ['yourname@someplace.com']

    for i, name in enumerate(fnames): 
        
        data = {
            'firstName' : name,
            'lastName' : lnames[i],
            'email' : emails[i],
            'blountville': {'1': '1'},
            'symptoms' : '0',
            'contact' : '0',
            'student' : '1'
            }
            
        time.sleep(0.5)
        print(data)

        r = requests.post(url, data=data)
        print(r.status_code)

    
if __name__ == '__main__':
    
    main()
