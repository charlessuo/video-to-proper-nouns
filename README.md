# Video To Proper Nouns

This project is to create a web service that will take a video as input, extract its audio, run speech
recognition and find the proper nouns (names) of the transcript

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Git clone this repo to your local

(Due to the large file size of the CoreNLP libraries, they are excluded from this repo and to run the app, you need to download yourself as below)

Download CoreNLP 3.8.0 from its [official website](https://stanfordnlp.github.io/CoreNLP/download.html)

Unzip the file downloaded, and move the unziped folder into your cloned repo folder

Install Dependencies:

1. cd to the directory where requirements.txt is located
2. activate your virtualenv
3. run:

```
pip install -r requirements.txt
```

### Running the application

cd to the directory where app.py is located

```
python app.py
```

And go to web browser

```
http://localhost:5000/
```

Then input the url to the video, such as: https://www.youtube.com/watch?v=pJY0mBWHPw4
and hit Go!

Please note that as the first version, it generally takes the same amount of time as the length of the video to finish processing and tagging, so be patient while it is decoding.

To improve later, the server could be better structured to support distributed computing such that a long video can be trimmed into small trunks and mapped to serveral instances to process and reduce the results. Also a better interacting front-end will be introduced.

## Running the tests

Currently two modules can be tested with unit tests

### Test URL input validity

```
python test_urlValidator.py
```

### Test parser module

Make sure video parser runs correctly and temp directory are properly created and deleted

```
python test_parser.py
```

## Deployment

To be finished

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [CMUSphinx](https://cmusphinx.github.io/) - Speech Recognition Engine
* [Sphinxbase](https://github.com/cmusphinx/sphinxbase) - CMU Sphinx common libraries
* [PocketSphinx](https://github.com/cmusphinx/pocketsphinx) - PocketSphinx 5prealpha
* [PocketSphinx-Python](https://github.com/cmusphinx/pocketsphinx-python) - PocketSphinx Python Interface
* [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/index.html) - Named Entity Recognition Engine
* [py-corenlp](https://github.com/smilli/py-corenlp) - Python wrapper for Stanford CoreNLP

## Author

* **Chao Suo** - *Initial work* - [charlessuo](https://github.com/charlessuo)



