![Logo](/images/Jupyter.png)
# Jupyter

Mind Maps of Space

![Planets](images/planets.png)

![People In Space](images/people.png)

## Introduction 

Using various APIs Jupyter collects JSON data and then uses Jinja2 templates to create markdown files. Using the markmap VS Code extension these markdown files render as mind maps! 

## NASA API Key 

Please visit [NASA](api.nasa.gov)

And register for an API key. Once you have your key please add it to the .env file

# -------------------------
# ! Important ! 
# You need to get a key from https://api.nasa.gov/
# Put this key in the .env file
# -------------------------

.env

NASA_KEY = "your key here"

## Setup

I recommend running Jupyter in a Python virtual environment. This will help keep your host system clean and allow you to have multiple environments to try new things. If you are not using a virtual environment, start at the download/clone step below.

You will also need Python 3 and venv installed on your host system.

In your project directory, create your virtual environment
``` console
python3 -m venv env
```
Activate (use) your new virtual environment (Linux):
``` console
source env/bin/activate
```
Download or clone the mind_nmap repository:

``` console
git clone https://github.com/automateyournetwork/jupyter.git
```

## Run the code! 

```console
cd Jupyter
cd MindMaps
python3 Jupyter.py
```

## View the Mindmaps 

Install the markmap VS Code Extension

![Mark Map](images/markmap.png)

Open the markdown file and click the "Open as markmap" 

## API List
The following files are created from the various APIs. The Space.md file contains <b>all</b> APIs. 

![List](/images/API_List.png)

Original background photo credit 
[Photo](https://www.nasa.gov/audience/forstudents/k-4/dictionary/Solar_System.html)
