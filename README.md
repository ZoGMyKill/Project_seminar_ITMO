# Sattelite images semantic segmentation

Исследовательский проект от AIRI, затрагивает тему обработки спутниковых снимков. В частности, семантическая сегментация утечек метана. Подобные утечки возможны как и на трубопроводах, так и в естественной среде. Из-за утечек происходит потери при транспортировке, а также метан опасный парниковый газ, который значительно влияет на изменение климата.

## Начало работы

Эти инструкции помогут вам запустить копию проекта на вашем локальном компьютере для разработки и тестирования.

### Предварительные условия

Перед началом убедитесь, что у вас установлены:

- Docker
- Docker Compose

### Установка

Шаги по установке и настройке проекта:

1. Склонируйте репозиторий на ваш локальный компьютер:
    ```bash
    git clone https://github.com/ZoGMyKill/Project_seminar_ITMO
    ```
2. Перейдите в директорию проекта:
    ```bash
    cd Project_seminar_ITMO
    ```
3. Запустите все сервисы с помощью Docker Compose:
    ```bash
    docker-compose up --build
    ```
4. Откройте интерфейс Streamlit в браузере по адресу http://localhost:8501.

5. FastAPI будет доступен по адресу http://localhost:8000.


# Полезные мытериалы

[Все вегетативные индексы](https://www.indexdatabase.de/db/i.php)

[Учебник по интерпритации спутниковых снимков](http://www.psu.ru/files/docs/science/books/uchebnie-posobiya/shikhov-gerasimov-ponomarchuk-perminova-tematicheskoe-deshifrovanie-i-interpretaciya-kosmicheskih-snimkov.pdf)
