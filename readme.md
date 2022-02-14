### Подготовка к запуску

```
# прописывать в командной строке
pip install virtualenv # если не установлено
git clone git@github.com:YarMolenko13/predprof-project.git
cd predprof-project
python3 -m venv venv
.\venv\Scripts\activate
pip install -r  requirements.txt # установка всех зависимостей (не рекомендуется)
pip install flask # установка Flask
```

### Запуск

```
.\venv\Scripts\activate
python main.py 
# или для запуска без нейросети
python main_no_yolo.py  
```
