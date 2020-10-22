FROM python:3.6.1-alpine
RUN pip install flask
COPY img.py /img.py
CMD ["python","img"]
