from typing import List, Optional
from fastapi import APIRouter
from app.classifiers.naive_bayes import NaiveBayes
from pydantic import BaseModel
import numpy as np

router = APIRouter()

class DetectDto(BaseModel):
    content: str
    ip: Optional[str]
    languages: Optional[List[str]] = ['en']
    countries: Optional[List[str]] = ['*']

class DetectResponse(BaseModel):
    spam: bool
    ham: bool

@router.post('/', response_model=DetectResponse)
def detect(dto: DetectDto):

    naive_bayes = NaiveBayes()

    X = np.array([dto.content])

    X = naive_bayes.vectorizer.transform(X.astype(str))

    y = naive_bayes.classifier.predict(X).astype(bool).tolist()

    spam = y[0]
    ham = not spam

    return {
        'spam': spam,
        'ham': ham,
    }
