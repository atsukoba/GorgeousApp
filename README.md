# GorgeousApp [![App:Gorgeous](https://img.shields.io/badge/App-Gorgeous-5a00b4.svg?longCache=true)](https://gorgeous-app.herokuapp.com) [![App:LINEbot](https://img.shields.io/badge/App-LINEbot-1dcd00.svg?longCache=true)](http://nav.cx/4O8fsmz) ![Deployed on:Heroku](https://img.shields.io/badge/Deployed-Heroku-ff69b4.svg?longCache=true)

Gor☆geous Web Application and LINE bot with `flask` and `LINE-bot-sdk` on `Heroku`

## Web App

[<https://gorgeous-app.herokuapp.com/>](https://gorgeous-app.herokuapp.com/)

![gif](https://i.gyazo.com/c63d4918607e97e777663fe4d4edc383.gif)

## LINE-bot <a href="http://nav.cx/4O8fsmz"><img src="https://scdn.line-apps.com/n/line_add_friends/btn/ja.png" alt="友だち追加" height="16" border="0"></a>

![gif](https://i.gyazo.com/6a41b54b6dcc0809dd408499e7a9aedf.gif)

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
