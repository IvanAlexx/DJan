import logging

from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request, *args, **kwargs):
    response = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Мой первый Django-сайт</title>
</head>
<body>

<h1>Мой первый Django-сайт</h1>

<p>Этот сайт был создан с использованием фреймворка Django - для веб-разработки на Python.</p>

<h2>Обо мне</h2>

<p>Меня зовут Иван, я новичок в веб-разработке.</p>

</body>
</html>
    """
    logger.info("index page was requested")
    return HttpResponse(response)


def about(request, *args, **kwargs):
    response = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Обо мне</title>
</head>
<body>

<h1>Обо мне</h1>

<p>Привет! Меня зовут Иван, я начинаю заниматься программированием. Я изучаю программирование несколько лет.</p>

<p>Мне нравится решать задачи и писать красивый и чистый код.</p>

</body>
</html>
    """
    logger.info("about page was requested")
    return HttpResponse(response)
