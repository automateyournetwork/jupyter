import requests
import json

# -------------------------
# Jinja2
# -------------------------
from jinja2 import Environment, FileSystemLoader
template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))
iss_template = env.get_template('iss.j2')

# -------------------------
# Headers
# -------------------------
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

# -------------------------
# Location
# -------------------------
location = requests.request("GET", "http://api.open-notify.org/iss-now.json", headers=headers)
locationJSON = location.json()

# -------------------------
# Location
# -------------------------
people = requests.request("GET", "http://api.open-notify.org/astros.json", headers=headers)
peopleJSON = people.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = iss_template.render(
  location = locationJSON,
  people = peopleJSON  
  )

# -------------------------
# Save File
# -------------------------

with open("International_Space_Station.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()