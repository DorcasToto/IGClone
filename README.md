# Instagram

#### Author: [Dorcas Cherono](https://github.com/DorcasToto)


## Description
This is an application that allows users to sign up, upload pictures,view other user's pictures,like them, comment on them and also follow the other users.

## Figma design
A [link](https://www.figma.com/file/LojVD0lZuua3mac60kh1Ib/instaclone?node-id=1%3A3) to my figma design
 
## Setup and installations

* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.6 manage.py runserver`
* Access the live site using the local host provided



## Getting started

### Prerequisites
* python3.6 and above
* virtual environment
* pip3

#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/DorcasToto/IGClone
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste the following. Replace with your own values:
```
SECRET_KEY='10(tizju^09xfdu7z)ighv@6gj)4-n**9qrqjf%zmw!_npld)l'
DEBUG=True
DB_NAME='ig'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
```

#### Install dependencies
Install dependencies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py check
python manage.py makemigrations instagram
python3.6 manage.py sqlmigrate instagram 0001
python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)

        
## Built With

* [Python3.6](https://docs.python.org/3/)
* Django 3.3.1
* Postgresql 
* Boostrap4
* HTML
* CSS


### License

* LICENSED UNDER  [![License: MIT](https://github.com/DorcasToto/IGClone/blob/master/License.md)](license/MIT)