from bs4 import BeautifulSoup
import requests
from datetime import datetime as dt
from collections import namedtuple
import threading
import concurrent.futures

Event = namedtuple('Event', 'title location date_start date_end')


def format_date_for_output(date):
    return date.strftime('%d %B %Y')


def reformat_event_date(date):
    reformat_date = dt.strptime(date, '%Y-%m-%dT%H:%M:%S%z')
    return reformat_date


def get_events_links(main_link):
    soup = get_soup(main_link)
    events_btn = soup.find('li', attrs={'id': 'events'}).a
    python_events_link = main_link + events_btn['href']
    soup = get_soup(python_events_link)

    return [python_main_link + event_link['href'] for event_link in soup.select('h3.event-title a')]


def get_event_info(link):
    soup = get_soup(link)

    return Event(soup.select_one('h1.single-event-title').text.strip(),
                 soup.select_one('span.single-event-location').text.strip(),
                 reformat_event_date(soup.select_one('time.date-start')['datetime']),
                 reformat_event_date(soup.select_one('time.date-end')['datetime']))


def get_events_info(main_link):
    events_links = get_events_links(main_link)
    events_info = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(events_links)) as executor:
        events_info = list(executor.map(get_event_info, events_links))

    return events_info


def get_soup(link):
    response = requests.get(link)
    return BeautifulSoup(response.text, 'lxml')


def print_events(events_info):
    for event_info in events_info:
        print(f'\nEvent title: {event_info.title}\n'
              f'Date start: {format_date_for_output(event_info.date_start)}\n'
              f'Date end: {format_date_for_output(event_info.date_end)}\n'
              f'Location: {event_info.location}')


if __name__ == '__main__':
    python_main_link = 'https://www.python.org'
    events_info = get_events_info(python_main_link)
    print_events(events_info[:3])
