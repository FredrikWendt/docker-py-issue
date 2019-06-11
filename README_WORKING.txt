ceda@x1c5:/tmp/bugg$ ./doit.sh 
DEBUG:docker.utils.config:Trying paths: ['/home/ceda/.docker/config.json', '/home/ceda/.dockercfg']
DEBUG:docker.utils.config:No config file found
DEBUG:docker.utils.config:Trying paths: ['/home/ceda/.docker/config.json', '/home/ceda/.dockercfg']
DEBUG:docker.utils.config:No config file found
INFO:root:Doing it
DEBUG:urllib3.connectionpool:http://localhost:None "GET /v1.35/images/letsencrypt_certbot_aws_1560251966/json HTTP/1.1" 404 122
INFO:root:Building docker image letsencrypt_certbot_aws_1560251966
DEBUG:docker.api.build:Looking for auth config
DEBUG:docker.api.build:No auth config in memory - loading from filesystem
DEBUG:docker.utils.config:Trying paths: ['/home/ceda/.docker/config.json', '/home/ceda/.dockercfg']
DEBUG:docker.utils.config:No config file found
DEBUG:docker.api.build:Sending auth config ()
DEBUG:urllib3.connectionpool:http://localhost:None "POST /v1.35/build?q=False&pull=False&t=letsencrypt_certbot_aws_1560251966&nocache=False&forcerm=False&rm=False HTTP/1.1" 200 None
DEBUG:urllib3.connectionpool:http://localhost:None "GET /v1.35/images/5cb6e97107e1/json HTTP/1.1" 200 None
INFO:root:Doing work /to-be-run-in-container.sh in container based on image: letsencrypt_certbot_aws_1560251966
DEBUG:urllib3.connectionpool:http://localhost:None "POST /v1.35/containers/create HTTP/1.1" 201 90
DEBUG:urllib3.connectionpool:http://localhost:None "GET /v1.35/containers/fee170d32072ab4a252a11a0b91e0a3f6d82050bb4cbe7289fafa0aac7dcc910/json HTTP/1.1" 200 None
DEBUG:urllib3.connectionpool:http://localhost:None "POST /v1.35/containers/fee170d32072ab4a252a11a0b91e0a3f6d82050bb4cbe7289fafa0aac7dcc910/start HTTP/1.1" 204 0
INFO:root:Sleeping for some time, so container can really be stopped
INFO:root:Waiting for container <Container: fee170d320> - usually takes a minute
DEBUG:urllib3.connectionpool:http://localhost:None "POST /v1.35/containers/fee170d32072ab4a252a11a0b91e0a3f6d82050bb4cbe7289fafa0aac7dcc910/wait HTTP/1.1" 200 17
INFO:root:Container <Container: fee170d320> done - here comes the logs:
DEBUG:urllib3.connectionpool:http://localhost:None "GET /v1.35/containers/fee170d32072ab4a252a11a0b91e0a3f6d82050bb4cbe7289fafa0aac7dcc910/logs?timestamps=0&tail=all&follow=0&stderr=1&stdout=1 HTTP/1.1" 200 None
DEBUG:urllib3.connectionpool:http://localhost:None "GET /v1.35/containers/fee170d32072ab4a252a11a0b91e0a3f6d82050bb4cbe7289fafa0aac7dcc910/json HTTP/1.1" 200 None
INFO:root:search wendt.vpn lotsgatan lan home
nameserver 10.0.0.2
nameserver 8.8.8.8
Copying to /etc/letsencrypt
/etc/letsencrypt:
total 12
drwxr-xr-x    3 root     root          4096 Jun 11 11:19 .
drwxr-xr-x   25 root     root          4096 Jun 11 11:19 ..
drwxr-xr-x    3 root     root          4096 Jun 11 11:19 archive

/etc/letsencrypt/archive:
total 12
drwxr-xr-x    3 root     root          4096 Jun 11 11:19 .
drwxr-xr-x    3 root     root          4096 Jun 11 11:19 ..
drwxr-xr-x    2 root     root          4096 Jun 11 11:19 some.domain

/etc/letsencrypt/archive/some.domain:
total 12
drwxr-xr-x    2 root     root          4096 Jun 11 11:19 .
drwxr-xr-x    3 root     root          4096 Jun 11 11:19 ..
-rw-r--r--    1 root     root            75 Jun 11 11:19 resolv.conf
All done inside the container, moving on!

DEBUG:root:Extracting files
DEBUG:urllib3.connectionpool:http://localhost:None "GET /v1.35/containers/fee170d32072ab4a252a11a0b91e0a3f6d82050bb4cbe7289fafa0aac7dcc910/archive?path=%2Fetc%2Fletsencrypt%2F HTTP/1.1" 200 None
DEBUG:root:<TarInfo 'letsencrypt' at 0x7ff8c1b946d0>
DEBUG:root:<TarInfo 'letsencrypt/archive' at 0x7ff8c23fa810>
DEBUG:root:<TarInfo 'letsencrypt/archive/some.domain' at 0x7ff8c1b94250>
DEBUG:root:<TarInfo 'letsencrypt/archive/some.domain/resolv.conf' at 0x7ff8c1b94750>
DEBUG:root:Found tar file member <TarInfo 'letsencrypt' at 0x7ff8c1b946d0>
DEBUG:root:Found tar file member <TarInfo 'letsencrypt/archive' at 0x7ff8c23fa810>
DEBUG:root:Found tar file member <TarInfo 'letsencrypt/archive/some.domain' at 0x7ff8c1b94250>
DEBUG:root:Found tar file member <TarInfo 'letsencrypt/archive/some.domain/resolv.conf' at 0x7ff8c1b94750>
DEBUG:root:Saving file untarred/resolv.conf
DEBUG:root:Removing container <Container: fee170d320>
DEBUG:urllib3.connectionpool:http://localhost:None "DELETE /v1.35/containers/fee170d32072ab4a252a11a0b91e0a3f6d82050bb4cbe7289fafa0aac7dcc910?force=False&link=False&v=False HTTP/1.1" 204 0
DEBUG:root:Removing docker image letsencrypt_certbot_aws_1560251966
DEBUG:urllib3.connectionpool:http://localhost:None "GET /v1.35/images/letsencrypt_certbot_aws_1560251966/json HTTP/1.1" 200 None
DEBUG:urllib3.connectionpool:http://localhost:None "DELETE /v1.35/images/letsencrypt_certbot_aws_1560251966?noprune=False&force=False HTTP/1.1" 200 231
ceda@x1c5:/tmp/bugg$ docker -v
Docker version 17.05.0-ce-rc3, build 90d35ab
ceda@x1c5:/tmp/bugg$ cat /etc/lsb-release 
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=18.04
DISTRIB_CODENAME=bionic
DISTRIB_DESCRIPTION="Ubuntu 18.04.2 LTS"
