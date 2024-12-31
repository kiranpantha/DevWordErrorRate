import re

class Normalizer:
    def __init__(self):
        self.base_characters = r'[अ-हज्ञत्रक्ष]'
        self.characters_to_convert = "ङञणनम"
        self.halant_pattern = "्"
        self.vowel_signs = {
            'ि': 'ि',
            'ी': 'ी',
            'ु': 'ु',
            'ू': 'ू',
            'ृ': 'ृ',
            'े': 'े',
            'ै': 'ै',
            'ो': 'ो',
            'ौ': 'ौ',
            'ं': 'ं'
        }
    
    def normalize_diacritics(self, sentence):
        normalized_sentence = re.sub(r'[िी]', 'ि', sentence)
        normalized_sentence = re.sub(r'[ुू]', 'ु', normalized_sentence)
        return normalized_sentence

    def normalize_anusvara(self, sentence):
        pattern = f"([{re.escape(self.characters_to_convert)}]){self.halant_pattern}"
        normalized_sentence = re.sub(pattern, 'ं', sentence)
        return normalized_sentence

    def normalize_spaces(self, sentence):
        normalized_sentence = re.sub(r'\s+', ' ', sentence)
        return normalized_sentence.strip()
    
    def normalize_vowels(self, sentence):
        pattern = f"([क-ह][{''.join(re.escape(vowel) for vowel in self.vowel_signs.keys())}])"
        
        normalized_sentence = re.sub(pattern, lambda m: m.group(1), sentence)
        return normalized_sentence
    
    def normalize_punctuation(self, sentence):
        pattern = r'[।.]'
        normalized_sentence = re.sub(pattern, '', sentence)
        return normalized_sentence

    def tokenize_nepali_sentence_for_cer(self, sentence):
        sentence = self.normalize_spaces(sentence)
        sentence = self.normalize_vowels(sentence)
        sentence = self.normalize_diacritics(sentence)
        sentence = self.normalize_anusvara(sentence)
        sentence = self.normalize_punctuation(sentence)
        return list(sentence)

    def tokenize_nepali_sentence_for_wer(self, sentence):
        sentence = self.normalize_spaces(sentence)
        sentence = self.normalize_vowels(sentence)
        sentence = self.normalize_diacritics(sentence)
        sentence = self.normalize_anusvara(sentence)
        sentence = self.normalize_punctuation(sentence)
        # tokens = re.findall(r'\w+|[^\s\w]', sentence)
        return sentence.split()