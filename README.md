# Welcome to my 'Project Fletcher' repo!   

For this project at Metis, I used unsupervised learning with non-negative matrix factorization, Word2Vec, Markov chains, Flask, and HTML/CSS to create a web app that allows the user to find similar articles to a given input. Users can also play with a random press release generator that creates press releases for select topics using a Markov chain generator.

#### [Web App Demo](https://drive.google.com/open?id=1nC9EIgTvhmlAQ6HY3sIBLLNa6A2MD0TX)

In this repo, I've uploaded my code and the presentation I gave at Metis on this project.  
  
Blog post is currently a work in progress.
  
## Repo Contents:   

### Data
* All data is available on [Kaggle].

### Data Exploration and Cleaning
* [doj_eda.py](https://github.com/maddyobrienjones/project_fletcher/blob/master/doj_eda.py) - some light data cleaning and data exploration
  
### Modeling
* [nmf_testing.ipynb](https://github.com/maddyobrienjones/project_fletcher/blob/master/nmf_testing.ipynb) - Testing of non-negative matrix factorization
* [topic_building.ipynb](https://github.com/maddyobrienjones/project_fletcher/blob/master/topic_building.ipynb) - Final topic modeling using non-negative matrix factorization
* [taxes.ipynb](https://github.com/maddyobrienjones/project_fletcher/blob/master/taxes.ipynb) - Topic modeling for tax topic only to see if it can be broken down into further subtopics
* [w2v.ipynb](https://github.com/maddyobrienjones/project_fletcher/blob/master/w2v.ipynb) - Building and examining word vectors for potential bias

### Web App Building
* [flaskapp.py](https://github.com/maddyobrienjones/project_fletcher/blob/master/flaskapp.py) - Flask app to look up relevant press releases and generate random press releases
* [testing_for_web_app.ipynb](https://github.com/maddyobrienjones/project_fletcher/blob/master/testing_for_web_app.ipynb) - Notebook building and testing functions for use in Flask app
* [generator.ipynb](https://github.com/maddyobrienjones/project_fletcher/blob/master/generator.ipynb) - Building rough generator for random press releases using Markov chains
* [page.html](https://github.com/maddyobrienjones/project_fletcher/blob/master/page.html) - First page of Flask app (search bar)
* [template2.html](https://github.com/maddyobrienjones/project_fletcher/blob/master/template2.html) - Page for list of relevant press releases
* [article.html](https://github.com/maddyobrienjones/project_fletcher/blob/master/article.html) - Page for randomly generated press releases

### Presentation
* [doj_presentation.pdf](https://github.com/maddyobrienjones/project_fletcher/blob/master/doj_presentation.pdf) - Powerpoint presentation given at Metis
* [Web App Demo](https://drive.google.com/open?id=1nC9EIgTvhmlAQ6HY3sIBLLNa6A2MD0TX) - Demonstration of Flask app

[Kaggle]: https://www.kaggle.com/jbencina/department-of-justice-20092018-press-releases/kernels
