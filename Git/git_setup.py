

# ========== GIT УСТАНОВКА И НАЧАЛЬНАЯ НАСТРОЙКА ==========
# Шаги для установки и настройки Git, инициализации локального проекта и публикации личной ветки на GitHub.

# **1. УСТАНОВКА GIT И ДОБАВЛЕНИЕ В ПУТЬ СИСТЕМЫ**
#? MacOS:
#? Откройте терминал и выполните команду:
#!     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
#? Затем установите git:
#!     brew install git

#? Windows:
#? Скачайте установочный файл с https://git-scm.com и установите.

# **ПРОВЕРКА УСТАНОВКИ GIT**
#! После установки откройте терминал (или PowerShell) и проверьте версию Git:
#!     git --version

#! ========== НАСТРОЙКА ОСНОВНЫХ НАСТРОЕК ==========
#! Настройте глобальные параметры пользователя Git:
#!     git config --global user.name "Ваше Имя"
#!     git config --global user.email "ваш.email@пример.com"

#* ========== ИНИЦИАЛИЗАЦИЯ ЛОКАЛЬНОГО РЕПОЗИТОРИЯ ==========
#? Перейдите в папку вашего проекта в терминале и выполните:
#!     git init (если git --version работает)
#? Это создаст скрытую папку .git и сделает ваш проект репозиторием Git. (Т.е на вашем устройстве будет создан ГИТ проект)

# **ДОБАВЛЕНИЕ ФАЙЛОВ ДЛЯ ОТСЛЕЖИВАНИЯ**
#? Проверьте статус проекта:
#!     git status
#? Добавьте файлы в "stage" для первого коммита:
#?!    git add .
#? Создайте начальный коммит с сообщением:
#!     git commit -m "Initial commit"

#?   git config --global user.email "bekzatdikhanov@gmail.com"
#?   git config --global user.name "bex200"


# **ДОБАВЛЕНИЕ УДАЛЕННОГО РЕПОЗИТОРИЯ**
#? Свяжите локальный репозиторий с GitHub, добавив удаленный репозиторий :
#!     git remote add origin https://github.com/bex200/pass_generator.git


#* ========== СОЗДАНИЕ И ПУБЛИКАЦИЯ ПЕРСОНАЛЬНОЙ ВЕТКИ ==========
#? Создайте новую ветку для разработки (name-dev):
#!     git branch имя-dev
#? Переключитесь на свою новую ветку:
#!     git checkout имя-dev

# **ПРОВЕРКА ТЕКУЩЕЙ ВЕТКИ**
#? Убедитесь, что вы находитесь на своей ветке:
#!     git branch

#* ========== ПУБЛИКАЦИЯ ВАШЕЙ ВЕТКИ НА GITHUB ==========
#? Отправьте ваши изменения в удаленную ветку:
#!     git push -u origin name-dev

#* Теперь ваша личная ветка опубликована на GitHub!
#* Вы можете продолжить работу в своей ветке, делая коммиты и выполняя push.
#* Чтобы в будущем выполнять push, достаточно использовать команду:
#!     git push
