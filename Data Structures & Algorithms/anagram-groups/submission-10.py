class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        def get_ord_list_for_word(word):
            ord_list = [0] * 26
            for char in word:
                ord_list[ord(char) - ord('a')] += 1
            return ord_list

        result = []
        anagram_groups = collections.defaultdict(list) # (ord_list) -> [word]

        for word in strs:
            word_ord_tuple = tuple(get_ord_list_for_word(word))            
            anagram_groups[word_ord_tuple].append(word)
        
        return [value for key, value in anagram_groups.items()]