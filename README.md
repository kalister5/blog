# Blog

An app that allows users to use that one minute wisely . The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them .

## Author name

Abdullahi Mohamaud .

## Project description

An app that allows users to use that one minute wisely . The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them .

## Technology used

I used HTML to develop the skeleton of the application .I used python to make the website functional so that people are able to input information and get feedback .

Target Audience-Everyone.

## Known bugs

So far no identified bugs but if you get any contact me on [email](zainkalister@gmail.com).

## Contact information

if anyone has question or wants to contribute to the project the please contact me through #0796303066 or at [email](zainkalister@gmail.com) .

# Project setup installation

## Prerequisites

- Python 3.6
- Ubuntu software

## Create a Virtual Environment

## Install dependancies

Install dependancies that will create an environment for the app to run

pip3 install -r requirements

Install Postgres

## Prepare environment variables

export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitches'

export SECRET_KEY='Your secret key'


## Run Database Migrations

python manage.py db init

python manage.py db migrate -m "initial migration"

python manage.py db upgrade

## Running the app in development

In the same terminal type: python3 manage.py server

Open the browser on http://localhost:5000/

## Behavior Driven Development

|Behavior|input|output|
|--------|-----|------|
|Sign up .| Enter email and password . | Sign in successful .|
| Log in .| Enter email and password .|  Login successful .|
|  comment  .| Enter comment and click post button .| comment published successful .|


## Licence

MIT licence. Copyright (c) 2018 Abdillahi mohamud .
   .
