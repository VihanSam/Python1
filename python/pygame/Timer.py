import time

def countdown(usertime):
    while usertime >= 0:
        mins,secs = divmod(usertime,60)
        timer = '{:02d}: {:02d}'.format(mins, secs)
        print(timer,end='\r')
        time.sleep(1)
        usertime -= 1
    print('lift off!')
if __name__ == '__main__':
    usertime = int(input("Enter a time in seconds"))
    countdown(usertime)
    