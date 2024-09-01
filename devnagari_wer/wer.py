from difflib import SequenceMatcher

def calculate_wer(reference, hypothesis):
    """
    Calculate the Word Error Rate (WER) for Devanagari text.
    :param reference: The correct reference text.
    :param hypothesis: The text to evaluate.
    :return: The WER as a float.
    """
    # Tokenize texts by splitting on spaces
    ref_tokens = reference.split()
    hyp_tokens = hypothesis.split()
    
    # Use SequenceMatcher to calculate WER
    matcher = SequenceMatcher(None, ref_tokens, hyp_tokens)
    edits = sum(tag != 'equal' for tag, _, _, _, _ in matcher.get_opcodes())
    return edits / len(ref_tokens) if len(ref_tokens) > 0 else 0.0
