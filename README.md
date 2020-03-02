# sokuho-pyocr

## build dockerfile

$ docker build -t sokuho/jupyter .

## running server

$ docker run -v <current_directory>:/home/jovyan/work --name sokuho -p 8888:8888 sokuho/jupyter

## starting container

$ docker start -a sokuho

## enter the container

$ docker exec -it sokuho bash