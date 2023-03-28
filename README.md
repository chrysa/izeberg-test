# generate graph for docker-compose

______________________________________________________________________

## Table Of Content

<!--TOC-->

- [generate graph for docker-compose](#generate-graph-for-docker-compose)
  - [Table Of Content](#table-of-content)
  - [Docker Usage](#docker-usage)
  - [Remarques](#remarques)
  - [Postman](#postman)
  - [Evolution](#evolution)
  - [Admin panel](#admin-panel)
  - [Makefile](#makefile)

<!--TOC-->

## Docker Usage

`make build` puis `make dev`

le volume `sockets` contient le socket uwsgi qui permettrait de connecter l'application a un reverse proxy

## Remarques

personnellement j'aurais fait queLQues modifications pour respecter les standards

- j'ai plus tendance a ne pas mettre `/add/` `/remove/` dans les urls et utiliser les verbes rest

cependant gardant votre postulat

- la route `POST /api/group/<type>/add/`
  - le type ne devrait pas etre dans l'URL mais dans un payload ce qui permettrait aussi de pouvoir ajouter plusieurs types et de limiter les appels API et a la DB
  - une route `PATCH /api/group/update` devrait etre creer pour ajouter des groupes a un user existant

## Postman

ayant un soucis avec la fonctionnalite `browsable API` je vous fournit une collection postman `izeberg.postman_collection.json` pour faciliter le test de l'API

## Evolution

```
- ajout de tests unitaire
- ajout de documentation
- ajout de tests fonctionnels via postman
```

## Admin panel

`http://127.0.0.1:8080/admin/`

- user `admin`
- password `admin`

## Makefile

<!-- START makefile-doc -->

```
$ make help
make[1]: Entering directory '/mnt/d/onedrive/tests-tech/izeberg'
Hello to the Makefile

target                                   help                                                                                                 usage
------                                   ----                                                                                                 ----
build                                     build container                                                                                      build
connect-dev                               connect on dev container                                                                             connect-dev
create-admin                              create admin user
dev                                       run application on dev configuration without mounted sources                                         dev
down                                      run application on dev configuration without mounted sources                                         dev
help                                      This help dialog                                                                                     help
migrate                                   migrate models to database                                                                           migrate
outdated                                  outdated python packages                                                                             outdated
pre-commit                                run pre-commit                                                                                       pre-commit
prune                                     remove all stuff associated to project on docker                                                     prune
startapp                                  create new django app                                                                                startapp app_name#{app_name}
wsgi                                      run application on wsgi mod                                                                          wsgi
make[1]: Leaving directory '/mnt/d/onedrive/tests-tech/izeberg'
```

<!-- END makefile-doc -->
