# fishmlserv

### Deploy
![image](https://github.com/user-attachments/assets/aa0556f8-1873-4adc-af03-69b0a1a69eb4)

### Quick execution using Docker
- https://hub.docker.com/r/mieun/isdomi
### Run
- dev
- http://localhost:8000/docs
```bash
# uvicorn --help
$ uvicorn src.fishmlserv.main:app --reload
```
- prd
```bash
$ uvicorn src.fishmlserv.main:app --host 0.0.0.0 --port 8949
```

### Docker
```bash
$ sudo docker build -t fishmlserv:0.4.0 .
$ sudo docker run -d --name fmlserv-040 -p 8877:8765 fishmlserv:0.4.0
```
### Docker
```bash
$ sudo docker build -t fishmlserv:0.7.1 .
$ sudo docker run -d -p 7799:8080 --name fml071 fishmlserv:0.7.1
$ sudo docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED         STATUS         PORTS                                       NAMES
855e7f93bc3f   fishmlserv:0.7.1   "uvicorn main:app --…"   4 seconds ago   Up 4 seconds   0.0.0.0:7799->8080/tcp, :::7799->8080/tcp   fml071 

# container에 접근
$ sudo docker exec -it fml071 bash

# container 내부
root@855e7f93bc3f:/code# cat /etc/os-realease
cat: /etc/os-realease: No such file or directory
root@855e7f93bc3f:/code# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"

# 다시 호스트OS(WSL) 로 exit
root@7244097edb66:/code# exit

# 로그 확인
$ sudo docker logs -f f073
```

### Fly.io
```bash
$ fly launch --no-deploy
$ flyctl launch --name mariofish
$ flyctl scale memory 256
$ flyctl deploy
```
### Ref
https://curlconverter.com/
