# factory2
Factory project
## Pre-installation
For ArchLinux
```bash
sudo pacman -Syu && sudo pacman -S gettext git
```
For Debian 10
```bash
sudo apt update && sudo apt-get install gettext git
```
## Installation
```bash
git clone https://github.com/factory2/factory2.git
cd factory2
git clone https://github.com/factory2/static_in_dev.git
git clone https://github.com/factory2/templates.git
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
vim factory2/settings_local.py
```
```python
SECRET_KEY = 'entersecretkey!!!!!tkekekrlud=jo8+97oo+&90i@a@4c$w1=g+iz#wup!m$_voqrepf2%s'
DEBUG = True
ALLOWED_HOSTS = ['*']
```
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Brand customization
```bash
mkdir templates/includes
vim templates/includes/brand.html
```
```html
{% load staticfiles %}
<a class="navbar-brand" href="/">
	<img src="{% static "logos/logo.svg" %}" height="32" class="d-inline-block align-top" alt="" loading="lazy">
	<span class="text-success">Factory2</span>
</a>
```
```bash
vim templates/includes/title.html
```
```html
<title>factory2</title>
```
## Compile languages
```bash
django-admin compilemessages
```

## Change logo
In the local machine
```bash
sudo scp -i /home/admin/Downloads/Key.pem /home/admin/Pictures/logo.svg admin@0.0.0.0:/home/admin/factory2/static_in_dev/logos/logo.svg
```
In the host machine
```bash
cd factory2 && source venv/bin/activate
python manage.py collectstatic
sudo systemctl restart gunicorn
sudo systemctl reload nginx
```
## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
