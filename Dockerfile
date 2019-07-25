FROM python:3.6

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y \
    libmecab-dev mecab-ipadic-utf8 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# MeCab
WORKDIR /app
RUN git clone https://github.com/taku910/mecab.git
WORKDIR /app/mecab/mecab
RUN ./configure  --enable-utf8-only \
  && make \
  && make check \
  && make install \
  && ldconfig

# MeCab ipadic
WORKDIR /app/mecab/mecab-ipadic
RUN ./configure --with-charset=utf8 \
  && make \
  &&make install

# ipadic-NEologd
WORKDIR /app
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
WORKDIR /app/mecab-ipadic-neologd
RUN ./bin/install-mecab-ipadic-neologd -n -y

# python packages
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN python get_nations_data.py

# run api on gunicorn
WORKDIR /app
CMD ["gunicorn", "-w", "4", "app:__hug_wsgi__", "-b", "0.0.0.0:8000", "-t", "120"]
