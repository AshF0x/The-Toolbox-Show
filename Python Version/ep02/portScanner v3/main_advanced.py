import threading

import requests


def link_correction(LINK, SECURE_CONNECTION=True, WWW=False):
    if "www." not in LINK and "http" in LINK and WWW == True:
        if SECURE_CONNECTION:
            LINK = LINK.replace("https://", "http://www.")
        else:
            LINK = LINK.replace("http://", "http://www.")

    if "www." not in LINK and WWW == True:
        LINK = "www." + LINK

    if "http" not in LINK:
        if SECURE_CONNECTION:
            LINK = "https://" + LINK
        else:
            LINK = "http://" + LINK

    return LINK


def connect_to(LINK, ONLY_WORKING=True):
    try:
        request = requests.get(LINK)
        print(f"Found Link at:  {request}   {LINK}")
    except:
        if ONLY_WORKING:
            print(f"Found Not found  at:        {LINK}")


def find_ports(LINK, MAX_PORT=1024):
    if ":" in LINK:
        LINK = LINK.split(":")
        LINK = str(LINK[0]) + ":" + str(LINK[1])
    port = 1

    while port <= MAX_PORT:
        connect_to(str(LINK + ":" + str(port)))
        port += 1


def find_ports_turbo(LINK, THREADS, ONLY_WORKING):
    links = []
    for i in range(THREADS):
        thread = threading.Thread(target=connect_to(LINK=LINK, ONLY_WORKING=ONLY_WORKING))
        links.append(thread)

    # Start the threads
    for l in links:
        l.start()

    # Ensure all of the threads have finished
    for l in links:
        l.join()


if __name__ == '__main__':
    link = "scanme.nmap.org:"
    link = link_correction(LINK=link, SECURE_CONNECTION=False, WWW=False)
    find_ports_turbo(LINK=link, THREADS=1, ONLY_WORKING=False)
