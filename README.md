# GorgeousApp

![Heroku](https://heroku-badge.herokuapp.com/?app=gorgeous-line-bot)

---

<a href="http://nav.cx/4O8fsmz"><img src="https://scdn.line-apps.com/n/line_add_friends/btn/ja.png" alt="友だち追加" height="36" border="0"></a>

`flask` & `LINE-bot-sdk` & `gorgeous.py` on `Heroku`  
ゴー☆ジャスWebアプリ&LINEボット 〜キミのハートに、レボ☆リューション〜

## LINE-bot

ID: [@244wensq](http://nav.cx/4O8fsmz)

![gif](https://i.gyazo.com/6a41b54b6dcc0809dd408499e7a9aedf.gif)

## Web App

[<https://gorgeous-app.herokuapp.com/>](https://gorgeous-app.herokuapp.com/)

![gif](https://i.gyazo.com/12737d67a9fef0beacdd6a5e20d7fb80.gif)

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
