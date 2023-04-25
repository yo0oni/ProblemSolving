def solution(brown, yellow):
    
    width = brown//2+2
    height = 0
    
    while (width-2)*(height-2) != yellow:
        width -= 1
        height += 1
    
    return [width, height]