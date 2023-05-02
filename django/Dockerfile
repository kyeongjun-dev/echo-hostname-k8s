FROM python:3.9-slim
RUN apt update -y && apt install -y curl jq
RUN pip install --upgrade pip && pip install django
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]