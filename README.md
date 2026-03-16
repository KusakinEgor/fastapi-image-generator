<h1 align="center" style="display: block; font-size: 2.5em; font-weight: bold; margin-block-start: 1em; margin-block-end: 1em;">
  <a name="logo">
    <img src="pictures/icon.png" style="width:100%;height:100%"/>
  </a>
  <br /><br />
  <strong>FastAPI Image Generator</strong>
</h1>

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)

</div>

FastAPI Image Generator - это RESTful API-сервис, позволяющий пользователям генерировать изображения на основе текстового описания (prompt).<br>

Проект реализован с использованием FastAPI, включает полноценную систему аутентификации на основе JWT, регистрацию, логин и хранение истории генераций. Ползьователь может авторизоваться, отправить текстовый запрос, получить до 10 изображений за раз и просматривать свою историю генераций.<br>

Также предусмотрены механизмы расширения: планируется реализация тегов, оценки изображений, админ-панели и контейнеризация через Docker.

---

## Функциональность
- 🔐 Регистрация и логин пользователей (JWT)
- 🧠 Генерация изображений по текстовому запросу (ограничение — до 10)
- 📜 История генераций для каждого пользователя
- 👤 Разграничение доступа по ролям

---

## Админ-панель
Для реализации админ-панели используется библиотека sqladmin - современный и удобный административный интерфейс для `FastAPI` и `SQLAlchemy`. С помощью `sqladmin` администраторы могут легко управлять данными в базе, создавать, редактировать и удалять записи, а также быстро просматривать историю генераций пользователей. Это позволяет значительно упростить администрирование и повысить эффективность работы без необходимости писать собственный интерфейс с нуля.

![Пример админ-панели](pictures/panel.PNG)

Описание: Главный экран админ-панели

![Информация о пользователях](pictures/admin.PNG)

Описание: Вид админ-панели после входа админа в систему

---

## Пример сгенерированного изображения

<p align="center">
    <img src="static/images/f0aeccea51a442d0a6055f5c3aadc5f2.png" alt="Пример сгенерированного изображения">
</p>

Описание: Результат генерации по запросу "A cat in space"

---

<p align="center">
    <img src="static/images/57a9f216dd9a4e3f8219f062119483f4.png" alt="Пример сгенерированного изображения">
</p>

Описание: Результат генерации по запросу "A farmer and his wife"

---

## Архитектура и структура

Проект организован по модульному принципу:
- `routes` - обработка HTTP-запросов
- `models/schemas` - описания моделей данных (ORM и Pydantic)
- `service` - логика генерации изображений
- Авторизация реализована черезе OAuth2 с JWT-токенами
- Данные хранятся в базе PostgreSQL

---

