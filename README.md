
Задание выполнено в полном объёме.

**Основной сценарий**
- Шифровка/дешифровка происходит на стороне сервера средствами python и передаётся с помощью формата json.

**Дополнительные сценарии**
- По мере ввода текста в поле появляется частотная диаграмма и предполагаемый сдвиг если он есть (данные сценарии полность проходят на стороне клиента с помощью JavaScript)

**Дополнительно**
- Создана таблица в БД с готовыми текстами, которые можно выбрать под полем ввода из выпадающего списка. Тексты можно добавлять/изменять/удалять через админку:
```
http://localhost:8000/admin/
login - admin
password - admin123
```
Так же есть тест на проверку шифрования/дешифрования, запустить можно с помощью команды:
```
manage.py test - для Windows и python manage.py test для Linux
```


-------------------------------------------------------------------------------------------------------------------
##### Как запустить проект:

**На Windows:**

- В коммандной строке перейти в каталог где вы хотите разместить проект и склонировать репозиторий выполнив команду:
```
git clone https://github.com/deoniszp/CaesarCrypt.git
```
- Перейти в каталог с проектом командой:
```
cd CaesarCrypt
```
- Создать виртуальное окружение командой:
```
virtualenv venv
```
- Активировать виртуальное окружение командой:
```
venv\Scripts\activate
```
- Установить требуемые пакеты с файла зависимостей командой:
```
pip install -r requirements.txt
```
- Запустить сервер командой:
```
manage.py runserver
```
- В браузере перейти по ссылке:
```
http://localhost:8000
```

**На Linux:**

- В терминале перейти в каталог где вы хотите разместить проект и склонировать репозиторий выполнив команду:
```
git clone https://github.com/deoniszp/CaesarCrypt.git
```
- Перейти в каталог с проектом командой:
```
cd CaesarCrypt
```
- Создать виртуальное окружение командой:
```
virtualenv venv
```
- Активировать виртуальное окружение командой:
```
source venv/bin/activate
```
- Установить требуемые пакеты с файла зависимостей командой:
```
pip install -r requirements.txt
```
- Запустить сервер командой:
```
python manage.py runserver
```
- В браузере перейти по ссылке:
```
http://localhost:8000
```
