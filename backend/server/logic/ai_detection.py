# backend/server/logic/heuristic.py
import spacy

nlp = spacy.load('en_core_web_sm')



def score_ai_detection(text: str):
    avg_sentence_length = _average_sentence_length(text)


    return avg_sentence_length

def _average_sentence_length(text: str):
    # split text into sentences
    doc = nlp(text)
    sentences = list(doc.sents)
    sentence_lengths = []

    # filter puncuation etc within sentences
    for sent in sentences:
        words = [token.text for token in sent if token.is_alpha]
        sentence_lengths.append(len(words))
    
    if sentence_lengths:
        return sum(sentence_lengths) / len(sentence_lengths)
    return 0


def _calculate_burstiness(text: str): ...



def _check_repitition(text: str): ...


