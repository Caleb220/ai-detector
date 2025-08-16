import math
import re
from collections import Counter
from typing import Tuple


def shannon_entropy(text: str) -> float:
    """Calculate Shannon entropy of the input text."""
    counts = Counter(text)
    total = sum(counts.values())
    if total == 0:
        return 0.0
    return -sum((c / total) * math.log2(c / total) for c in counts.values())


def word_stats(text: str) -> Tuple[float, float]:
    """Return average word length and its standard deviation."""
    words = re.findall(r"\b\w+\b", text)
    if not words:
        return 0.0, 0.0
    lengths = [len(w) for w in words]
    avg = sum(lengths) / len(lengths)
    variance = sum((l - avg) ** 2 for l in lengths) / len(lengths)
    std_dev = math.sqrt(variance)
    return avg, std_dev


def analyse_text(text: str) -> tuple[float, str]:
    """Analyse text and return a score and explanation."""
    entropy = shannon_entropy(text)
    avg_len, std_dev = word_stats(text)

    def sigmoid(x: float) -> float:
        return 1 / (1 + math.exp(-x))

    entropy_component = sigmoid(entropy - 3.5)
    variance_component = sigmoid(std_dev - 1.5)
    score = (entropy_component + variance_component) / 2 * 100

    explanation = (
        f"Entropy={entropy:.2f}, Avg word length={avg_len:.2f}, Std dev={std_dev:.2f}"
    )
    return score, explanation
