---
title: 'Hello Node Kubernetes'
author: 'ash84'
pub_date: '2019-01-23'
description: ''
featured_image: ''
tags: ['k8s', 'node', 'gcp', 'gcr']
---

본 포스팅은 Qwiklabs 의 [Kubernetes in the Google Cloud](https://www.qwiklabs.com/quests/29)
를 기반으로 하고 있습니다. 

이번 시간에 실습해 볼 것들:

- Create a Node.js server.
- Create a Docker container image.
- Create a container cluster.
- Create a Kubernetes pod.
- Scale up your services.


![](https://farm5.staticflickr.com/4896/46843656391_4ec0c17e7b_b.jpg)

위의 그림에서 보면 GKE 와 GCR 그리고 k8s 의 관계를 설명해주고 있다. GCP 안에서의 관계는 저런식이지만 GCR 이 DockerHub 로 대체될 수 있고, GKE 가 AWS 로 대체 될 수 있을것 같다. 

## Node.js app

- 아래와 같이 `server.js` 를 생성한다.

```javascript
    var http = require('http');
    var handleRequest = function(request, response) {
      response.writeHead(200);
      response.end("Hello World!");
    }
    var www = http.createServer(handleRequest);
    www.listen(8080);
```

## Docker container image 만들기

- `Dockerfile` 생성

```
    FROM node:6.9.2
    EXPOSE 8080
    COPY server.js .
    CMD node server.js
```

- 8080 포트를 오픈한다는 것이고, `CMD` 를 통해서 `server.js` 를 실행한다.

```shell
    docker build -t gcr.io/PROJECT_ID/hello-node:v1 .
```

- GCR 에 올리기 위해서 `PROJECT_ID` 으로 이름을 생성한다.

```shell
    docker run -d -p 8080:8080 gcr.io/PROJECT_ID/hello-node:v1
```

- 8080 포트를 8080 포트로 맵핑해서 실행

실행하면, Cloud shell 에서 `preview on port 8080` 버튼을 통해서 8080 포트를 웹 브라우저에서 볼 수 가 있다. 

```shell
    gcloud docker -- push gcr.io/PROJECT_ID/hello-node:v1
```

- 생성한 docker image를 GCR 에 올린다.

## 클러스터 만들기

- 아래와 같이 k8s hello-world cluster 를 생성한다.

```shell
    gcloud config set project PROJECT_ID
    gcloud container clusters create hello-world \
                    --num-nodes 2 \
                    --machine-type n1-standard-1 \
                    --zone us-central1-a
```

## Pod 생성하기

```shell
    kubectl run hello-node \
        --image=gcr.io/PROJECT_ID/hello-node:v1 \
        --port=8080
```

- 앞서서 GCR에 올려둔 hello-node:v1 의 이미지를 가져와서 실행을 시킨다.
- 실행을 하면 `deployment` 가 생성된다.

```shell
    kubectl get deployments
    kubectl get pods
```

- 위의 deployment 와 pod 의 리스트를 볼 수 있다.

## 외부 트래픽 연결하기

- 현재까지 진행했으면, 클러스터 안에서 내부IP 로 pod 에 접근이 가능한 상태이다.
- 이것을 외부로 오픈하기 위해서는 k8s service 를 생성해야한다.

```shell
    kubectl expose deployment hello-node --type="LoadBalancer"
```

- `type` :
    - LoadBalancer : [cluster 에서 제공하는 로드밸런서](https://cloud.google.com/load-balancing/docs/)를 사용한다는 것.
    - ClusterIP(기본값)
    - NodePort
    - ExternalName
    - Headless

```shell
    kubectl get services
    
    NAME         CLUSTER-IP     EXTERNAL-IP      PORT(S)    AGE
    hello-node   10.3.250.149   104.154.90.147   8080/TCP   1m
    kubernetes   10.3.240.1     <none>           443/TCP    5m
```

- k8s service 에 대한 리스트를 볼 수가 있다. CLUSTER-IP는 내부 IP이다.

## 서비스 스케일업 하기

```shell
    kubectl scale deployment hello-node --replicas=4
```

- `replicas` 를 통해서 스케일업을 할 수 있다. 0으로 줄일 수도 있다.

```shell
    kubectl get deployment
    
    NAME         DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
    hello-node   4         4         4            4           16m
```

![](https://farm8.staticflickr.com/7818/31902247287_9aa1d5c9d8_b.jpg)


## 서비스의 롤링업그레이드

- server.js 를 수정을 하고 다시 docker image 를 생성하는데 hello-node:v2 로 생성을 한다.
- 그리고 생성된 이미지를 GCR 에 push 를 한다.

```shell
    kubectl edit deployment hello-node
```

- 기존의  hello-node 에 v2 이미지를 바라보도록 deployment 를 수정한다.
- 수정하고 나면 새로운 이미지로 다시 pod 들이 뜨는 것을 확인할 수 있다.
