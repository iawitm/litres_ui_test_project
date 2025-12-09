# Дипломный проект тестирования веб-версии Litres.ru
> [Litres](https://www.litres.ru/)

![This is an image](/resources/images/readme/litres.png)

### Список проверок:
- [x] Проверка поиска на главной странице
  - Поиск существующей книги по ее названию
  - Поиск несуществующей книги
- [x] Проверка страницы книги
  - Добавление книги в \"Отложено\"
  - Добавление книги в корзину
- [x] Проверка страницы \"Отложено\"
  - Удаление книги из \"Отложено\"
  - Выбор книги из \"Отложено\" ведет на страницу рекомендаций
- [x] Проверка страницы корзины
  - Проверка необходимости авторизоваться перед покупкой
  - Удаление книги без добавления в избранное
  - Удаление книги с добавлением в избранное
  - Добавление книги в избранное без удаления
----
### Используемые технологии
<p  align="center">
   <code><img width="5%" title="Python" src="/resources/images/readme/python.png"></code>
   <code><img width="5%" title="PyCharm" src="/resources/images/readme/pycharm.png"></code>
   <code><img width="5%" title="Selene" src="/resources/images/readme/selene.png"></code>
   <code><img width="5%" title="Pytest" src="/resources/images/readme/pytest.png"></code>
   <code><img width="5%" title="Jenkins" src="/resources/images/readme/jenkins.png"></code>
   <code><img width="5%" title="Allure Report" src="/resources/images/readme/allure_report.png"></code>
   <code><img width="5%" title="Allure TestOps" src="/resources/images/readme/allure_testops.png"></code>
   <code><img width="5%" title="Telegram" src="/resources/images/readme/tg.png"></code>
</p>

----
### Локальный запуск

1. Склонировать репозиторий
2. Установить зависимости командой `pip install -r requirements.txt`
3. Открыть проект в PyCharm, установить интерпретатор
4. Создать `.env` файл, пример файла - `.env.example`
5. Запустить тесты в командной строке `pytest .`:

----
### Удаленный запуск в Jenkins

> <a target="_blank" href="https://jenkins.autotests.cloud/job/iawitm_litres_ui_test_project/">_**Ссылка на сборку в Jenkins**_</a>

1. Открыть проект
2. Выбрать пункт `Build with Parameters`
3. Указать комментарий для отчета в Telegram
3. Нажать кнопку `Build`

![This is an image](/resources/images/readme/jenkins_build.png)

----

### Allure отчет

#### Пример формирования отчета:

![This is an image](/resources/images/readme/allure_overview.png)

----
### Интеграция с Allure TestOps

#### Пример генерации тест-кейсов на основе автотестов
![This is an image](/resources/images/readme/testops_cases.png)

----
### Оповещение о результатах прогона тестов в Telegram
#### Пример уведомления в Telegram
![This is an image](/resources/images/readme/tg_notification.png)