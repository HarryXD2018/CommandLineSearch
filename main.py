import argparse
import csv
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str)
    parser.add_argument('-e', type=str)
    args = parser.parse_args()
    print(args)
    path = r'C:\...\dist\\'        # Add your PATH dir here
    csv_file = csv.reader(open(path+'default_database.csv', 'r', encoding='UTF8'))
    data_item = [row for row in csv_file]
    keyword = args.keyword
    keyword: str
    keyword = keyword.replace(' ', '+')
    print(keyword)
    for data in data_item:
        engine = data[0]
        url_link = data[1]
        print(engine, url_link)
        if engine == args.e:
            url = url_link.format(keyword)
            os.system(r'start "C:\Program Files\Google\Chrome\Application\chrome.exe" {}'.format(url))
            break
    else:
        url = data_item[1][1].format(keyword)
    print(url)
    os.system(r'start "C:\Program Files\Google\Chrome\Application\chrome.exe" {}'.format(url))
