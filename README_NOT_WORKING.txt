go@filserver:/var/lib/go-agent/pipelines/internet$ git clone https://github.com/FredrikWendt/docker-py-issue.git
Cloning into 'docker-py-issue'...
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 11 (delta 0), reused 11 (delta 0), pack-reused 0
Unpacking objects: 100% (11/11), done.
Checking connectivity... done.
go@filserver:/var/lib/go-agent/pipelines/internet$ cd docker-py-issue/
go@filserver:/var/lib/go-agent/pipelines/internet/docker-py-issue$ ls
doit.sh  issue.py  requirements.txt  src
go@filserver:/var/lib/go-agent/pipelines/internet/docker-py-issue$ ./doit.sh 
Running virtualenv with interpreter /usr/bin/python2
New python executable in /var/lib/go-agent/pipelines/internet/docker-py-issue/.venv/bin/python2
Also creating executable in /var/lib/go-agent/pipelines/internet/docker-py-issue/.venv/bin/python
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
Collecting six>=1.5.2 (from pyopenssl->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Collecting cryptography>=2.3 (from pyopenssl->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/e6/68/50698ce24c61db7d44d93a5043c621a0ca7839d4ef9dff913e6ab465fc92/cryptography-2.7-cp27-cp27mu-manylinux1_x86_64.whl
Collecting gitdb2>=2.0.0 (from gitpython->-r requirements.txt (line 2))
  Using cached https://files.pythonhosted.org/packages/da/30/a407568aa8d8f25db817cf50121a958722f3fc5f87e3a6fba1f40c0633e3/gitdb2-2.0.5-py2.py3-none-any.whl
Collecting ipaddress>=1.0.16; python_version < "3.3" (from docker->-r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/fc/d0/7fc3a811e011d4b388be48a0e381db8d990042df54aa4ef4599a31d39853/ipaddress-1.0.22-py2.py3-none-any.whl
Collecting backports.ssl-match-hostname>=3.5; python_version < "3.5" (from docker->-r requirements.txt (line 3))
Collecting requests!=2.18.0,>=2.14.2 (from docker->-r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/51/bd/23c926cd341ea6b7dd0b2a00aba99ae0f828be89d72b2190f27c11d4b7fb/requests-2.22.0-py2.py3-none-any.whl
Collecting websocket-client>=0.32.0 (from docker->-r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/29/19/44753eab1fdb50770ac69605527e8859468f3c0fd7dc5a76dd9c4dbd7906/websocket_client-0.56.0-py2.py3-none-any.whl
Collecting parse-type>=0.4.2 (from behave->-r requirements.txt (line 4))
  Using cached https://files.pythonhosted.org/packages/a2/c9/e6fd8092a5a06f2519ec434ca8e9e42238384f64c9b659456d98b0593b89/parse_type-0.4.2-py2.py3-none-any.whl
Collecting parse>=1.8.2 (from behave->-r requirements.txt (line 4))
Collecting enum34; python_version < "3.4" (from behave->-r requirements.txt (line 4))
  Using cached https://files.pythonhosted.org/packages/c5/db/e56e6b4bbac7c4a06de1c50de6fe1ef3810018ae11732a50f15f62c7d050/enum34-1.1.6-py2-none-any.whl
Collecting traceback2; python_version < "3.0" (from behave->-r requirements.txt (line 4))
  Using cached https://files.pythonhosted.org/packages/17/0a/6ac05a3723017a967193456a2efa0aa9ac4b51456891af1e2353bb9de21e/traceback2-1.4.0-py2.py3-none-any.whl
Requirement already satisfied: setuptools in ./.venv/lib/python2.7/site-packages (from pyhamcrest->-r requirements.txt (line 5)) (41.0.1)
Collecting PyYAML (from pyaml->-r requirements.txt (line 6))
Collecting cffi!=1.11.3,>=1.8 (from cryptography>=2.3->pyopenssl->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/8d/e9/0c8afd1579e5cf7bc0f06fbcd7cdb954cbc0baadd505973949a99337da1c/cffi-1.12.3-cp27-cp27mu-manylinux1_x86_64.whl
Collecting asn1crypto>=0.21.0 (from cryptography>=2.3->pyopenssl->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/ea/cd/35485615f45f30a510576f1a56d1e0a7ad7bd8ab5ed7cdc600ef7cd06222/asn1crypto-0.24.0-py2.py3-none-any.whl
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
Installing collected packages: six, enum34, pycparser, cffi, asn1crypto, ipaddress, cryptography, pyopenssl, smmap2, gitdb2, gitpython, backports.ssl-match-hostname, urllib3, certifi, chardet, idna, requests, websocket-client, docker, parse, parse-type, linecache2, traceback2, behave, pyhamcrest, PyYAML, pyaml
Successfully installed PyYAML-5.1.1 asn1crypto-0.24.0 backports.ssl-match-hostname-3.7.0.1 behave-1.2.6 certifi-2019.3.9 cffi-1.12.3 chardet-3.0.4 cryptography-2.7 docker-4.0.1 enum34-1.1.6 gitdb2-2.0.5 gitpython-2.1.11 idna-2.8 ipaddress-1.0.22 linecache2-1.0.0 parse-1.12.0 parse-type-0.4.2 pyaml-19.4.1 pycparser-2.19 pyhamcrest-1.9.0 pyopenssl-19.0.0 requests-2.22.0 six-1.12.0 smmap2-2.0.5 traceback2-1.4.0 urllib3-1.25.3 websocket-client-0.56.0
INFO:root:Doing it
INFO:root:Building docker image letsencrypt_certbot_aws_1560251740
INFO:root:Doing work /to-be-run-in-container.sh in container based on image: letsencrypt_certbot_aws_1560251740
INFO:root:Sleeping for some time, so container can really be stopped
INFO:root:Waiting for container <Container: 7e111e1ac7> - usually takes a minute
INFO:root:Container <Container: 7e111e1ac7> done - here comes the logs:
INFO:root:# Dynamic resolv.conf(5) file for glibc resolver(3) generated by resolvconf(8)
#     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE OVERWRITTEN
nameserver 10.20.30.44
search wendt.vpn

# tail
nameserver 192.168.1.254
Copying to /etc/letsencrypt
/etc/letsencrypt:
total 12
drwxr-xr-x    3 root     root          4096 Jun 11 11:15 .
drwxr-xr-x    1 root     root          4096 Jun 11 11:15 ..
drwxr-xr-x    3 root     root          4096 Jun 11 11:15 archive

/etc/letsencrypt/archive:
total 12
drwxr-xr-x    3 root     root          4096 Jun 11 11:15 .
drwxr-xr-x    3 root     root          4096 Jun 11 11:15 ..
drwxr-xr-x    2 root     root          4096 Jun 11 11:15 some.domain

/etc/letsencrypt/archive/some.domain:
total 12
drwxr-xr-x    2 root     root          4096 Jun 11 11:15 .
drwxr-xr-x    3 root     root          4096 Jun 11 11:15 ..
-rw-r--r--    1 root     root           224 Jun 11 11:15 resolv.conf
All done inside the container, moving on!

go@filserver:/var/lib/go-agent/pipelines/internet/docker-py-issue$ docker -v 
Docker version 18.09.6, build 481bc77
go@filserver:/var/lib/go-agent/pipelines/internet/docker-py-issue$ pip freeze 
adns-python==1.2.1
ansible==2.0.0.2
attrs==17.4.0
backports.ssl-match-hostname==3.5.0.1
cached-property==1.5.1
certifi==2018.11.29
chardet==3.0.4
docker==3.6.0
docker-compose==1.23.2
docker-pycreds==0.4.0
dockerpty==0.4.1
docopt==0.6.2
ecdsa==0.13
enum34==1.1.6
funcsigs==1.0.2
functools32==3.2.3.post2
GeoIP==1.3.2
httplib2==0.9.1
idna==2.7
ipaddress==1.0.22
IPy==0.83
Jinja2==2.8
jsonschema==2.6.0
MarkupSafe==0.23
meld==3.14.2
netaddr==0.7.18
notify2==0.3.1
paramiko==1.16.0
pluggy==0.6.0
py==1.5.2
pycrypto==2.6.1
pygobject==3.20.0
pytest==3.3.2
python-apt==1.1.0b1+ubuntu0.16.4.4
PyYAML==3.13
redis==2.10.6
requests==2.20.1
six==1.12.0
texttable==0.9.1
urllib3==1.24.1
websocket-client==0.54.0
You are using pip version 8.1.1, however version 19.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
go@filserver:/var/lib/go-agent/pipelines/internet/docker-py-issue$ cat /etc/lsb-release 
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.6 LTS"
