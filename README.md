# DJANGO CONTACT US APPLICATION
![pypi](https://img.shields.io/pypi/v/ahlev-django-about-us) ![pypi](https://img.shields.io/pypi/status/ahlev-django-about-us)

This django application is used to show the contact us page.

## prerequisites
The instructions below assume that you have a django project already set up; and a python virtual environment already installed and activated. 

## styles
All ahlev-django applications are using styles from [mdbootstrap.com](https://mdbootstrap.com), so please make sure you install [ahlev-django-css-js](https://github.com/ohahlev/ahlev-django-css-js.git) first.


## install from this repository
### clone
```
git clone https://github.com/ohahlev/ahlev-django-contact-us.git
```

### go to directory ahlev-django-contact-us
```
cd ahlev-django-contact-us
```

### create installer package
```
python3 setup.py sdist
```

### go to project directory
```
pip install dist/ahlev-django-contact-us-0.0.1.tar.gz
```

## install from pypi
### go to the project directory and install from pypi
[ahlev-django-contact-us](https://pypi.org/project/ahlev-django-contact-us/)

## project configuration
### update settings.py as the following
```
INSTALLED_APPS = [
    'contact_us', # add this line
    ...
]
```

### add these lines to the end of settings.py if they don't exist yet
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
#STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/medias/'
```

## screenshots
### frontend: contact us page
![](screenshot/contact_us_frontend.png)
This is why django contact us applicaiton depends on [ahlev-django-location](https://github.com/ohahlev/ahlev-django-location.git)

### backend: contact us management
![](screenshot/contact_us_backend1.png)

### backend: list contact us info
![](screenshot/contact_us_backend2.png)

### backend: edit contact us info
![](screenshot/contact_us_backend3.png)
The contact us model links to the location model of [ahlev-django-location](https://github.com/ohahlev/ahlev-django-location.git)