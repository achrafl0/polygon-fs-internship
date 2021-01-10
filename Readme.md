# Polygon Full Stack Internship Assessment

## Roadmap
- [x] Initialize backend
- [x] Initialize frontend
- [x] Read documentation about FastAPI
- [x] Make the docker containers
- [x] Create mock first layout in front
- [x] Create the middleware in the backend
- [x] Add the business logic in the back to compute the metrics
- [x] Create Mock Data in front to test the display
- [x] Create the API Client in the frontend
- [x] Link the Front to the back
- [ ] Hope that Meryll likes my work 

## How does it work
At first, I wanted to have a default route to add my logger, but then I realized that wasn't optimal, as the more routes we have, the more copied code we'd have, and that's a big no no.  

I then remembered that middlewares run before every request is resolved, so that was the best place to implement this.  
I've then started working on implementing that middleware.

For the frontend, I wanted to keep it simple and replicate the given wireframes, once I had something like that, I started working on the backend 

## What can be Improved
### Backend
- Use ElasticSearch, Kibana and Logstash to keep track of our logs
- Add more metrics to keep track of ( status codes, most requested routes, payload size ?)
- Make SQL queries for AVG/MIN/MAX instead of calculating them to reduce overhead
- Find a way to automatically generate typescript types using the pydantic types if we scale our application 
### Frontend
- We could replace the front service by Server Side Rendering using Nuxt
- Add graphs using Chart.js or D3.js or some other library to display the metrics we had
- Add display alerts if no data is found or an error happened 
- There is no loading state, we could use skeleton loaders from Vuetify to add that
- Add a .env.template instead of pushing the real .env if we have sensitive data ( for now it's okay it's just the API URL but this should change in the future )

## Settings
Most of the backend settings can be changed in ```app.core.settings```  
