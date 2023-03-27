# generate graph for docker-compose

______________________________________________________________________

## Table Of Content

<!--TOC-->

- [generate graph for docker-compose](#generate-graph-for-docker-compose)
  - [Table Of Content](#table-of-content)
  - [Makefile](#makefile)

<!--TOC-->

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
dev                                       run application on dev configuration without mounted sources                                         dev
help                                      This help dialog                                                                                     help
migrate                                   migrate models to database                                                                           migrate
outdated                                  outdated python packages                                                                             outdated
pre-commit                                run pre-commit                                                                                       pre-commit
prune                                     remove all stuff associated to project on docker                                                     prune
up-detach                                 run services without logs following                                                                  up-detach
up                                        run services with logs following                                                                     up
make[1]: Leaving directory '/mnt/d/onedrive/tests-tech/izeberg'
```

<!-- END makefile-doc -->
