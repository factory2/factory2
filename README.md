# factory2
Factory project

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
mkdir includes
vim templates/includes/brand.html
```
```html
{% load staticfiles %}
<a class="navbar-brand" href="/">
	<img src="{% static "logos/logo.svg" %}" height="32" class="d-inline-block align-top" alt="" loading="lazy">
	<span class="text-success">Factory2</span>
</a>
```
## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
