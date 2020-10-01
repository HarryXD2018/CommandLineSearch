import argparse
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str)
    parser.add_argument('-e', type=str)
    args = parser.parse_args()
    print(args)
    if args.e == 'trans':
        url = r'http://dict.youdao.com/w/eng/{}'.format(args.keyword)
    elif args.e == 'tieba':
        url = r'http://tieba.baidu.com/f?kw={}'.format(args.keyword)
    elif args.e == 'baidu':
        url = r'https://www.baidu.com/s?wd={}'.format(args.keyword)
    elif args.e == 'jd':
        url = r'https://search.jd.com/Search?keyword={}'.format(args.keyword)
    elif args.e == 'taobao':
        url = r'https://s.taobao.com/search?q={}'.format(args.keyword)
    else:
        url = r'https://cn.bing.com/search?q={}'.format(args.keyword)
    # print(url)
    os.system(r'start "C:\Program Files\Google\Chrome\Application\chrome.exe" {}'.format(url))
