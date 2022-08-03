import requests
import json
import rich_click as click
from jinja2 import Environment, PackageLoader

# -------------------------
# Jinja2
# -------------------------
env = Environment(loader=PackageLoader("jupyter_mindmaps","Templates"))
space_template = env.get_template('space.j2')

# -------------------------
# Headers
# -------------------------
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

class Jupyter_MindMaps():
    def __init__(self,token):
        self.token = token

    def jupyter_mindmaps(self):
        self.iss_location()
        self.people_in_space()
        self.weather_on_mars()
        self.astronomy_pod()
        self.asteroids_neo()
        self.coronal_me()
        self.geomagnetic_storm()
        self.interplanetary_shock()
        self.solar_flare()
        self.solar_energetic_particle()
        self.magnetopause_crossing()
        self.radiation_belt_enhancement()
        self.high_speed_streams()
        self.wsa()
        self.notifications()
        self.natural_events()
        self.earth_polychromatic()
        self.known_celestial_body_count()
        self.planets()
        self.all_of_space()

# -------------------------
# ISS Location
# -------------------------
    def iss_location(self):
        iss_template = env.get_template('iss.j2')
        location = requests.request("GET", "http://api.open-notify.org/iss-now.json", headers=headers)
        print(f"<Status code {location.status_code} for ISS Location>")
        self.locationJSON = location.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = iss_template.render(location = self.locationJSON)

