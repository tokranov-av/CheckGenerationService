Данный сервис разработан с соответствии с техническим заданием, которое приведено в папке ТЗ с необходимыми файлами.

Сервис выполняет следующие функции:

1. После получения информации о новом заказа в виде json-файла, создаёт в БД чеки для всех принтеров точки указанной в заказе и ставит асинхронные задачи на генерацию PDF-файлов для этих чеков. Если у точки нет ни одного принтера - возвращает ошибку. Если чеки для данного заказа уже были созданы - возвращает ошибку.
2. Асинхронный воркер с помощью wkhtmltopdf генерируют PDF-файл из HTML-шаблон. Имя файла имеет следущий вид <ID заказа>_<тип чека>.pdf (123456_client.pdf). Файлы хранятся в папке media/pdf в корне проекта.
3. Приложение опрашивает сервис на наличие новых чеков. Опрос происходит по следующему пути: сначала запрашивается список чеков которые уже сгенерированы для конкретного принтера, после скачивается PDF-файл для каждого чека и отправляется на печать.

Сервис разработан с использованием фреймворка Django и DRF, библиотки для асинхронных задач django_rq, docker-контейнера базы данных Postgres 9.6, инструмента формирования pdf-файлов wkhtmltopdf в виде docker-контейнера, и хранилища redis, которая также запускается в docker-контейнере.

Проект собирается с помощью docker-compose

Эндпоинты сервиса приведены в файле api.yml, расположенный в папке ТЗ