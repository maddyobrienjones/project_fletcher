#necessary imports
import flask
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.decomposition import NMF
import string
import unidecode
import re
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import random

#nmf model to transform input into search box
with open('nmf.pkl','rb') as f:
    nmf = pickle.load(f)

#referencing matrix values for each press release to find most similar by cosine similarity
with open('doj_transformed.pkl','rb') as f:
    X = pickle.load(f)

#dictionaries for use with Markov chain generator
with open('imdict.pkl', 'rb') as f:
    imm = pickle.load(f)
with open('offshore.pkl', 'rb') as f:
    oa = pickle.load(f)
with open('access.pkl', 'rb') as f:
    acc = pickle.load(f)
with open('ocean.pkl', 'rb') as f:
    ocean = pickle.load(f)
with open('vets.pkl', 'rb') as f:
    vets = pickle.load(f)
with open('elections.pkl', 'rb') as f:
    elec = pickle.load(f)
with open('realestate.pkl', 'rb') as f:
    realestate = pickle.load(f)
with open('ht.pkl', 'rb') as f:
    ht = pickle.load(f)
with open('fraud.pkl', 'rb') as f:
    fraud = pickle.load(f)
with open('drugs.pkl', 'rb') as f:
    drugs = pickle.load(f)

#mapping generator dictionaries to options used in dropdown
gendicts = {
    "Immigration": imm,
    "Offshore Accounts": oa,
    "Accessibility": acc,
    'Maritime Issues/Ocean Pollution/Wildlife': ocean,
    "Veterans": vets,
    "Elections": elec,
    "Real Estate": realestate,
    "Human Trafficking": ht,
    "Fraud": fraud,
    "Drugs": drugs
}

#importing raw articles
articles = pd.read_csv('topics.csv')

#tokenizer to use with tf-idf vectorizer to put data in the right format
def customtokenizer(article):
    punc = str.maketrans('','',string.punctuation+"''``''``\"")
    article_c = article.translate(punc)
    dig = str.maketrans('','',string.digits)
    article_c=article_c.translate(dig)
    article_c = unidecode.unidecode(article_c)
    article_c = article_c.lower()
    regex = re.compile(r'(?u)\b\w\w+\b')
    article_c = re.findall(regex,article_c)
    stop_words = stopwords.words('english')
    article_c = [y for y in article_c if y not in stop_words]
    stemmer = SnowballStemmer('english')
    article_c = [stemmer.stem(y) for y in article_c]
    return article_c

#pre-trained tf-idf vectorizer
with open('vectorizer.pkl','rb') as f:
    vectorizer = pickle.load(f)

#simple rough Markov chain generator
def quotegen(prdict):
    generated = []
    generated.append(random.choice(list(prdict.keys())))
    while len(generated) < 500:
        key = generated[-1]
        generated.append(random.choice(prdict[key]))
    quote = generated[0].capitalize() + ' ' + ' '.join(generated[1:]) + '.'
    return quote

#topic names for use when detecting relevant topics from search bar input
topicnames = {
    1: 'Criminal Trials',
    2: 'Taxes',
    3: 'Benefits',
    4: 'Discrimination',
    5: 'Child Pornography',
    6: 'Environment',
    7: 'Terrorism',
    8: 'Market Regulation',
    9: 'Immigration',
    10: 'Prisoners',
    11: 'Civil Trials',
    12: 'Accessibility',
    13: 'Corruption',
    14: 'Whistleblowers',
    15: 'Drugs',
    16: 'Fraud',
    17: 'White Collar Crime',
    18: 'Elections',
    19: 'Consumer Issues',
    20: 'Native Americans',
    21: 'Real Estate',
    22: 'Human Trafficking',
    23: 'Veterans',
    24: 'Maritime Issues/Ocean Pollution/Wildlife',
    25: 'Offshore Accounts',
}

# Initialize the app
app = flask.Flask(__name__)

# Homepage
@app.route("/")
def viz_page():
    topics = ['Accessibility','Elections','Human Trafficking','Immigration','Maritime Issues/Ocean Pollution/Wildlife','Offshore Accounts','Veterans','Topics']
    return flask.render_template('page.html',topics=topics)


# Return similar articles
@app.route("/score", methods=["POST"])
def score():
    rec = flask.request.get_data()
    #cleaning and tranforming input into something that can be compared to existing articles
    rec = rec.decode('utf-8')
    rec = rec.split('=')[1].replace('+',' ')
    vec = vectorizer.transform([rec])
    mat = nmf.transform(vec)
    title = "Relevant articles for \"" + rec + "\""
    #finding most relevant topic for input
    topic = topicnames[mat.argmax()+1]
    #list of articles most similar by cosine similarity
    mostsimilar = list(cosine_similarity(vec,X).argsort()[0][-6:-1])
    #generating dictionaries to be used in table
    sim = []
    arts = []
    years = []
    contents = []
    for each in mostsimilar:
        arts.append(articles.at[each,'title'])
        years.append(str(articles.at[each,'year']))
        contents.append(articles.at[each,'contents'])
    table = list(zip(arts,years,contents))
    return flask.render_template('template2.html',title=title, topic=topic, sim=table)

#Press release generator
@app.route("/gen", methods=["POST"])
def gen():
    topic = flask.request.form.get("topics", None)
    #select topic from dropdown to generate press release for
    if topic != "Topics":
        article = quotegen(gendicts[topic])
        return flask.render_template('article.html',title="Generated Press Release for " + topic, article=article)
    else:
        #if no input selected, just refresh the page
        topics = ['Accessibility','Elections','Human Trafficking','Immigration','Maritime Issues/Ocean Pollution/Wildlife','Offshore Accounts','Veterans','Topics']
        return flask.render_template('page.html',topics=topics)

app.run(host='0.0.0.0')
app.run(debug=True)
