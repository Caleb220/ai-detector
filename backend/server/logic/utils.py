# backend/server/logic/utils.py
import re


# tokense text -> sentences and remove white space
def tokenise_sentencs(text: str):
    return [s.strip() for s in text.split('.') if s.strip()]



def tokenise_words(text: str):
    return text.split()


def is_valid_text(text: str, min_word_count: int = 10, min_char_ratio: float = 0.7) -> bool:
    stripped_text = text.strip()

    code_patterns = [
        r"\bdef\s+\w+\s*\(",          # Python function defs
        r"\bclass\s+\w+\s*[:{]",      # Class definition (Python, JS-style)
        r"\bfunction\s+\w+\s*\(",     # JS function
        r"\bvar\s+\w+",               # JS variable
        r"\bconst\s+\w+",             # Const in JS
        r"<\/?[a-z]+\s*[^>]*>",       # HTML tags
        r"\w+\s*=\s*['\"].+['\"]",    # String assignments
        r"\bimport\s+\w+",            # Import statements
        r"\bif\s*\(.+\)\s*{?",        # if statements with ()
    ]

    if len(stripped_text) < 30:
        return f"Invalid Input, input text doesnt meet the minimum character requirements of 30."  

    words = stripped_text.split()
    if len(words) < min_word_count:
        return f"Invalid Input, input text doesnt meet the minimum word requirements of {min_word_count}."

    # Checks if text is mostly alphabetical characters
    alpha_chars = len(re.findall(r'[a-zA-Z]', stripped_text))
    total_chars = len(stripped_text)
    if total_chars == 0 or (alpha_chars / total_chars) < min_char_ratio:
        return "Invalid Input, not able to analyse text due to text not being alphabetical characters"

    # no code like text as input 
    for pattern in code_patterns:
        if re.search(pattern, stripped_text):
            return "Invalid Input, Code like input detected." 

    return "Success"