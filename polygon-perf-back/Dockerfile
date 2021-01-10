FROM python:3.7
COPY . ./polygon-perf-back
WORKDIR /polygon-perf-back
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
# We are adding the wait dependency here so we can wait out our db 
RUN chmod +x /wait
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 1337