# backend/server/logic/heuristic.py
import spacy
from textstat import textstat
from dataclasses import dataclass, field
from typing import List, Dict

from .utils import is_valid_text


nlp = spacy.load('en_core_web_sm')


@dataclass
class SentenceData:
    text: str
    word_count: int


@dataclass
class AnalysedText:
    original_text: str
    sentences: List[SentenceData] = field(default_factory=list)
    average_sentence_length: float = 0.0
    total_sentences: int = 0
    total_words: int = 0


@dataclass
class Readbility:
    overall_readability: float
    readability_score: float
    grade_score: int
    reading_time: float


@dataclass
class Burstiness:
    burstiness_value: float


@dataclass
class TextRepitition:
    reptition_score: float



def score_ai_detection(text: str):
    analysed_text = AnalysedText(original_text=text)

    analysed_text.average_sentence_length = _average_sentence_length(analysed_text)

    _calculate_readability(analysed_text.original_text)

    return analysed_text.average_sentence_length


def _average_sentence_length(text_data: AnalysedText):
    # split text into sentences
    doc = nlp(text_data.original_text)
    text_data.sentences = list(doc.sents)
    text_data.total_sentences = len(text_data.sentences)
    sentence_lengths = []

    # filter puncuation etc within sentences
    for sent in text_data.sentences:
        words = [token.text for token in sent if token.is_alpha]
        sentence_lengths.append(len(words))
    
    text_data.total_words = sum(sentence_lengths)

    if sentence_lengths:
        return sum(sentence_lengths) / len(sentence_lengths)
    return 0


def _calculate_readability(text: str):
    grade_to_read = textstat.flesch_kincaid_grade(text)
    



def _calculate_burstiness(text: str): ...



def _check_repitition(text: str): ...


