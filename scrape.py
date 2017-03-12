from bs4 import BeautifulSoup
import requests

import models
import secrets

def decorate_yahoo(p):
    r = requests.get(
        'https://baseball.fantasysports.yahoo.com/b1/32447/playersearch?utmpdku=1&search=%s' % p.mlb_name,
        cookies=secrets.YAHOO_COOKIE
    )
    soup = BeautifulSoup(r.content, 'lxml')
    players = soup.select('div.players-table div.ysf-player-name')
    print(len(players))
    for div in players:
        if div.select('a')[0].attrs['href'] == 'https://sports.yahoo.com/mlb/players/%s' % p.yahoo_id:
            position = div.select('span.Fz-xxs')[0].text.strip().split(' - ')[1].replace(',', '/')
            if p.yahoo_pos != position:
                p.yahoo_pos = position
                p.save()
                print(position)
                print(p.yahoo_pos, position)
def main():
    players = models.Players.select().where(
        ~(models.Players.yahoo_id >> None),
        ~(models.Players.mlb_depth >> None),
    )
    for i,p in enumerate(players):
        print(i, p.mlb_name, p.yahoo_id)
        decorate_yahoo(p)

if __name__ == "__main__":
    main()
