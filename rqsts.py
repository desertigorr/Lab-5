import requests

response = requests.get('https://vk.com')
print(f'Status code: {response.status_code}')


print('1. Nubmersapi.com API')
num = int(input('Input number: '))
res = requests.get(f'http://numbersapi.com/{num}')
print(res.text, '\n')


KEY = 'c95ded21f03f66825588e2e2109f3c78'

def get_weather():
    print('2. Openweathermap API.')
    city = input('Input city name: ')

    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&units=metric')
    response = result.json()

    print(f'City: {city}')
    print(f'County: {response["sys"]["country"]}')
    print(f'Temperature: {round(response["main"]["temp"])}°')
    print(f'Weather: {response["weather"][0]["main"]}\n')

get_weather()

def get_word_info():
    print('3. Online dictionary API (meanings of words).')
    word = input('Input word: ')
    result = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    if result.status_code == 200:
        response = result.json()
        count = 0

        print('Meanings:')
        for i in response[0]["meanings"]:
            for j in i["definitions"]:
                count += 1
                print(f'{count}. {j["definition"]}')
    else:
        print('You typed something wrong')


get_word_info()