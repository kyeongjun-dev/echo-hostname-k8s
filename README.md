# echo-hostname-k8s
custom app using node, django for MSA

## docker 이미지 빌드방법(buildx 사용, push 안할경우 `--push` 옵션 제거)
```
docker buildx create --use
docker buildx build --push --platform linux/arm64,linux/amd64 --tag rudwns273/node:echo-hostname-v2 -f node/Dockerfile ./node
docker buildx build --push --platform linux/arm64,linux/amd64 --tag rudwns273/django:echo-hostname-v2 -f django/Dockerfile ./django
```


## docker-compose 작성방법
실행하기 전, 아래 명령어로 django 서비스의 secret key 설정
```
export DJANGO_SECRET_KEY="rm^(ex634^s^t$6+c#6&9w7-8&d^ycnneb4sqsu(nu-jv*"
```


node 서비스에서 GET 요청을 보낼 URL을 입력. 아래 예시에서는 "http://django:8000"
```
version: "3"
services:
  node:
    build:
      context: node
    image: rudwns273/node:echo-hostname
    ports:
      - 3000:3000
    environment:
      VERSION: "v1"
      REQUEST_URL: "http://django:8000"
  django:
    build:
      context: django
    image: rudwns273/django:echo-hostname
    ports:
      - 8000:8000
    environment:
      DJANGO_SECRET_KEY: "${DJANGO_SECRET_KEY}"
      VERSION: "v1"
```

docker-compose를 이용해 서비스 실행
```
docker-compose up -d --build
```