# -------------------------
# Save File
# -------------------------

        with open("ISS.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# People
# -------------------------
    def people_in_space(self):
        people_template = env.get_template('people.j2')
        people = requests.request("GET", "http://api.open-notify.org/astros.json", headers=headers)
        print(f"<Status code {people.status_code} for People In Space>")
        self.peopleJSON = people.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = people_template.render(people = self.peopleJSON)

# -------------------------
# Save File
# -------------------------

        with open("People.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Weather on Mars
# -------------------------
    def weather_on_mars(self):
        weatherOnMars_template = env.get_template('weatherOnMars.j2')
        weatherOnMars = requests.request("GET", f"https://api.nasa.gov/insight_weather/?api_key={ self.token }&feedtype=json&ver=1.0", headers=headers)
        print(f"<Status code {weatherOnMars.status_code} for Weather On Mars>")
        weatherOnMarsJSON = weatherOnMars.json()
        self.solChecks = weatherOnMarsJSON['validity_checks']

# -------------------------
# Template
# -------------------------

        parsed_all_output = weatherOnMars_template.render(solChecks = self.solChecks)

# -------------------------
# Save File
# -------------------------

        with open("WeatherOnMars.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Astronomy Picture of the Day
# -------------------------
    def astronomy_pod(self):
        apod_template = env.get_template('apod.j2')
        apod = requests.request("GET", f"https://api.nasa.gov/planetary/apod?api_key={ self.token }")
        print(f"<Status code {apod.status_code} for Astronomy Picture of the Day>")
        self.apodJSON = apod.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = apod_template.render(apod = self.apodJSON)

# -------------------------
# Save File
# -------------------------

        with open("AstronomyPhotoOfTheDay.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Asteroids Near Earth Objects 
# -------------------------
    def asteroids_neo(self):
        neo_template = env.get_template('neo.j2')
        neo = requests.request("GET", f"https://api.nasa.gov/neo/rest/v1/feed?api_key={ self.token }")
        print(f"<Status code {neo.status_code} for Asteroids Near Earth Objects>")
        self.neoJSON = neo.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = neo_template.render(neo = self.neoJSON)

# -------------------------
# Save File
# -------------------------

        with open("NearEarthObjects.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Coronal Mass Ejections
# -------------------------
    def coronal_me(self):
        cme_template = env.get_template('cme.j2')
        cme = requests.request("GET", f"https://api.nasa.gov/DONKI/CME?api_key={ self.token }")
        print(f"<Status code {cme.status_code} for Coronal Mass Ejections>")
        self.cmeJSON = cme.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = cme_template.render(cme = self.cmeJSON)

# -------------------------
# Save File
# -------------------------

        with open("CoronalMassEjections.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Geomagnetic Storm
# -------------------------
    def geomagnetic_storm(self):
        gst_template = env.get_template('gst.j2')
        gst = requests.request("GET", f"https://api.nasa.gov/DONKI/GST?startDate=2021-01-01&api_key={ self.token }")
        print(f"<Status code {gst.status_code} for Geomagetic Storms>")
        self.gstJSON = gst.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = gst_template.render(gst = self.gstJSON)

# -------------------------
# Save File
# -------------------------

        with open("GeomagneticStorms.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Interplanetary Shock
# -------------------------
    def interplanetary_shock(self):
        ips_template = env.get_template('ips.j2')
        ips = requests.request("GET", f"https://api.nasa.gov/DONKI/IPS?api_key={ self.token }")
        print(f"<Status code {ips.status_code} for Interplanetary Shock>")
        self.ipsJSON = ips.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = ips_template.render(ips = self.ipsJSON)

# -------------------------
# Save File
# -------------------------

        with open("InterplanetaryShock.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Solar Flare
# -------------------------
    def solar_flare(self):
        flr_template = env.get_template('flr.j2')
        flr = requests.request("GET", f"https://api.nasa.gov/DONKI/FLR?api_key={ self.token }")
        print(f"<Status code {flr.status_code} for Solar Flare>")
        self.flrJSON = flr.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = flr_template.render(flr = self.flrJSON)

# -------------------------
# Save File
# -------------------------

        with open("SolarFlares.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Solar Energetic Particle
# -------------------------
    def solar_energetic_particle(self):
        sep_template = env.get_template('sep.j2')
        sep = requests.request("GET", f"https://api.nasa.gov/DONKI/SEP?startDate=2021-01-01&api_key={ self.token }")
        print(f"<Status code {sep.status_code} for Solar Energetic Particle>")
        self.sepJSON = sep.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = sep_template.render(sep = self.sepJSON)

# -------------------------
# Save File
# -------------------------

        with open("SolarEnergeticParticles.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Magnetopause Crossing
# -------------------------
    def magnetopause_crossing(self):
        mpc_template = env.get_template('mpc.j2')
        mpc = requests.request("GET", f"https://api.nasa.gov/DONKI/MPC?api_key={ self.token }")
        print(f"<Status code {mpc.status_code} for Magnetopause Crossing>")
        if mpc.text:
            self.mpcJSON = mpc.json()
        else:
            self.mpcJSON = {}
# -------------------------
# Template
# -------------------------

        parsed_all_output = mpc_template.render(mpc = self.mpcJSON)

# -------------------------
# Save File
# -------------------------

        with open("MagnetopauseCrossings.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Radiation Belt Enhancement
# -------------------------
    def radiation_belt_enhancement(self):
        rbe_template = env.get_template('rbe.j2')
        rbe = requests.request("GET", f"https://api.nasa.gov/DONKI/RBE?api_key={ self.token }")
        print(f"<Status code {rbe.status_code} for Radiation Belt Enhancement>")
        self.rbeJSON = rbe.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = rbe_template.render(rbe = self.rbeJSON)

# -------------------------
# Save File
# -------------------------

        with open("RadiationBeltEnhancements.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# High Speed Streams
# -------------------------
    def high_speed_streams(self):
        hss_template = env.get_template('hss.j2')
        hss = requests.request("GET", f"https://api.nasa.gov/DONKI/HSS?api_key={ self.token }")
        print(f"<Status code {hss.status_code} for High Speed Streams>")
        self.hssJSON = hss.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = hss_template.render(hss = self.hssJSON)

# -------------------------
# Save File
# -------------------------

        with open("HighSpeedStreams.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# WSA+EnlilSimulation
# -------------------------
    def wsa(self):
        wsa_template = env.get_template('wsa.j2')
        wsa = requests.request("GET", f"https://api.nasa.gov/DONKI/WSAEnlilSimulations?api_key={ self.token }")
        print(f"<Status code {wsa.status_code} for WSA+EnlilSimulation>")
        self.wsaJSON = wsa.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = wsa_template.render(wsa = self.wsaJSON)

# -------------------------
# Save File
# -------------------------

        with open("WSAEnlilSimulations.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Notifications
# -------------------------
    def notifications(self):
        notification_template = env.get_template('notification.j2')
        notifications = requests.request("GET", f"https://api.nasa.gov/DONKI/notifications?api_key={ self.token }")
        print(f"<Status code {notifications.status_code} for Notifications>")
        self.notificationsJSON = notifications.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = notification_template.render(notifications = self.notificationsJSON)

# -------------------------
# Save File
# -------------------------

        with open("Notifications.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Natural Events
# -------------------------
    def natural_events(self):
        natural_template = env.get_template('natural.j2')
        events = requests.request("GET", "https://eonet.gsfc.nasa.gov/api/v2.1/events")
        print(f"<Status code {events.status_code} for Natural Events>")
        self.eventsJSON = events.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = natural_template.render(events = self.eventsJSON)

# -------------------------
# Save File
# -------------------------

        with open("NaturalEvents.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Earth Polychromatic Imaging Camera
# -------------------------
    def earth_polychromatic(self):
        epicNat_template = env.get_template('epicNat.j2')
        epicNatural = requests.request("GET", f"https://api.nasa.gov/EPIC/api/natural/date?api_key={ self.token }")
        print(f"<Status code {epicNatural.status_code} for Earth Polychromatic Imaging Camera>")
        self.epicNaturalJSON = epicNatural.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = epicNat_template.render(epicNatural = self.epicNaturalJSON)

# -------------------------
# Save File
# -------------------------

        with open("EPIC_Natural.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Known Celestial Body Count
# -------------------------
    def known_celestial_body_count(self):
        knownCount_template = env.get_template('knownCount.j2')
        knownCount = requests.request("GET", "https://api.le-systeme-solaire.net/rest/knowncount/")
        print(f"<Status code {knownCount.status_code} for Known Celestial Body Count>")
        self.knownCountJSON = knownCount.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = knownCount_template.render(knownCount = self.knownCountJSON['knowncount'])

# -------------------------
# Save File
# -------------------------

        with open("Known_Count.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Planets
# -------------------------
    def planets(self):
        planets_template = env.get_template('planets.j2')
        planets = requests.request("GET", "https://api.le-systeme-solaire.net/rest/bodies?filter[]=isPlanet,eq,true")
        print(f"<Status code {planets.status_code} for Planets>")
        self.planetsCountJSON = planets.json()

# -------------------------
# Template
# -------------------------

        parsed_all_output = planets_template.render(planets = self.planetsCountJSON['bodies'])

# -------------------------
# Save File
# -------------------------

        with open("Planets.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

# -------------------------
# Template
# -------------------------
    def all_of_space(self):
        parsed_all_output = space_template.render(
            location = self.locationJSON,
            people = self.peopleJSON,
            solChecks = self.solChecks,
            apod = self.apodJSON,
            neo = self.neoJSON,
            cme = self.cmeJSON,
            gst = self.gstJSON,
            ips = self.ipsJSON,
            flr = self.flrJSON,
            sep = self.sepJSON,
            mpc = self.mpcJSON,
            rbe = self.rbeJSON,
            hss = self.hssJSON,
            wsa = self.wsaJSON,
            notifications = self.notificationsJSON,
            events = self.eventsJSON,
            epicNatural = self.epicNaturalJSON,
            knownCount = self.knownCountJSON['knowncount'],
            planets = self.planetsCountJSON['bodies']
            )

# -------------------------
# Save File
# -------------------------

        with open("Space.md", "w") as fh:
            fh.write(parsed_all_output)               
            fh.close()

@click.command()
@click.option('--token',
    prompt="NASA Token",
    help="NASA Token",
    required=True, hide_input=True,envvar="TOKEN")
def cli(token):
    invoke_class = Jupyter_MindMaps(token)
    invoke_class.jupyter_mindmaps()

if __name__ == "__main__":
    cli()    