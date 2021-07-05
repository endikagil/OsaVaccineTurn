# OsaVaccineTurn

Due to covid19 and the global pandemic, vaccination shifts have been established among the population. <br>
This script checks on 'Osakidetza' health page if they have included us within the current vaccination shift. <br>
In that case, it notifies you thought Telegram. <br>
It checks every 2 minutes, but you can adapt as you wish. <br>
 
Use .env file to specify sensitive information: <br>
TIS_NUMBER, SURNAME, BIRTHDATE, CHROME_DRIVER_PATH, TELEGRAM_API_TOKEN, TELEGRAM_CHAT_ID


### Requirements 📋

Make sure to create a Telegram bot:

```
https://core.telegram.org/bots/api
```

You also need to download a driver for web browser. In my case I used Chrome web browser (v91) driver for MacOSX.<br>
You can download your version driver at:
```
https://chromedriver.chromium.org/downloads
```


### Installation 🔧

Install requirements:

```
$ pip install -r requirements.txt
```

Create .env file to set your values:

```
TIS_NUMBER = '<Your TIS number>'
SURNAME = '<Your surname>'
BIRTHDATE = '<Your birthdate>'
TELEGRAM_API_TOKEN = '<Your_Telegram_API_Token>'
TELEGRAM_CHAT_ID = '<Your_Chat_ID>'
CHROME_DRIVER_PATH = '<Your chrome driver path>'
```

## Configure system ⚙️

It checks every 2 minutes, but you can adapt as you wish by changing the value of this line:
```
driver.implicitly_wait(<Secs you want to wait>)
```

## Author ✒️

* **Endika Gil** - *Initial Work* - [endikagil](https://github.com/endikagil)