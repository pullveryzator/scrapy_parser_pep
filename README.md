markdown
# PEP Document Parser

Этот проект представляет собой парсер документов PEP (Python Enhancement Proposals), который собирает и анализирует информацию о PEP и выводит результаты в формате CSV.

## Описание

Парсер извлекает информацию о PEP с официального сайта [https://peps.python.org/](https://peps.python.org/) и создает два файла CSV:

1. **peps_<date_time>.csv** - Список всех PEP, включающий:
   - Номер PEP
   - Название PEP
   - Статус PEP

2. **status_summary_<date_time>.csv** - Сводка по статусам PEP, содержащая:
   - Статус PEP
   - Количество PEP с данным статусом
   - Последняя строка с итоговым количеством всех документов, где статус указывается как `Total`.

## Функциональность

- Метод `parse()` собирает ссылки на страницы с документами PEP.
- Метод `parse_pep()` парсит страницы с документами PEP и формирует объекты `Items`.
- Для парсинга применяются CSS- или XPath-селекторы.
- Парсер использует класс `PepParseItem` (наследник `scrapy.Item`), который имеет три атрибута:
  - `number`: номер PEP
  - `name`: название PEP
  - `status`: статус, указанный на странице PEP

## Установка и запуск

1. Клонируйте репозиторий:

   
bash
git clone git@github.com:pullveryzator/scrapy_parser_pep.git
cd scrapy_parser_pep


2. Установите необходимые зависимости (например, через `pip`):

   
bash
pip install -r requirements.txt


3. Запустите парсер:

   
bash
scrapy crawl pep


## Результаты

Результаты парсинга будут сохранены в два файла CSV в директории `results/`, которая находится в корне проекта, на одном уровне с папками `pep_parse/` и `tests/`.

## Пример файлов

- **pep_<date_time>.csv**
  
  | Number | Name                            | Status       |
  |--------|---------------------------------|--------------|
  | PEP 1  | PEP Purpose and Guidelines      | Final        |
  | PEP 2  | Procedure for Adding New Module | Final        |
  
- **status_summary_<date_time>.csv**

  | Статус    | Количество |
  |-----------|------------|
  | Final     | 10         |
  | Draft     | 5          |
  | Total     | 15         |

## Контрибьюция

Приветствуется любая помощь! Пожалуйста, создайте issue или pull request для обсуждения изменений.