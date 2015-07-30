# Active system components version storage and visualization


## Webservice

 - PUT /version

 - JSON Fields
   + system : "dev" | "test" | "live"
   + component
   + version
   + timestamp
   + source
    



### Base Docker Image

* [ubuntu:12.04](https://registry.hub.docker.com/_/ubuntu/)


### Installation

1. Git clone from [repo](https://github.com/Alafazam/versions) .

2. build using docker build -t active_versions:v2 .

```bash
docker build -t active_versions:v2 .
```


### Usage

```bash
docker run -d -p 80:80 active_versions
```

After few seconds, open `http://<host>` to see the Flask app.
