FROM python:2.7
RUN pip install -r requirements.txt

EXPOSE 2020
CMD ["python", "/app.py"]