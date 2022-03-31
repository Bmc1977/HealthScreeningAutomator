import requests

url = "https://webapps.alma.edu/daily-health-screening/submit-screening"
data = {
   "experiencing-symptoms":"No",
   "contact-or-travel":"No"
}

x = requests.post(url, data = data)

print(str(x))