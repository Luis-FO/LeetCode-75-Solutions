class Solution:
    def compress(self, chars: list[str]) -> int:
        cont = 0
        write = 0
        lenght = len(chars)
        
        for idx, ch in enumerate(chars):
            cont+=1
            if idx+1 == lenght or  ch != chars[idx+1]:
                chars[write] = ch
                write+=1
                if cont>1:
                    for num in str(cont):
                        chars[write] = num
                        write+=1
                cont = 0
        return write