import requests
import json

# -------------------------
# Jinja2
# -------------------------
from jinja2 import Environment, FileSystemLoader
template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))
iss_template = env.get_template('space.j2')

# -------------------------
# Headers
# -------------------------
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

nasa_key = ''

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
# Weather on Mars
# -------------------------
weatherOnMars = requests.request("GET", f"https://api.nasa.gov/insight_weather/?api_key={ nasa_key }&feedtype=json&ver=1.0", headers=headers)
weatherOnMarsJSON = weatherOnMars.json()
sol = weatherOnMarsJSON['sol_keys'][0]
solDetails = weatherOnMarsJSON[sol]
solChecks = weatherOnMarsJSON['validity_checks']

# -------------------------
# Template
# -------------------------

parsed_all_output = iss_template.render(
  location = locationJSON,
  people = peopleJSON,
  sol = sol,
  solDetails = solDetails,
  solChecks = solChecks
  )

# -------------------------
# Save File
# -------------------------

with open("Space.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()