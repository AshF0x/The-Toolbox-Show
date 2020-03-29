import requests

if __name__ == '__main__':
    link = "http://scanme.nmap.org:80"

    try:
        request = requests.get(link)
        print(f"Found Link at:  {request}   {link}")
    except:
        print(f"Found Not found  at:        {link}")
