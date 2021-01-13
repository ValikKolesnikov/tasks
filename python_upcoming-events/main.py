from bs4 import BeautifulSoup
import requests
from datetime import datetime as dt

def reformat_event_date(date):
    reformat_date = dt.strptime(date, '%Y-%m-%dT%H:%M:%S%z')
    return reformat_date.strftime('%d %B %Y')

def get_events_info(links):
    events_soups = [get_soup(link) for link in links]
    events_info = []
    for soup in events_soups:
        events_info.append({'title': soup.select_one('h1.single-event-title').text.strip(),
                            'location': soup.select_one('span.single-event-location').text.strip(),
                            'date_start': reformat_event_date(soup.select_one('time.date-start')['datetime']),
                            'date_end': reformat_event_date(soup.select_one('time.date-end')['datetime'])
                            })

    return events_info

def get_soup(link):
    response = requests.get(link)
    return BeautifulSoup(response.text, 'lxml')


def print_events(events_info):
    for event_info in events_info:
        print(f'\nEvent title: {event_info["title"]}\n'
              f'Date start: {event_info["date_start"]}\n'
              f'Date end: {event_info["date_end"]}\n'
              f'Location: {event_info["location"]}')

if __name__ == '__main__':
    python_main_link = 'https://www.python.org'
    soup = get_soup(python_main_link)
    events_btn = soup.find('li', attrs={'id': 'events'}).a

    python_events_link = python_main_link + events_btn['href']
    soup = get_soup(python_events_link)

    events_links = [python_main_link + event_link['href'] for event_link in soup.select('h3.event-title a')]


    events_info = get_events_info(events_links)
    print_events(events_info[:3])
