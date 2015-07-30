# Active system components version storage and visualization


## Webservice

 - PUT /update

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
docker run -d -p 80:80 active_versions:v2
```

After few seconds, open `http://<host>` to see the Flask app.


### Api

## Logging version changes

    !python
	>>>from requests import put
	>>>put('http://<host>/update', data={'systems':'system_type', 'components': 'component_name', 'version': 'value', 'source': 'author_name'})
    [response 200]
---

## Viewing Logs

for current component versions of all systems(dev|production|test)
`http://<host>/current`

for current versions of a component
`http://<host>/current/components/component_name`

for current components of a system(dev|production|test)
`http://<host>/current/systems/system_name`

for latest updates by a source
`http://<host>/current/source/source_name`


for all components of all system(dev|production|test)
`http://<host>/logs`

for all components of a system(dev|production|test)
`http://<host>/syslogs/system_name`

for all versions of a component
`http://<host>/logs/component_name`

for all components of by a source
`http://<host>/sourcelogs/source_name`

---

## Deleting Logs

you can simply use the delete button

---


##Tools used
nginx + gunicorn + flask
