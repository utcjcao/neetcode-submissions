class Solution:

    def encode(self, strs: List[str]) -> str:
        # input: list of strings, output is one string
        # combine all the strings together. 
        # , " "

        # we can convert each character to its ascii representation
        # we can use a special character to separate these ascii representations
        if (len(strs) == 0):
            return "-"
        ans = ""
        for s in strs:
            for char in s:
                ans += str(ord(char)) + " "
            ans += ","
        return  ans[:len(ans)-1]


    def decode(self, s: str) -> List[str]:
        # one string of ascii integers separated by spaces and commas
        if s == "-":
            return []
        splitted_strs = s.split(",") # ascii integers separated by spaces
        ans = []
        for encoded_str in splitted_strs:
            ascii_arr = encoded_str.split(" ")
            ans.append("".join([chr(int(char)) for char in ascii_arr[:len(ascii_arr)-1]]))
        return ans
        # output: a single string, returns a list of strings
