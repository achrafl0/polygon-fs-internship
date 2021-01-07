FROM python:3.7
COPY . ./polygon-perf-back
WORKDIR ./polygon-perf-back
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 1337
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "1337"]
