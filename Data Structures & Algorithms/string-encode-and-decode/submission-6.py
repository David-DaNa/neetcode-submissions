class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += str(len(i)) + "#" + i
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        chars_count = 0
        # while chars_count < len(s):
        #     i = int(s[chars_count])
        #     word = s[chars_count + 2 : i + 1]
        #     decoded_string.append(word)
        #     chars_count = chars_count + i + 1
        while chars_count < len(s):
            j = chars_count

            # Move j until it reaches the delimiter "#"
            while s[j] != "#":
                j += 1

            # Length is everything before "#"
            length = int(s[chars_count:j])

            # Word starts after "#"
            word_start = j + 1
            word_end = word_start + length

            word = s[word_start:word_end]
            decoded_string.append(word)

            # Move to the next encoded word
            chars_count = word_end

        return decoded_string


