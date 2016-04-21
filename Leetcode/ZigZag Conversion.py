''' 
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

'''

class Solution:
     # @return a string 
    def convert(self, s, nRows):
        
        if nRows == 1: return s

        tmp =[ ''  for i in range(nRows)]
        index = -1; step = 1

        for i in range(len(s)):
            index += step            
            
            if index == nRows: #轉方向的點
                index -= 2; step = -1 
            elif index == -1 :#轉方向的點
                index = 1; step = 1 

            tmp[index] += s[i]
        return  '' .join(tmp)

if __name__ == "__main__":
    s = Solution() 
    print s.convert( "PAYPALISHIRING", 3 )
    print s.convert( "PAYPALISHIRING", 4 )