from typing import List


class CodeToWordTranslator:
    @staticmethod
    def translate_codes_to_words(codes: List[str]) -> List[str]:
        words: List[str] = list()
        
        for code in codes:
            word_elems = []
            for code_elem in code:
                word_elem = CodeToWordTranslator.translate_code_to_word(code_elem)
                word_elems.append(word_elem)
            word_elems = CodeToWordTranslator.get_word_with_leading_zeroes(word_elems)
            words.append(' '.join(word_elems))
        return words
    
    @staticmethod
    def translate_code_to_word(code: str) -> str:
        word: str = bin(int(code, 16))[2:]
        word_with_zeroes = word.zfill(4)
        return word_with_zeroes
    
    @staticmethod
    def get_word_with_leading_zeroes(word: List[str]) -> List[str]:
        missing_zeroes_count: int = 4 - len(word)
        word_result: List[str] = ['0000'] * missing_zeroes_count + word
        return word_result
