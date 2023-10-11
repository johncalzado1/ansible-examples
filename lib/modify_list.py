import sys

if __name__ == "__main__":
    
    # Get input
    list_size = len(sys.argv)
        
    if list_size <= 1:
        raise Exception("Need to pass a param")
    
    index = 1
    
    while index < list_size:
        i = {
            "value": sys.argv[index],
            "extra": ""
        }
        print(i)
        index += 1
    
    
    