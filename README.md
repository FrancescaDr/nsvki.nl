# NSVKI website

## Setup

Ubuntu install packages (other OS's should install similar stuff):
```bash
sudo apt-get install python3 python3-pip python-virtualenv
```

Create the virtual environment:
```bash
virtualenv venv/ -p /usr/bin/python3
. venv/bin/activate
pip install -r requirements.txt
```

Run the site with:
```bash
python run.py
```

## Changing content

If you want to make changes to the website, please fork this repository,
make your changes, and create a pull request.
