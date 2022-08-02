import requests
import json
import os
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv
load_dotenv()

# -------------------------
# ! Important ! 
# You need to get a key from https://api.nasa.gov/
# Update the .env file with your key
# -------------------------

nasa_key = os.getenv("NASA_KEY")

# -------------------------
# Jinja2
# -------------------------

template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))
space_template = env.get_template('space.j2')

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

iss_template = env.get_template('iss.j2')
location = requests.request("GET", "http://api.open-notify.org/iss-now.json", headers=headers)
locationJSON = location.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = iss_template.render(location = locationJSON)

# -------------------------
# Save File
# -------------------------

with open("Space/ISS.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# People
# -------------------------

people_template = env.get_template('people.j2')
people = requests.request("GET", "http://api.open-notify.org/astros.json", headers=headers)
peopleJSON = people.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = people_template.render(people = peopleJSON)

# -------------------------
# Save File
# -------------------------

with open("Space/People.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Weather on Mars
# -------------------------

weatherOnMars_template = env.get_template('weatherOnMars.j2')
weatherOnMars = requests.request("GET", f"https://api.nasa.gov/insight_weather/?api_key={ nasa_key }&feedtype=json&ver=1.0", headers=headers)
weatherOnMarsJSON = weatherOnMars.json()
solChecks = weatherOnMarsJSON['validity_checks']

# -------------------------
# Template
# -------------------------

parsed_all_output = weatherOnMars_template.render(solChecks = solChecks)

# -------------------------
# Save File
# -------------------------

with open("Space/WeatherOnMars.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Astronomy Picture of the Day
# -------------------------

apod_template = env.get_template('apod.j2')
apod = requests.request("GET", f"https://api.nasa.gov/planetary/apod?api_key={ nasa_key }")
apodJSON = apod.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = apod_template.render(apod = apodJSON)

# -------------------------
# Save File
# -------------------------

with open("Space/AstronomyPhotoOfTheDay.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Asteroids Near Earth Objects 
# -------------------------

neo_template = env.get_template('neo.j2')
neo = requests.request("GET", f"https://api.nasa.gov/neo/rest/v1/feed?api_key={ nasa_key }")
neoJSON = neo.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = neo_template.render(neo = neoJSON)

# -------------------------
# Save File
# -------------------------

with open("Space/NearEarthObjects.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Coronal Mass Ejections
# -------------------------

cme_template = env.get_template('cme.j2')
cme = requests.request("GET", f"https://api.nasa.gov/DONKI/CME?api_key={ nasa_key }")
cmeJSON = cme.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = cme_template.render(cme = cmeJSON)

# -------------------------
# Save File
# -------------------------

with open("Space/CoronalMassEjections.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Geomagnetic Storm
# -------------------------

gst_template = env.get_template('gst.j2')
gst = requests.request("GET", f"https://api.nasa.gov/DONKI/GST?startDate=2021-01-01&api_key={ nasa_key }")
gstJSON = gst.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = gst_template.render(gst = gstJSON)

# -------------------------
# Save File
# -------------------------

with open("Space/GeomagneticStorms.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Interplanetary Shock
# -------------------------

ips_template = env.get_template('ips.j2')
ips = requests.request("GET", f"https://api.nasa.gov/DONKI/IPS?api_key={ nasa_key }")
ipsJSON = ips.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = ips_template.render(ips = ipsJSON)

# -------------------------
# Save File
# -------------------------

with open("Space/InterplanetaryShock.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Solar Flare
# -------------------------

flr_template = env.get_template('flr.j2')
flr = requests.request("GET", f"https://api.nasa.gov/DONKI/FLR?api_key={ nasa_key }")
flrJSON = flr.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = flr_template.render(flr = flrJSON)

# -------------------------
# Save File
# -------------------------

with open("Space/SolarFlares.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Solar Energetic Particle
# -------------------------

sep_template = env.get_template('sep.j2')
sep = requests.request("GET", f"https://api.nasa.gov/DONKI/SEP?startDate=2021-01-01&api_key={ nasa_key }")
sepJSON = sep.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = sep_template.render(sep = sepJSON)

# -------------------------
# Save File
# -------------------------

with open("Space/SolarEnergeticParticles.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Magnetopause Crossing
# -------------------------

mpc_template = env.get_template('mpc.j2')
mpc = requests.request("GET", f"https://api.nasa.gov/DONKI/MPC?api_key={ nasa_key }")
if mpc.text:
    mpcJSON = mpc.json()

# -------------------------
# Template
# -------------------------

    parsed_all_output = mpc_template.render(mpc = mpcJSON)

# -------------------------
# Save File
# -------------------------

    with open("Space/MagnetopauseCrossings.md", "w") as fh:
        fh.write(parsed_all_output)               
        fh.close()
else:
    mpcJSON = {}
# -------------------------
# Radiation Belt Enhancement
# -------------------------

rbe_template = env.get_template('rbe.j2')
rbe = requests.request("GET", f"https://api.nasa.gov/DONKI/RBE?api_key={ nasa_key }")
rbeJSON = rbe.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = rbe_template.render(rbe = rbeJSON)

# -------------------------
# Save File
# -------------------------

with open("Space/RadiationBeltEnhancements.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# High Speed Streams
# -------------------------

hss_template = env.get_template('hss.j2')
hss = requests.request("GET", f"https://api.nasa.gov/DONKI/HSS?api_key={ nasa_key }")
hssJSON = hss.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = hss_template.render(hss = hssJSON)

# -------------------------
# Save File
# -------------------------

with open("Space/HighSpeedStreams.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# WSA+EnlilSimulation
# -------------------------

wsa_template = env.get_template('wsa.j2')
wsa = requests.request("GET", f"https://api.nasa.gov/DONKI/WSAEnlilSimulations?api_key={ nasa_key }")
wsaJSON = wsa.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = wsa_template.render(wsa = wsaJSON)

# -------------------------
# Save File
# -------------------------

with open("Space/WSAEnlilSimulations.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Notifications
# -------------------------

notification_template = env.get_template('notification.j2')
notifications = requests.request("GET", f"https://api.nasa.gov/DONKI/notifications?api_key={ nasa_key }")
notificationsJSON = notifications.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = notification_template.render(notifications = notificationsJSON)

# -------------------------
# Save File
# -------------------------

with open("Space/Notifications.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Natural Events
# -------------------------

natural_template = env.get_template('natural.j2')
events = requests.request("GET", "https://eonet.gsfc.nasa.gov/api/v2.1/events")
eventsJSON = events.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = natural_template.render(events = eventsJSON)

# -------------------------
# Save File
# -------------------------

with open("Space/NaturalEvents.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Earth Polychromatic Imaging Camera
# -------------------------

epicNat_template = env.get_template('epicNat.j2')
epicNatural = requests.request("GET", f"https://api.nasa.gov/EPIC/api/natural/date?api_key={ nasa_key }")
epicNaturalJSON = epicNatural.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = epicNat_template.render(epicNatural = epicNaturalJSON)

# -------------------------
# Save File
# -------------------------

with open("Space/EPIC_Natural.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Known Celestial Body Count
# -------------------------

knownCount_template = env.get_template('knownCount.j2')
knownCount = requests.request("GET", "https://api.le-systeme-solaire.net/rest/knowncount/")
knownCountJSON = knownCount.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = knownCount_template.render(knownCount = knownCountJSON['knowncount'])

# -------------------------
# Save File
# -------------------------

with open("Space/Known_Count.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Planets
# -------------------------

planets_template = env.get_template('planets.j2')
planets = requests.request("GET", "https://api.le-systeme-solaire.net/rest/bodies?filter[]=isPlanet,eq,true")
print(planets)
planetsCountJSON = planets.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = planets_template.render(planets = planetsCountJSON['bodies'])

# -------------------------
# Save File
# -------------------------

with open("Space/Planets.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Template
# -------------------------

parsed_all_output = space_template.render(
  location = locationJSON,
  people = peopleJSON,
  solChecks = solChecks,
  apod = apodJSON,
  neo = neoJSON,
  cme = cmeJSON,
  gst = gstJSON,
  ips = ipsJSON,
  flr = flrJSON,
  sep = sepJSON,
  mpc = mpcJSON,
  rbe = rbeJSON,
  hss = hssJSON,
  wsa = wsaJSON,
  notifications = notificationsJSON,
  events = eventsJSON,
  epicNatural = epicNaturalJSON,
  knownCount = knownCountJSON['knowncount'],
  planets = planetsCountJSON['bodies']
  )

# -------------------------
# Save File
# -------------------------

with open("Space/Space.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()