
import logging, traceback

def foo(s):
    return 10 / int(s)

def bar(s):
    global __gb
    print('gb=%s' % __gb)
    return foo(s) * 2

def main():
    try:
        gb()
        bar('0')
   
    except Exception as e:
        logging.basicConfig(filename='loger.txt', filemode="w", level=logging.ERROR)
        logging.exception(e)
def gb():
    global __gb
    __gb = '你好'
main()
print('__gb:%s' % __gb)
print('END')