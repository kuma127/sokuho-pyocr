# sokuho-pyocr

## build dockerfile

$ docker build -t sokuho/jupyter .

## starting server

$ docker run -v <current_directory>:/home/jovyan/work --name sokuho -p 8888:8888 sokuho/jupyter
