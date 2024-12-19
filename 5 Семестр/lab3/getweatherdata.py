# openweatherapi


def get_weather_data(place, api_key=None):
    if not place or api_key is None:
        return None
    # Запрашиваем данные с api
    data = request_weather_data(place, api_key)
    # Если произошла какая-то ошибка, поднимаем Исключение
    response_code = data.get("cod")
    if response_code != 200:
        raise Exception("Error: " + response_code + " " + data.get("message"))
    # Достаем необходимые данные
    result = extract_weather_data(data)
    # Возвращаем результат
    return result


def request_weather_data(place, api_key=None):
    import requests
    # Создаем URL с помощью URLBuilder'a
    url = "https://api.openweathermap.org/data/2.5/weather"
    query_params = {
        # Метрическая система
        "units": "metric",
        # Название на русском языке
        "lang": "ru",
        # Город
        "q": place,
        # Ключ
        "appid": api_key,
    }
    # Запрашиваем данные с api
    response = requests.get(url, params=query_params)
    # Конвертируем в JSON
    data = response.json()
    # Возвращаем результат
    return data


def extract_weather_data(data):
    import datetime
    import json
    # Валидируем входные данные
    if data is None:
        raise TypeError("Data must not be None.")
    # Создаем словарь с нужными данными
    result = {
        # Название города
        "name": data.get("name"),
        "coord": {
            # Долгота
            "lon": data.get("coord").get("lon"),
            # Широта
            "lat": data.get("coord").get("lat")
        },
        # Временная зона в формате UTC+0
        "timezone": data.get("timezone"),
        # Код города
        "country": data.get("sys").get("country"),
        # Температура (как ощущается)
        "feels_like": data.get("main").get("feels_like")
    }
    # Валидируем полученные данные
    for key, value in result.items():
        if value is None:
            raise TypeError(f"Key `{key}` in weather data is None")

    # Конвертируем offset в UTC+00.00
    timezone_offset = datetime.timedelta(seconds=data["timezone"])
    timezone = datetime.timezone(timezone_offset)
    # Конвертируем UTC в строку UTC+0
    result["timezone"] = str(timezone)[:4] + str(timezone)[4:6].lstrip("0")
    # Конвертируем словарь в JSON
    # ensure_ascii=False для корректного отображения русского языка
    return json.dumps(result, ensure_ascii=False)


def print_weather_forecast(forecast):
    print("\t\tПогода".format())
    print("Город           {}".format(forecast["name"]))
    print("Страна          {}".format(forecast["country"]))
    print("Временная зона  {}".format(forecast["timezone"]))
    print("Координаты      {:.2f}°, {:.2f}°".format(forecast["coord"]["lat"],
                                                    forecast["coord"]["lon"]))
    print("Температура     {:.2f}°C".format(forecast["feels_like"]))


if __name__ == "__main__":
    import os
    import json
    api_key = os.environ['WEATHER_API_KEY']

    # UTC+3
    moscow = get_weather_data("Москва", api_key)
    print_weather_forecast(json.loads(moscow))
    print()

    # UTC+3
    saint_petersburg = get_weather_data("Санкт-Петербург", api_key)
    print_weather_forecast(json.loads(saint_petersburg))
    print()

    # UTC+6
    dakka = get_weather_data("Дакка", api_key)
    print_weather_forecast(json.loads(dakka))
    print()

    # UTC+10
    vladivostok = get_weather_data("Владивосток", api_key)
    print_weather_forecast(json.loads(vladivostok))
    print()

    # UTC+4
    new_york = get_weather_data("New York", api_key)
    print_weather_forecast(json.loads(new_york))
    print()

    # Несуществующий город
    try:
        get_weather_data("New Yorkk", api_key)
    except Exception as err:
        print("Some API error: ", err)

    # Остальные тесты находятся в `get_weather_data.py`
