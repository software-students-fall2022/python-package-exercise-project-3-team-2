import thisday.thisday as thisday
import sys

def main():
    option = thisday.validate(sys.argv)
    dom = thisday.connect(option)
    li = thisday.get_events(dom)
    print(thisday.show(li))

if __name__ == '__main__':
    main()