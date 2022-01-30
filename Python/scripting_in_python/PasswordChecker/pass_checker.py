import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    # print(res)

    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}')

    return res

def get_password_leaks_count(hashes, hashes_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hashes_to_check:
            return count
    return 0

def read_response(response):
    print(response.text)

def pwned_api_check(password):
    #print('passwprd: ', password.encode('utf-8'))
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #print('password hash: ', sha1password)

    first5char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5char)
    #print('response: ', response)

    #read_response(response)
    
    return get_password_leaks_count(response, tail)

pwned_api_check('123')


def main(args):
    for password in args:
        count = pwned_api_check(password)

        if count:
            print(f'{password} was found {count} times, better to change passwor')
        else:
            print(f'{password} was not found')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))