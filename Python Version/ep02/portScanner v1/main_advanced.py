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


def connect_to(LINK):
    try:
        request = requests.get(LINK)
        print(f"Found Link at:  {request}   {LINK}")
    except:
        print(f"Found Not found  at:        {LINK}")


if __name__ == '__main__':
    link = "scanme.nmap.org:80"
    link = link_correction(LINK=link, SECURE=False, WWW=False)
    connect_to(link)
