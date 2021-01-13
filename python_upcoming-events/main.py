from bs4 import BeautifulSoup
import requests


def get_events_info(soup):
    events = soup.select('ul.list-recent-events li')

    return [{'title': event.h3.text,
             'date': event.p.time.text,
             'location': event.p.select_one('span.event-location').text} for event in events]


def get_soup(link):
    response = requests.get(link)
    return BeautifulSoup(response.text, 'lxml')


def print_events(events_info):
    for event_info in events_info:
        print(f'\nEvent title: {event_info["title"]}\n'
              f'Date: {event_info["date"]}\n'
              f'Location: {event_info["location"]}')

if __name__ == '__main__':
    python_main_link = 'https://www.python.org'
    soup = get_soup(python_main_link)
    events_btn = soup.find('li', attrs={'id': 'events'}).a

    python_events_link = python_main_link + events_btn['href']
    soup = get_soup(python_events_link)

    events_info = get_events_info(soup)
    print_events(events_info[:3])
