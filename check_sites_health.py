import sys
import requests
from whois import whois
from datetime import datetime


def get_urls4check(filepath):
    with open(filepath, 'r') as file:
        for url in file:
            if url != '\n':
                yield url.strip('\n ')


def is_server_respond_ok(url):
    try:
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            return True
    except requests.exceptions.InvalidSchema:
        return False
    except requests.exceptions.ConnectionError:
        return False


def check_domain_expiration_date(domain_name, paid_period=30):
    response = whois(domain_name)
    if not(response.expiration_date):
        return False
    if isinstance(response.expiration_date, datetime):
        expiration_date = response.expiration_date
    elif isinstance(response.expiration_date, list):
        expiration_date = response.expiration_date[0]
    if (expiration_date - datetime.now()).days > paid_period:
        return True
    else:
        return False


def check_url(url):
    server_ok = is_server_respond_ok(url)
    if server_ok:
        return [server_ok, check_domain_expiration_date(url)]
    else:
        return ['Invalid URL', 'Invalid URL']


def print_result(results_dict):
    for url, status in results_dict.items():
        print('\n{}:\n request HTTP 200: {},\n '
              'Domain Name paid for 1 month and more: {}'
              .format(url, status[respond], status[date]))


if __name__ == '__main__':
    try:
        respond = 0
        date = 1
        results_dict = {}
        for url in get_urls4check(sys.argv[1]):
            results_dict[url] = check_url(url)
        print_result(results_dict)
    except IndexError:
        print('Launch: $python3 check_site_health.py <path_to_file>'
              'where <pathe_to_file> is a file with list of urls for checking')
    except FileNotFoundError:
        print('File {} not found'.format(sys.argv[1]))


