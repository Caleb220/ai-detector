from logic import analyse_text


def test_analyse_text_produces_score_and_explanation():
    score, explanation = analyse_text("This is a simple test sentence for AI detection.")
    assert isinstance(score, float)
    assert 0 <= score <= 100
    assert "Entropy" in explanation
