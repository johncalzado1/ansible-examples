import time

MAX_COUNT = 10

if __name__ == "__main__":
    
    # Count to 60 seconds
    
    counter = 0
    
    while counter < MAX_COUNT:
        time.sleep(1)  # sleep 5 seconds
        print("Counter at: {0}".format(counter))
        counter += 1