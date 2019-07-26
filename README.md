# GorgeousApp

[![App:Gorgeous](https://img.shields.io/badge/App-Gorgeous-5a00b4.svg?longCache=true)](https://gorgeous-app.herokuapp.com)
[![App:LINEbot](https://img.shields.io/badge/App-LINEbot-1dcd00.svg?longCache=true)](http://nav.cx/4O8fsmz)
![Deployed on:Heroku](https://img.shields.io/badge/Deployed-Heroku-ff69b4.svg?longCache=true)

`flask` & `LINE-bot-sdk` & `gorgeous.py` on `Heroku`  
ゴー☆ジャスWebアプリ&LINEボット 〜キミのハートに、レボ☆リューション〜

<a href="http://nav.cx/4O8fsmz"><img src="https://scdn.line-apps.com/n/line_add_friends/btn/ja.png" alt="友だち追加" height="36" border="0"></a>

## LINE-bot

ID: [@244wensq](http://nav.cx/4O8fsmz)

![gif](https://i.gyazo.com/6a41b54b6dcc0809dd408499e7a9aedf.gif)

## Web App

[<https://gorgeous-app.herokuapp.com/>](https://gorgeous-app.herokuapp.com/)

![gif](https://i.gyazo.com/e12670ef155861b6544e3be7ede5b1e7.gif)

---

## Environment

### API

web app: `/` : `POST`, `GET`  
LINE bot: `/callback`: `POST`

### on local Docker

```shell
docker build .
```

### run app

```shell
python run.py -p 8080
```

or

```shell
docker run -p 8080:8000 -it --rm
```

#### Get Data for `Gorgeous.revolution()`

```shell
python get_nations_data.py
```

#### Front-end

- SASS style css
- menu with [Slideout.js](https://slideout.js.org/)
