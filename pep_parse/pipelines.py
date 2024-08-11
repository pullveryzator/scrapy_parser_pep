import csv
from datetime import datetime as dt

from .constants import BASE_DIR, EXPECTED_STATUS, DATETIME_FOR_FILE_FORMAT


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = [('Статус', 'Количество')]
        self.unexpected_status = set()
        self.status_list = []

    def process_item(self, item, spider):
        if item['status'] not in EXPECTED_STATUS:
            self.unexpected_status.add(item['status'])
        self.status_list.append(item['status'])
        return item

    def close_spider(self, spider):
        for status in EXPECTED_STATUS:
            self.results.append((status, self.status_list.count(status)))
        for status in self.unexpected_status:
            self.results.append((status, self.status_list.count(status)))
        self.results.append(('Total', len(self.status_list)))
        results_dir = BASE_DIR.parent / 'results'
        results_dir.mkdir(exist_ok=True)
        now_formatted = dt.now().strftime(DATETIME_FOR_FILE_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(self.results)