## Стек технологий
- [![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)

- [![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)

- [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-000000?logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)

- [![Pydantic](https://img.shields.io/badge/Pydantic-176DC3?logo=pydantic&logoColor=white)](https://pydantic-docs.helpmanual.io/)

- [![JWT](https://img.shields.io/badge/JWT-000000?logo=json-web-tokens&logoColor=white)](https://jwt.io/)

- [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)

- [![Alembic](https://img.shields.io/badge/Alembic-2C3E50?logo=alembic&logoColor=white)](https://alembic.sqlalchemy.org/)

---

## Установка и запуск

```bash
# Клонировать проект
git clone https://github.com/KusakinEgor/fastapi-image-generator.git
cd fastapi-image-generator

# Создать и активировать виртуальное окружение
python -m venv venv
source venv/bin/activate      # для Linux/macOS
venv\Scripts\activate         # для Windows

# Установить зависимости
pip install -r requirements.txt

# Инициализировать миграции
alembic init alembic

# Создать миграцию
alembic revision --autogenerate -m "init"

# Применить миграцию
alembic upgrade head

# Запустить сервер
uvicorn app.main:app --reload
```

## Настройка переменных окружения
Для корректной работы приложения необходимо создать файл `.env` с конфигурационными параметрами.

1. Скоируйте файл-шаблон `.env.example` в новый файл `.env` в корне проекта:
   ```bash
   cp .env.example .env # для Linux/macOS
   copy .env.example .env
   ```
2. Откройте файл `.env` и отредактируйте значения переменных под свои нужды. Файл содержит основные настройки, например:
   ```ini
   DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
   SECRET_KEY=ваш_секретный_ключ
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```


---

## Использование GPU с CUDA (рекомендуется)

Для ускоренной генерации изображений проект может использовать видеокарту NVIDIA с поддержкой CUDA.

### Шаги для настройки:

- Убедитесь, что на компьютере установлены **драйверы NVIDIA** и **CUDA ToolKit** соответстующей версии.
- Установите Pytorch с поддержкой CUDA. Например, для CUDA 12.6 выполните:

```bash
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
```

> Полезная ссылка: https://pytorch.org/get-started/locally/

### Важные замечания

- Попытка загрузить модель на CUDA без установленного PyTorch с поддержкой CUDA вызовет ошибку:
  ```vbnet
  AssertionError: Torch not compiled with CUDA enabled
  ```
- Убедитесь, что версия PyTorch и CUDA совместимы с вашей видеокартой.
---

## Использование CPU (если GPU отсутствует или не нужен)

Если у вас нет видеокарты с поддержкой CUDA или вы не хотите использовать GPU, можно работать на CPU.

### Шаги для настройки:

- Установите CPU-версию PyTorch:
  ```bash
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
  ```
- В каталоге `services` укажите устройство CPU:
  ```python
  pipe = pipe.to("cpu")
  ```
- Генерация будет работать но значительно медленнее, чем на GPU.

> Вопрос: А можно без установки CPU-версии? Да, можно и без явного указания `--index-url` в файле `requirements.txt` указаны все нужные пакеты для работы проекта. Но nтогда pip установит ту версию PyTorch, которая подходит под твою систему по умолчанию. Если у тебя CUDA не установлена или не поддерживается, он обычно поставит CPU-версию автоматическию.<br>
<strong>Минус:</strong> без явного указания могут ингогда подтягиваться версии с CUDA (если у тебя установлены CUDA-драйверы), и тогда будет ошибка при запуске, если PyTorch не собран с CUDA.<br>
Поэтому явное указание индекса на CPU-версию - это способ гарантировать, что будет именно CPU-сборка.

---

## Настройка Alembic (миграции БД)

Для управления миграциями в проекте используется Alembic.

### Конфигурация

- Файл `alembic.ini` содержит основные настройки подключения к базе данных.
  ```python
  sqlalchemy.url = postgresql+psycopg2://username:password@localhost:port/dbname
  ```

- Файл `alembic/env.py` отвечает за интеграцию Alembic с вашим SQLAlchemy-моделями и контекстом БД.
  ```python
  from app.database import Base
  from app.models import Client, Image, ImageTag, AdminAction, AuthToken, Tag, Rating, PromptRequest, History
  
  target_metadata = Base.metadata
  ```

> Важно:
> В `alembic.ini` нужно указать правильную строку подключения к вашей базе данных (например, PostgreSQL или SQLite).

### Как исползовать миграции

Создать новую миграцию (после изменений в моделях):

```bash
alembic revision --autogenerate -m "Описание миграции"
```
Применить миграции к базе:

```bash
alembic upgrade head
```
Откатить миграцию (если нужно):
```bash
alembic downgrade -1
```

> 💡 **Совет:**
> Для корректной работы Alembic в `env.py`:
> - Импортируйте все SQLAlchemy-модели (иначе Alembic не увидит изменения)
> - Убедитесь, что инициализирован движок SQLAlchemy (engine)

---

## Аунтификация
1. Зарегистрироваться через `/register`
2. Получить токен через `/token` (OAuth2PasswordRequest Form)
3. Использовать токен как `Bearer <token>` в заголовке Authorization
