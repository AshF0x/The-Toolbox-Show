import requests

if __name__ == '__main__':
    port = 1
    while port <= 1024:
        link = "http://scanme.nmap.org"
        link = link + ":" + str(port)
        try:
            request = requests.get(link)
            print(f"Found Link at:  {request}   {link}")
        except:
            print(f"Found Not found  at:        {link}")

        port += 1
