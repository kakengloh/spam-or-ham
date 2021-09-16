import pickle
import boto3
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from .. import Singleton

class NaiveBayes(metaclass=Singleton):

    classifier: MultinomialNB
    vectorizer: CountVectorizer

    def __init__(self) -> None:
        
        with open('/Users/kakeng/dev/projects/open-source/spam-or-ham/app/classifiers/naive_bayes/vectorizer.pkl', 'rb') as file:
            self.vectorizer = pickle.load(file)

        with open('/Users/kakeng/dev/projects/open-source/spam-or-ham/app/classifiers/naive_bayes/classifier.pkl', 'rb') as file:
            self.classifier = pickle.load(file)

        # s3 = boto3.client(
        #     's3',
        #     aws_access_key_id='',
        #     aws_secret_access_key='',
        #     aws_session_token='',
        # )

        # self.vectorizer = pickle.loads(
        #     s3.Bucket('bucket_name').Object('key_to_pickle.pickle').get()['Body'].read()
        # )

        # self.classifier = pickle.loads(
        #     s3.Bucket('bucket_name').Object('key_to_pickle.pickle').get()['Body'].read()
        # )
