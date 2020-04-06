import threading

import requests


def connect_to(LINK, ONLY_WORKING=True, PORT=0):
    link2 = LINK + ":" + str(PORT)
    try:
        request = requests.get(link2)
        print(f"Found Link at:  {request}   {link2}")
        return None
    except:
        if ONLY_WORKING:
            print(f"Found Not found  at:    {link2}")
        return None


if __name__ == "__main__":
    link = "http://scanme.nmap.org"
    threads = 1

    links = []
    for i in range(threads):
        thread = threading.Thread(target=connect_to(LINK=link, ONLY_WORKING=False, PORT=i))
        links.append(thread)

    # Start the threads
    for l in links:
        l.start()

    # Ensure all of the threads have finished
    for l in links:
        l.join()
