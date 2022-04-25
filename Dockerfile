FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./check_generation_service .
EXPOSE 8000