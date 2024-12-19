1. Устанавливаем виртуальное окружение
$ python3 -m venv venv
$ venv/bin/activate
(venv) $ pip install -r ./requirements.txt

2. Запускаем приложение
$ uvicorn main:app --reload

3. Деплой
$ docker build . --tag fastapi_app && docker run -p 80:80 fastapi_app