# Active system components version storage and visualization

Log versions of active componects in your system through a JSON Api.




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

```bash
git clone https://github.com/Alafazam/versions
```

2. build using docker build -t active_versions:v2 .

```bash
docker build -t active_versions:v2 .
```


### Usage


starting without username and password
```bash
docker run -d -p 80:80 active_versions:v2
```



starting with user and pass
```bash
docker run -d -p -e user="USERNAME" -e pass="PASSWORD" 80:80 active_versions:v2
```


After few seconds, open `http://<host>` to see the Flask app.


### Adding new Columns
To add new columns you have to make changes in 3 files -> 

* Hello.py 

 Add the new column to the model, in line 52 and 64. 

 Add new column values to put and post request in line 260. 


* Current.html

 Add the new column to the table.


* Hello.html

 Add the new column to the table.



#Api

## Logging version changes

    !python
	>>>from requests import put
	>>>put('http://192.168.59.103/update', data={'systems':'dev', 'components': 'components 1', 'version': 'version 2.', 'source': 'alaf',   'user':'q','pass':'a'}).json()

    Done


## Viewing Logs

Current component versions of all systems(dev|production|test)

`http://<host>/current`

Current versions of a component

`http://<host>/current/components/component_name`

Current components of a system(dev|production|test)

`http://<host>/current/systems/system_name`

Latest updates by a source

`http://<host>/current/source/source_name`


All components of all system(dev|production|test)

`http://<host>/logs`

All components of a system(dev|production|test)

`http://<host>/syslogs/system_name`

All versions of a component

`http://<host>/logs/component_name`

All components of by a source

`http://<host>/sourcelogs/source_name`

---

## Deleting Logs

you can simply use the delete button from the web interface.

---
