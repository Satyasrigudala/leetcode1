from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Extract only letters from licensePlate, lowercase, and count frequencies
        target = Counter(ch.lower() for ch in licensePlate if ch.isalpha())

        res = None
        for word in words:
            word_count = Counter(word.lower())
            
            # Check if word covers target letters
            if all(word_count[ch] >= target[ch] for ch in target):
                if res is None or len(word) < len(res):
                    res = word
        return res
