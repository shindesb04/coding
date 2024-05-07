class Solution:
    def decodeString(self, s: str) -> str:
        curstr = ""
        num = 0

        numS = []
        strS = []

        for c in s:
            if c.isalpha():
                curstr += c
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                numS.append(num)
                strS.append(curstr)
                curstr = ""
                num = 0
            elif c == "]":
                Tnum = numS.pop()
                temp1 = ""
                for i in range(Tnum):
                    temp1 += curstr
                temp = strS.pop()
                curstr = temp + temp1
        return curstr
