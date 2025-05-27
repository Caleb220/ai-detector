# backend/server/logic/utils.py



# tokense text -> sentences and remove white space
def tokenise_sentencs(text: str):
    return [s.strip() for s in text.split('.') if s.strip()]



def tokenise_words(text: str):
    return text.split()