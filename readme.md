
# Cephalometric Ai analysis Web App

This is a web application for cephalometric analysis automated using ai for detecting landmarks and start analysis .


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [File Structure](#file-structure)
- [How It Works](#how-it-works)
- [Examples](#examples)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The goal is to create a web app that can be used by the clinicians and researchers in order to analyze their data.

## Features
- User authentication: users can create accounts, log in.
- Upload X-ray img.
- detect cephalometric landmark automated with Ai.
- Display the detected landmarks on the image.
- make user able to change posisition of any detected landmarks.
- make user able to add new landmarks.
- start analysis and show results.
- save analysis results in database


## Files Structure
```bash
    ├── ai_model
    │   ├── weights
    │   │   ├── best3.pt
    │   │   └── best_small.pt
    │   ├── detect.py
    │   ├── extract.py
    │   └── utils.py
    ├── cephalometric
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── main
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── user
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── media
    │   ├── images
    ├── readme_images
    ├── requirements.txt
    ├── README.md
    └── LICENSE
```

- `ai_model/`: 
    - `weights/`: contains the trained models.
    - `detect.py`: contains the code for detecting landmarks.
    - `extract.py`: contains the code for extracting the landmarks.
    - `utils.py`: contains the code for the utility functions.
- `cephalometric/`: contains the settings for the Django project.
- `main/`: contains the code for the main app.
- `user/`: contains the code for the user app.
- `media/`: contains the uploaded images.
- `readme_images/`: contains the images used in the readme file.
- `requirements.txt`: contains the required packages to run the project.
- `README.md`: contains the readme file.
- `LICENSE`: contains the license file.


## How It Works
- The user uploads an image.
- The image is sent to the server.
- The server runs the model on the image.
- the model that used here is yolov8 to detect landmarks and trained on custom dataset.
- The server returns the detected landmarks.
- displays the detected landmarks on the image.

## Examples
![site](readme_images/video.gif)


## Installation
Clone the repository:

```bash
$ git clone https://github.com/m7mdGNo/cephalometric.git
$ cd cephalometric
```

### Create a virtual environment and activate it:

```bash
$ python3 -m venv env
$ source env/bin/activate
```

### Install the dependencies:

```bash
$ pip install -r requirements.txt
```

### create postgres database
```bash
$ sudo apt-get install python3-dev libpq-dev postgresql postgresql-contrib
$ sudo su - postgres
$ psql
$ create database <database_name>;
$ create role <name> with encrypted password <'password'>;
$ alter role <name> with LOGIN;
$ grant all on DATABASE <db_name> to <role_name>;
```

### Create a .env file in the root directory with the following environment variables:

see .env.example in the root directory and replace these values with real values
```makefile
SECRET_KEY=secret-key
DEBUG=True
DATABASE_URL=psql://postgres:<password>@localhost:<password>/<db_name>
STATIC_URL=/static/
STATIC_ROOT=static/
MEDIA_URL=/media/
MEDIA_ROOT=media/
ALLOWED_HOSTS=*
```
### Run the migrations:

```Copy code
$ python manage.py migrate
```

### Run the development server:

```Copy code
$ python manage.py runserver
```

Open the web browser and go to http://localhost:8000.

### create administrator user
```Copy code
$ python manage.py createsuperuser
```

Open the web browser and go to http://localhost:8000/admin.


## Usage
- Register a new user account or log in as an existing user.
- click on "start analysing with ai" button
- upload x-ray image
- click on "detect points with Ai" button
- you can add new points with the name of this point by clicking "add points" button
- you can change position of any point by clicking on it and drag it to new position
- you can reset the posision of all point by clicking on "reset" button
- save the results with detected points and patient name in database from "save" button
- in admin panel you can see your patients with landmarks posistions



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.