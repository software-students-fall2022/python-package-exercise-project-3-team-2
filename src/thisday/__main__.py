import thisday.thisday as thisday
import sys

def main():
    response = thisday.run(sys.argv)
    print(response)

if __name__ == '__main__':
    main()