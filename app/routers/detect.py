from enum import Enum
from typing import List, Optional
from fastapi import APIRouter
from app.classifiers.naive_bayes import NaiveBayes
from pydantic import BaseModel
import numpy as np

router = APIRouter()

class DetectRequest(BaseModel):
    content: str
    # ip: Optional[str]
    # languages: Optional[List[str]] = ['en']
    # countries: Optional[List[str]] = ['*']

@router.post('/detect', response_model=str)
def spam(request: DetectRequest):

    naive_bayes = NaiveBayes()

    X = np.array([request.content])

    X = naive_bayes.vectorizer.transform(X.astype(str))

    y = naive_bayes.classifier.predict(X).astype(bool).tolist()

    return 'spam' if y[0] else 'ham'
