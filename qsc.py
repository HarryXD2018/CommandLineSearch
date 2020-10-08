import argparse
import csv
import os


def search(f_url: str, f_keyword: str):
    f_url = f_url.format(f_keyword)
    os.system(r'start "C:\Program Files\Google\Chrome\Application\chrome.exe" {}'.format(f_url))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str)
    parser.add_argument('-e', '--engine', type=str, help='engine')
    args = parser.parse_args()
    print(args)
    path = r'C:\...\dist\\'        # Add your PATH dir here
    csv_file = csv.reader(open(path+'default_database.csv', 'r', encoding='UTF8'))
    data_item = [row for row in csv_file]
    keyword = args.keyword
    keyword = keyword.replace(' ', '+')
    print(keyword)
    for data in data_item[1:]:
        engine = data[0]
        url_link = data[1]
        if engine == args.engine:
            search(url_link, keyword)
            break
        elif args.engine == 'all':
            search(url_link, keyword)
    else:
        if args.engine != 'all':
            url = data_item[1][1].format(keyword)
            os.system(r'start "C:\Program Files\Google\Chrome\Application\chrome.exe" {}'.format(url))
