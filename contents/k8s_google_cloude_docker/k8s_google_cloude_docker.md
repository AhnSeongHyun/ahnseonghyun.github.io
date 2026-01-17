---
title: 'Introduction to Docker'
author: 'ash84'
pub_date: '2019-01-13'
description: '본 포스팅은 Qwiklabs 의 [Kubernetes in the Google Cloud](https://www.qwiklabs.com/quests/29)
를 기반으로 하고 있습니다. 

## Docker Image & Build, Run

기본적으로 도커이미지 형태로 올리는 것이 기반이 되어야 한다. 일단 도커 이미지를 생성하기 위해서는 `Dockerfile` 을 생성해야 한다. 

    # Use an official Node runtime as the parent image
    FROM node:6
    
    # S'
featured_image: ''
tags: ['k8s', 'Docker']
---
본 포스팅은 Qwiklabs 의 [Kubernetes in the Google Cloud](https://www.qwiklabs.com/quests/29)
를 기반으로 하고 있습니다. 

## Docker Image & Build, Run

기본적으로 도커이미지 형태로 올리는 것이 기반이 되어야 한다. 일단 도커 이미지를 생성하기 위해서는 `Dockerfile` 을 생성해야 한다. 

    # Use an official Node runtime as the parent image
    FROM node:6
    
    # Set the working directory in the container to /app
    WORKDIR /app
    
    # Copy the current directory contents into the container at /app
    ADD . /app
    
    # Make the container's port 80 available to the outside world
    EXPOSE 80
    
    # Run app.js using node when the container launches
    CMD ["node", "app.js"]

`From` 부분에서 기존의 부모 이미지를 가져와서 활용 할 수가 있다. node 나 python 같은 언어나 혹은 특정환경이 세팅된 도커 이미지를 활용할 수 있을것 같다.  이럴 경우, 이미지를 삭제할 때 자식 이미지를 먼저 삭제 해줘야 부모 이미지를 삭제 할 수 있다. 

**도커 이미지 빌드 :** 

    Usage:	docker build [OPTIONS] PATH | URL | -
    
    > docker build -t node-app:0.1 .

`-t` : name 과 tag 를 달 수 있다. `.` 부분은 현재 도커파일이 있는 위치를 가리킨다. 그 외에 여러가지 옵션이 있고 `docker build —help` 옵션을 통해서 확인 할 수 있다. 빌드가 되면 `docker images` 를 통해서 확인 할 수 있다. 

**도커 이미지 실행 :** 

    > docker run -p 4000:80 --name my-app node-app:0.1

`-p` : 옵션은 도커 내의 port 를 외부 port 로 연결하는 옵션이다. 여기서는 4000 포트를 80포트로 연결 하고 있다. `—name` 옵션은 이름을 부여하는 것이고 앞에서 생성한 이미지의 `name:tag` 을 지정해서 실행하게 된다. 실행한 이후에는 `docker ps` 를 통해서 확인 할 수 있다. 

**도커에서 디커깅 하기 위한 명령어들 :** 

    > docker inspect [container_id]
    
    > docker exec -it [container_id] bash // 도커 내부 bash 로 들어가는 명령어 
    
    > docker logs -f [container_id]

## GCR(Google Container Registry) Update

[Google Container Registry](https://cloud.google.com/container-registry/) 에 도커이미지를 업데이트 한다. GCR 은 Google Cloud 에서 제공하는 비공개 도커이미지 저장소이다. 

업데이트 하기 위해서 알아야 할 것은 아래와 같은데 

- [hostname]= gcr.io
- [project-id]= your project's ID
- [image]= your image name
- [tag]= any string tag of your choice. If unspecified, it defaults to "latest".

아래의 명령어를 통해서 확인 할 수가 있다. 

    > gcloud config list project

    [core]
    project = qwiklabs-gcp-439588a0de092959
    Your active configuration is: [cloudshell-17375]

프로젝트ID 를 도커 이름으로 지정

    ex) docker tag node-app:0.2 gcr.io/[project-id]/node-app:0.1

    > docker tag node-app:0.1 gcr.io/qwiklabs-gcp-439588a0de092959/node-app:0.1

## GCR 에 이미지 올리기

    ex) gcloud docker -- push [gcr.io/[project-id]/node-app:0.](http://gcr.io/%5Bproject-id%5D/node-app:0.2)1
    
    > gcloud docker -- push gcr.io/qwiklabs-gcp-439588a0de092959/node-app:0.1

## GCR 에 올린 이미지 가져와서 띄우기

    > gcloud docker -- pull gcr.io/[project-id]/node-app:0.1
    
    > docker run -p 4000:80 -d gcr.io/[project-id]/node-app:0.1
