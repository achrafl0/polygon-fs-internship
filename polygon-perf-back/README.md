# Backend server

## Stack 
- Python
- FastAPI
- SQLAlchemy


## Structure
We want to log data each request, and the middleware is always processed for all the routes and requests, so it made sense to create one to our needs.  
Our middleware logs each request and the time we need to process it so we can get performances stats afterwards on the ````/api/v1/perf```` 

## Ideas to improve the back later on
- Use ElasticSearch, Kibana and Logstash to keep track of our logs
- Add more metrics to keep track of ( status codes, most requested routes, payload size ?)
  
  