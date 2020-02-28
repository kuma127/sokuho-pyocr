FROM jupyter/datascience-notebook

USER root
RUN sudo apt update && sudo apt -y install tesseract-ocr && \
    apt install tesseract-ocr-jpn && \
    apt install tesseract-ocr-script-jpan && \
    apt -y install libmecab-dev
WORKDIR /home/jovyan/work
COPY requirements.txt ./
RUN pip install -r requirements.txt
