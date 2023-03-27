# generate graph for docker-compose

______________________________________________________________________

## Table Of Content

<!--TOC-->

- [generate graph for docker-compose](#generate-graph-for-docker-compose)
  - [Table Of Content](#table-of-content)
  - [Admin panel](#admin-panel)
  - [Makefile](#makefile)

<!--TOC-->

## Admin panel

`http://127.0.0.1:8080/admin/`

user `admin`

password `admin`

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
