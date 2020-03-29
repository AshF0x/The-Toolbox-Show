import requests


def link_correction(LINK, SECURE=True, WWW=False):
    if "www." not in LINK and "http" in LINK and WWW == True:
        if SECURE:
            LINK = LINK.replace("https://", "http://www.")
        else:
            LINK = LINK.replace("http://", "http://www.")

    if "www." not in LINK and WWW == True:
        LINK = "www." + LINK

    if "http" not in LINK:
        if SECURE:
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


if __name__ == '__main__':
    link = "scanme.nmap.org:"
    link = link_correction(LINK=link, SECURE=False, WWW=False)
    find_ports(LINK=link, MAX_PORT=1024)
