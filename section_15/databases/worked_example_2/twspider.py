from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# створити таблицю, якщо Twitter не існує
cur.execute('''
            CREATE TABLE IF NOT EXISTS Twitter 
            (name TEXT, retrieved INTEGER, friends INTEGER)''')

# Ignore SLL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT name FROM twitter WHERE retrieved = 0 LIMIT 1')
        try:
            # fetchone() 1-й рядок
            # [0] 1-й стовпець
            acct = cur.fetchone()[0]
        except:
            print('No unretrieved Twitter accounts found')
            continue
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'album_count': '5'})
    print('Retrieving', url)
    connection = urlopen(url, context=ctx)
    # Отримати формат файлу в utf-8 также после в unicode
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    # Debugging
    # print json.dumps(js, indent=4)

    cur.execute('UPDATE Twitter SET  =1 WHERE name = ?', (acct,))

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
                    (friend,))
        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friend = ? WHERE name = ?',
                        (count + 1, friend))
            countold += 1
        except:
            cur.execute('''INSERT INTO Twitter (name, retrieved, friends) 
                        VALUES (?, 0, 1)''', (friend,))
            countnew += 1
    print('New accounts=', countnew, ' revisited=', countold)
    conn.commit()