Пульт охраны банка
Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны — это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

Как установить
Запросите доступ к БД у менеджера вашего банка. Для доступа вам понадобятся:
 - хост 
 - порт
 - имя базы данных
 - имя пользователя базы данных
 - пароль
 
Эти параметры задаются в файле ``.env``:

DB_HOST=''

DB_PORT=''

DB_NAME=''

DB_USER=''

DB_PASSWORD=''

Скачать архив по ссылке: 
[https://github.com/killla/django-orm-watching-storage/archive/master.zip](https://github.com/killla/django-orm-watching-storage/archive/master.zip)

Распаковать архив в папку.

datacenter
project
manage.py
requirements.txt

 
 , .................... [TODO: объясните пользователю, куда класть эти данные и как они выглядят]

Python3 должен быть уже установлен. Затем используйте pip для установки зависимостей:

``pip install -r requirements.txt``
[TODO: объясните куда класть файл с каталогом вин]

[TODO: приведите пример содержимого файла с каталогом вин, чтобы было что копировать]

[TODO: объясните какой командой сайт запустить и где он появится]

Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.


# Пульт охраны банка

## Общее описание
Данная программа представляет собой интерфейс для охранника банка.
Программа подключается к удаленной базе данных и отображает:
* список активных карт доступа
* список всех визитов по карте доступа
* список находящихся лиц в хранилище

А также проодит оценку подозрительности поведения сотрудников по количеству проведенного времени в хранилище.

## Требования:
* Python версии 3.0 и выше

## Настройка
Перед запуском программы должны быть заданы переменные окружения:
* DB_HOST - адрес базы данных
* DB_PORT - порт
* DB_NAME - название базы данных
* DB_USER - имя пользователя
* DB_PASSWORD - пароль
* DEBUG - режим отладки (0 - выкл, 1 - вкл)

## Запуск
``python main.py``

После запуска программа доступна через веб интерфейс по адресу [http://0.0.0.0:8000/](http://0.0.0.0:8000/)


## Структура программы
Веб интерфес состоит из трех веб страниц:
/active_passcards_view - страница с активными пропусками
/passcard_info_view - страница конкретного пропуска со всеми визитами по нему
/storage_information_view - сотрудники находящиеся в хранилище

## Лицензия
Программа подготовлена для [dvmn.org](dvmn.org).
