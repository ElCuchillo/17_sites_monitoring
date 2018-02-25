import sys
import requests
from whois import whois
from datetime import datetime


def get_urls4check(filepath):
    with open(filepath, 'r') as file:
        for url in file:
            if url != '\n':
                yield url.strip('\n ')


def is_server_respond_with_200(url):
    try:
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            return True
    except requests.exceptions.InvalidSchema:
        return False
    except requests.exceptions.ConnectionError:
        return False


def check_domain_expiration_date(domain_name):
    response = whois(domain_name)
    if isinstance(response.expiration_date, datetime):
        expiration_date = response.expiration_date
    elif isinstance(response.expiration_date, list):
        expiration_date = response.expiration_date[0]
    if (expiration_date - datetime.now()).days > 30:
            return True


def check_url(url, results_dict):
    if is_server_respond_with_200(url):
        results_dict[url][respond] = is_server_respond_with_200(url)
        results_dict[url][date] = check_domain_expiration_date(url)
    else:
        results_dict[url] = ['Invalid URL', 'Invalid URL']


def print_result(results_dict):
    for url, status in results_dict.items():
        print('\n{}:\n request HTTP 200: {},\n '
              'Domain Name paid for 1 month and more: {}'
              .format(url, status[respond], status[date]))


if __name__ == '__main__':
    try:
        respond = 0
        date = 1
        results_dict = {url: [False, False] for url
                       in get_urls4check(sys.argv[1])}
        for url in results_dict.keys():
            check_url(url, results_dict)
        print_result(results_dict)
    except IndexError:
        print("Launch: $python3 check_site_health.py <path_to_file>"
              "where <pathe_to_file> is a file with list of urls for checking")
    except FileNotFoundError:
        print('File {} not found'.format(sys.argv[1]))


