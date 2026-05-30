import requests
res = set()


def fetch():
    from datetime import datetime
    from time import sleep
    while True:
        try:
            x = requests.get('https://third-shifr-uvb.cloudpub.ru/poll', timeout=5).json()
            if 'message' in x: res.add(x['message'])
            new = []
            with open('CIPHERTEXT_STORAGE.txt') as f:
                data = f.readlines()
                new = [(j + (' ' * ((100 * ((len(j) // 100) + 1)) - len(j))) + str(datetime.now()) + '\n') for j in res if j not in [i[:-1].split('   ')[0] for i in data] and j != '>>>...<<<']
            if new:
                with open('CIPHERTEXT_STORAGE.txt', 'a') as f:
                    f.write('\n'.join(new))
            print([i for i in res])
        except Exception as e:
            print(e)
        sleep(1)
