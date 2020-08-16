
"""
Created on Sun Aug 16 13:49:46 2020

@author: harshvardhan
"""


def check(image,sr,sc,newColor,prevC):
    if sr<0 or sr>=len(image) or sc<0 or sc>=len(image[0]) or image[sr][sc]!=prevC or image[sr][sc]==newColor:
        return
    
    image[sr][sc]=newColor    
    check(image, sr+1, sc, newColor, prevC)
    check(image, sr-1, sc, newColor, prevC)
    check(image, sr, sc+1, newColor, prevC)
    check(image, sr, sc-1, newColor, prevC)
    
    
def floodfill(image,sr,sc,newC):
    if image[sr][sc]==newC:
        return image
    prevC = image[sr][sc]
    check(image, sr, sc, newC, prevC)

image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 2
floodfill(image, sr, sc, newColor)