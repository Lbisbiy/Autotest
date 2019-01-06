# Запуск проекта

* Положить в папку проекта cromedriver

* Открыть проект в PyCharm

* Скачать и установить Allure

* Меню Run -> Edit Configurations...

* **Name:** test

* **Parameters:** test_main.py

* **Working directory:** <путь до папки с проектом>

* Запуск теста:
		pytest.test --alluredir reports

	Генерация отчета:
			allure generate -o reports reports

* Открыть index.html с помощью Mozilla Firefox
