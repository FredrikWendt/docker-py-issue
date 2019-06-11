ceda@x1c5:/tmp/bugg$ ./doit.sh 
Running virtualenv with interpreter /usr/bin/python2
New python executable in /tmp/bugg/.venv/bin/python2
Also creating executable in /tmp/bugg/.venv/bin/python
Installing setuptools, pkg_resources, pip, wheel...done.
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.
Collecting pyopenssl (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/01/c8/ceb170d81bd3941cbeb9940fc6cc2ef2ca4288d0ca8929ea4db5905d904d/pyOpenSSL-19.0.0-py2.py3-none-any.whl
Collecting gitpython (from -r requirements.txt (line 2))
  Using cached https://files.pythonhosted.org/packages/fe/e5/fafe827507644c32d6dc553a1c435cdf882e0c28918a5bab29f7fbebfb70/GitPython-2.1.11-py2.py3-none-any.whl
Collecting docker (from -r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/91/93/310fe092039f6b0759a1f8524e9e2c56f8012804fa2a8da4e4289bb74d7c/docker-4.0.1-py2.py3-none-any.whl
Collecting behave (from -r requirements.txt (line 4))
  Using cached https://files.pythonhosted.org/packages/a8/6c/ec9169548b6c4cb877aaa6773408ca08ae2a282805b958dbc163cb19822d/behave-1.2.6-py2.py3-none-any.whl
Collecting pyhamcrest (from -r requirements.txt (line 5))
  Using cached https://files.pythonhosted.org/packages/9a/d5/d37fd731b7d0e91afcc84577edeccf4638b4f9b82f5ffe2f8b62e2ddc609/PyHamcrest-1.9.0-py2.py3-none-any.whl
Collecting pyaml (from -r requirements.txt (line 6))
  Using cached https://files.pythonhosted.org/packages/33/1a/936074f3492156693fc9e471269fc5747fa3b7d9d7f8a33af054f6b24066/pyaml-19.4.1-py2.py3-none-any.whl
Collecting cryptography>=2.3 (from pyopenssl->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/e6/68/50698ce24c61db7d44d93a5043c621a0ca7839d4ef9dff913e6ab465fc92/cryptography-2.7-cp27-cp27mu-manylinux1_x86_64.whl
Collecting six>=1.5.2 (from pyopenssl->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Collecting gitdb2>=2.0.0 (from gitpython->-r requirements.txt (line 2))
  Using cached https://files.pythonhosted.org/packages/da/30/a407568aa8d8f25db817cf50121a958722f3fc5f87e3a6fba1f40c0633e3/gitdb2-2.0.5-py2.py3-none-any.whl
Collecting ipaddress>=1.0.16; python_version < "3.3" (from docker->-r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/fc/d0/7fc3a811e011d4b388be48a0e381db8d990042df54aa4ef4599a31d39853/ipaddress-1.0.22-py2.py3-none-any.whl
Collecting requests!=2.18.0,>=2.14.2 (from docker->-r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/51/bd/23c926cd341ea6b7dd0b2a00aba99ae0f828be89d72b2190f27c11d4b7fb/requests-2.22.0-py2.py3-none-any.whl
Collecting websocket-client>=0.32.0 (from docker->-r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/29/19/44753eab1fdb50770ac69605527e8859468f3c0fd7dc5a76dd9c4dbd7906/websocket_client-0.56.0-py2.py3-none-any.whl
Collecting backports.ssl-match-hostname>=3.5; python_version < "3.5" (from docker->-r requirements.txt (line 3))
Collecting enum34; python_version < "3.4" (from behave->-r requirements.txt (line 4))
  Using cached https://files.pythonhosted.org/packages/c5/db/e56e6b4bbac7c4a06de1c50de6fe1ef3810018ae11732a50f15f62c7d050/enum34-1.1.6-py2-none-any.whl
Collecting traceback2; python_version < "3.0" (from behave->-r requirements.txt (line 4))
  Using cached https://files.pythonhosted.org/packages/17/0a/6ac05a3723017a967193456a2efa0aa9ac4b51456891af1e2353bb9de21e/traceback2-1.4.0-py2.py3-none-any.whl
Collecting parse-type>=0.4.2 (from behave->-r requirements.txt (line 4))
  Using cached https://files.pythonhosted.org/packages/a2/c9/e6fd8092a5a06f2519ec434ca8e9e42238384f64c9b659456d98b0593b89/parse_type-0.4.2-py2.py3-none-any.whl
Collecting parse>=1.8.2 (from behave->-r requirements.txt (line 4))
Requirement already satisfied: setuptools in ./.venv/lib/python2.7/site-packages (from pyhamcrest->-r requirements.txt (line 5)) (41.0.1)
Collecting PyYAML (from pyaml->-r requirements.txt (line 6))
Collecting asn1crypto>=0.21.0 (from cryptography>=2.3->pyopenssl->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/ea/cd/35485615f45f30a510576f1a56d1e0a7ad7bd8ab5ed7cdc600ef7cd06222/asn1crypto-0.24.0-py2.py3-none-any.whl
Collecting cffi!=1.11.3,>=1.8 (from cryptography>=2.3->pyopenssl->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/8d/e9/0c8afd1579e5cf7bc0f06fbcd7cdb954cbc0baadd505973949a99337da1c/cffi-1.12.3-cp27-cp27mu-manylinux1_x86_64.whl
Collecting smmap2>=2.0.0 (from gitdb2>=2.0.0->gitpython->-r requirements.txt (line 2))
  Using cached https://files.pythonhosted.org/packages/55/d2/866d45e3a121ee15a1dc013824d58072fd5c7799c9c34d01378eb262ca8f/smmap2-2.0.5-py2.py3-none-any.whl
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 (from requests!=2.18.0,>=2.14.2->docker->-r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/e6/60/247f23a7121ae632d62811ba7f273d0e58972d75e58a94d329d51550a47d/urllib3-1.25.3-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests!=2.18.0,>=2.14.2->docker->-r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/60/75/f692a584e85b7eaba0e03827b3d51f45f571c2e793dd731e598828d380aa/certifi-2019.3.9-py2.py3-none-any.whl
Collecting chardet<3.1.0,>=3.0.2 (from requests!=2.18.0,>=2.14.2->docker->-r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl
Collecting idna<2.9,>=2.5 (from requests!=2.18.0,>=2.14.2->docker->-r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl
Collecting linecache2 (from traceback2; python_version < "3.0"->behave->-r requirements.txt (line 4))
  Using cached https://files.pythonhosted.org/packages/c7/a3/c5da2a44c85bfbb6eebcfc1dde24933f8704441b98fdde6528f4831757a6/linecache2-1.0.0-py2.py3-none-any.whl
Collecting pycparser (from cffi!=1.11.3,>=1.8->cryptography>=2.3->pyopenssl->-r requirements.txt (line 1))
Installing collected packages: asn1crypto, enum34, ipaddress, pycparser, cffi, six, cryptography, pyopenssl, smmap2, gitdb2, gitpython, urllib3, certifi, chardet, idna, requests, websocket-client, backports.ssl-match-hostname, docker, linecache2, traceback2, parse, parse-type, behave, pyhamcrest, PyYAML, pyaml
Successfully installed PyYAML-5.1.1 asn1crypto-0.24.0 backports.ssl-match-hostname-3.7.0.1 behave-1.2.6 certifi-2019.3.9 cffi-1.12.3 chardet-3.0.4 cryptography-2.7 docker-4.0.1 enum34-1.1.6 gitdb2-2.0.5 gitpython-2.1.11 idna-2.8 ipaddress-1.0.22 linecache2-1.0.0 parse-1.12.0 parse-type-0.4.2 pyaml-19.4.1 pycparser-2.19 pyhamcrest-1.9.0 pyopenssl-19.0.0 requests-2.22.0 six-1.12.0 smmap2-2.0.5 traceback2-1.4.0 urllib3-1.25.3 websocket-client-0.56.0
DEBUG:docker.utils.config:Trying paths: ['/home/ceda/.docker/config.json', '/home/ceda/.dockercfg']
DEBUG:docker.utils.config:No config file found
DEBUG:docker.utils.config:Trying paths: ['/home/ceda/.docker/config.json', '/home/ceda/.dockercfg']
DEBUG:docker.utils.config:No config file found
INFO:root:Doing it
DEBUG:urllib3.connectionpool:http://localhost:None "GET /v1.35/images/letsencrypt_certbot_aws_1560252221/json HTTP/1.1" 404 122
INFO:root:Building docker image letsencrypt_certbot_aws_1560252221
DEBUG:docker.api.build:Looking for auth config
DEBUG:docker.api.build:No auth config in memory - loading from filesystem
DEBUG:docker.utils.config:Trying paths: ['/home/ceda/.docker/config.json', '/home/ceda/.dockercfg']
DEBUG:docker.utils.config:No config file found
DEBUG:docker.api.build:Sending auth config ()
DEBUG:urllib3.connectionpool:http://localhost:None "POST /v1.35/build?q=False&pull=False&t=letsencrypt_certbot_aws_1560252221&nocache=False&forcerm=False&rm=False HTTP/1.1" 200 None
DEBUG:urllib3.connectionpool:http://localhost:None "GET /v1.35/images/82dbe189e8df/json HTTP/1.1" 200 None
INFO:root:Doing work /to-be-run-in-container.sh in container based on image: letsencrypt_certbot_aws_1560252221
DEBUG:urllib3.connectionpool:http://localhost:None "POST /v1.35/containers/create HTTP/1.1" 201 90
DEBUG:urllib3.connectionpool:http://localhost:None "GET /v1.35/containers/db7aad8d93bbcc041b58833cd6204b31efe704c15212f1065c3e85e8ba45ec48/json HTTP/1.1" 200 None
DEBUG:urllib3.connectionpool:http://localhost:None "POST /v1.35/containers/db7aad8d93bbcc041b58833cd6204b31efe704c15212f1065c3e85e8ba45ec48/start HTTP/1.1" 204 0
INFO:root:Sleeping for some time, so container can really be stopped
INFO:root:Waiting for container <Container: db7aad8d93> - usually takes a minute
DEBUG:urllib3.connectionpool:http://localhost:None "POST /v1.35/containers/db7aad8d93bbcc041b58833cd6204b31efe704c15212f1065c3e85e8ba45ec48/wait HTTP/1.1" 200 17
INFO:root:Container <Container: db7aad8d93> done - here comes the logs:
DEBUG:urllib3.connectionpool:http://localhost:None "GET /v1.35/containers/db7aad8d93bbcc041b58833cd6204b31efe704c15212f1065c3e85e8ba45ec48/logs?timestamps=0&tail=all&follow=0&stderr=1&stdout=1 HTTP/1.1" 200 None
DEBUG:urllib3.connectionpool:http://localhost:None "GET /v1.35/containers/db7aad8d93bbcc041b58833cd6204b31efe704c15212f1065c3e85e8ba45ec48/json HTTP/1.1" 200 None
INFO:root:search wendt.vpn lotsgatan lan home
nameserver 10.0.0.2
nameserver 8.8.8.8
Copying to /etc/letsencrypt
/etc/letsencrypt:
total 12
drwxr-xr-x    3 root     root          4096 Jun 11 11:23 .
drwxr-xr-x   25 root     root          4096 Jun 11 11:23 ..
drwxr-xr-x    3 root     root          4096 Jun 11 11:23 archive

/etc/letsencrypt/archive:
total 12
drwxr-xr-x    3 root     root          4096 Jun 11 11:23 .
drwxr-xr-x    3 root     root          4096 Jun 11 11:23 ..
drwxr-xr-x    2 root     root          4096 Jun 11 11:23 some.domain

/etc/letsencrypt/archive/some.domain:
total 12
drwxr-xr-x    2 root     root          4096 Jun 11 11:23 .
drwxr-xr-x    3 root     root          4096 Jun 11 11:23 ..
-rw-r--r--    1 root     root            75 Jun 11 11:23 resolv.conf
All done inside the container, moving on!

DEBUG:root:Extracting files
DEBUG:urllib3.connectionpool:http://localhost:None "GET /v1.35/containers/db7aad8d93bbcc041b58833cd6204b31efe704c15212f1065c3e85e8ba45ec48/archive?path=%2Fetc%2Fletsencrypt%2F HTTP/1.1" 200 None
DEBUG:root:<TarInfo 'letsencrypt' at 0x7f4829fa06d0>
DEBUG:root:<TarInfo 'letsencrypt/archive' at 0x7f482a806810>
DEBUG:root:<TarInfo 'letsencrypt/archive/some.domain' at 0x7f4829fa0250>
DEBUG:root:<TarInfo 'letsencrypt/archive/some.domain/resolv.conf' at 0x7f4829fa0750>
DEBUG:root:Found tar file member <TarInfo 'letsencrypt' at 0x7f4829fa06d0>
DEBUG:root:Found tar file member <TarInfo 'letsencrypt/archive' at 0x7f482a806810>
DEBUG:root:Found tar file member <TarInfo 'letsencrypt/archive/some.domain' at 0x7f4829fa0250>
DEBUG:root:Found tar file member <TarInfo 'letsencrypt/archive/some.domain/resolv.conf' at 0x7f4829fa0750>
DEBUG:root:Saving file untarred/resolv.conf
DEBUG:root:Removing container <Container: db7aad8d93>
DEBUG:urllib3.connectionpool:http://localhost:None "DELETE /v1.35/containers/db7aad8d93bbcc041b58833cd6204b31efe704c15212f1065c3e85e8ba45ec48?force=False&link=False&v=False HTTP/1.1" 204 0
DEBUG:root:Removing docker image letsencrypt_certbot_aws_1560252221
DEBUG:urllib3.connectionpool:http://localhost:None "GET /v1.35/images/letsencrypt_certbot_aws_1560252221/json HTTP/1.1" 200 None
DEBUG:urllib3.connectionpool:http://localhost:None "DELETE /v1.35/images/letsencrypt_certbot_aws_1560252221?noprune=False&force=False HTTP/1.1" 200 231
ceda@x1c5:/tmp/bugg$ docker -v
Docker version 17.05.0-ce-rc3, build 90d35ab
ceda@x1c5:/tmp/bugg$ pip freeze 
adns-python==1.2.1
ansible==2.5.1
apache-libcloud==2.2.1
asn1crypto==0.24.0
attrs==17.4.0
awslogs==0.10.0
backports.ssl-match-hostname==3.5.0.1
beautifulsoup4==4.6.0
boto3==1.9.50
botocore==1.12.50
cached-property==1.3.1
certifi==2017.11.5
chardet==3.0.4
coverage==4.5
cryptography==2.1.4
docker==2.7.0
docker-compose==1.18.0
docker-pycreds==0.2.1
dockerpty==0.4.1
docopt==0.6.2
docutils==0.14
enum34==1.1.6
funcsigs==1.0.2
functools32==3.2.3.post2
futures==3.2.0
GeoIP==1.3.2
html5lib==0.999999999
httplib2==0.9.2
idna==2.6
ipaddress==1.0.17
IPy==0.83
Jinja2==2.10
jmespath==0.9.3
jsonschema==2.6.0
keyring==10.6.0
keyrings.alt==3.0
lockfile==0.12.2
lxml==4.2.1
MarkupSafe==1.0
mysql-connector-python==2.1.6
mysql-utilities==1.6.4
netaddr==0.7.19
nose2==0.7.4
notify2==0.3.1
numpy==1.13.3
paramiko==2.0.0
pem==17.1.0
pexpect==4.2.1
pluggy==0.6.0
pritunl-client==1.0.1568.9
py==1.5.2
pyasn1==0.4.2
pycairo==1.16.2
pycrypto==2.6.1
pycurl==7.43.0.1
pygobject==3.26.1
pykerberos==1.1.14
pyodbc==4.0.17
pyOpenSSL==17.5.0
pysqlite==2.7.0
pytest==3.3.2
python-apt==1.6.4
python-dateutil==2.7.5
python-magic==0.4.15
pyxdg==0.25
PyYAML==3.12
requests==2.18.4
s3cmd==2.0.2
s3transfer==0.1.13
scour==0.36
SecretStorage==2.3.1
simplejson==3.13.2
six==1.11.0
termcolor==1.1.0
texttable==0.9.1
urllib3==1.24.1
webencodings==0.5
websocket-client==0.46.0
xmltodict==0.11.0
ceda@x1c5:/tmp/bugg$ cat /etc/lsb-release 
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=18.04
DISTRIB_CODENAME=bionic
DISTRIB_DESCRIPTION="Ubuntu 18.04.2 LTS"
