FROM python:3.8-slim
COPY app.py .
COPY requirements.txt .
COPY model.pkl .
COPY startup.sh .
RUN pip install -r requirements.txt -q
EXPOSE 5000
ENTRYPOINT ["sh", "startup.sh"]