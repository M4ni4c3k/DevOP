FROM python:3.12-alpine
WORKDIR /workspaces/DevOP
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "test.py"]