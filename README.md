# Homework

A genomic variant web application that allows a user to search for genomic variants based on a gene name and display the results in a tabular view.
- backend - Flask, SQLite, SQLAlchemy
- frontend - ReactJS, Webpack, Babel, Bootstrap

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- pip3
- virtualenv
- npm
- all included bash scripts were executed on a Mac

### Installing

Clone this repository locally

```
git clone https://github.com/dabrau/homework
```


Install python3 dependencies

*From root folder:*
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```


Build SQLite3 db from zipped variant_results.tsv in clinvitae_download.zip

http://clinvitae.invitae.com/download 

*From root folder:*
```
./create_db.sh /path/to/clinvitae_download.zip
```


At this point the app can be run locally.

*From root folder:*
```
source venv/bin/activate
export FLASK_APP=app
flask run
```
Open http://127.0.0.1:5000 in a browser.



### Setting up front-end dev environment

Install node dependencies

*From /client folder:*
```
npm install
```

To build assets into /client/dist

*From /client folder:*
```
npm build
```

To work on a front-end only dev server localhost:8080

*From /client folder:*
```
npm start
```


## Running the tests
*From root folder:*
```
pytest
```


