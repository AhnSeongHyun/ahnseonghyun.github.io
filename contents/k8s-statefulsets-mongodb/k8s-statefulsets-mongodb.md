---
title: 'Running a MongoDB Database in Kubernetes with StatefulSets'
author: 'ash84'
pub_date: '2019-01-26'
description: '본 포스팅은 Qwiklabs 의 [Kubernetes in the Google Cloud](https://www.qwiklabs.com/quests/29)
를 기반으로 하고 있습니다. 

**이번 시간에 할 것들 :** 

- How to d Kubernetes cluster, a headless service, and a StatefulSet.
- How to connect a Kubernetes cluster to a MongoDB replica set.
- How to scale MongoDB replica set instan'
featured_image: ''
tags: ['k8s', 'statefulsets', 'mongodb']
---

본 포스팅은 Qwiklabs 의 [Kubernetes in the Google Cloud](https://www.qwiklabs.com/quests/29)
를 기반으로 하고 있습니다. 

**이번 시간에 할 것들 :** 

- How to d Kubernetes cluster, a headless service, and a StatefulSet.
- How to connect a Kubernetes cluster to a MongoDB replica set.
- How to scale MongoDB replica set instances up and down.

## Setting up

아래와 같은 단계로 세팅을 한다. 

- Download the MongoDB [replica set/sidecar](https://github.com/thesandlord/mongo-k8s-sidecar.git) (or utility container in our cluster).
- Instantiate a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/).
- Instantiate a [headless service](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services).
- Instantiate a [StatefulSet](http://kubernetes.io/docs/concepts/abstractions/controllers/statefulsets/).

다운로드 받기 

```shell
    git clone https://github.com/thesandlord/mongo-k8s-sidecar.git
    cd ./mongo-k8s-sidecar/example/StatefulSet/
```

StorageClass 설정 

- StorageClass : 데이터베이스 노드로 사용할 스토리지의 한 종류

```yaml
    kind: StorageClass
    apiVersion: storage.k8s.io/v1beta1
    metadata:
      name: fast
    provisioner: kubernetes.io/gce-pd
    parameters:
      type: pd-ssd
```

- `fast` 라는 이름으로 SSD 볼륨을 설정한다.

```shell
    kubectl apply -f googlecloud_ssd.yaml
```

## Deploying the Headless Service and StatefulSet

설정하는 파일을 살펴보자. 

```yaml
    apiVersion: v1   <-----------   Headless Service configuration
    kind: Service
    metadata:
      name: mongo
      labels:
        name: mongo
    spec:
      ports:
      - port: 27017
        targetPort: 27017
      clusterIP: None
      selector:
        role: mongo
    ---
    apiVersion: apps/v1beta1    <------- StatefulSet configuration
    kind: StatefulSet
    metadata:
      name: mongo
    spec:
      serviceName: "mongo"
      replicas: 3
      template:
        metadata:
          labels:
            role: mongo
            environment: test
        spec:
          terminationGracePeriodSeconds: 10
          containers:
            - name: mongo
              image: mongo
              command:
                - mongod
                - "--replSet"
                - rs0
                - "--smallfiles"
                - "--noprealloc"
              ports:
                - containerPort: 27017
              volumeMounts:
                - name: mongo-persistent-storage
                  mountPath: /data/db
            - name: mongo-sidecar
              image: cvallance/mongo-k8s-sidecar
              env:
                - name: MONGO_SIDECAR_POD_LABELS
                  value: "role=mongo,environment=test"
      volumeClaimTemplates:
      - metadata:
          name: mongo-persistent-storage
          annotations:
            volume.beta.kubernetes.io/storage-class: "fast"
        spec:
          accessModes: [ "ReadWriteOnce" ]
          resources:
            requests:
              storage: 100Gi
```

**Headless service: overview**

- 첫번째 섹션을 headless-service
- k8s 에서 원래 service 는 특정 pod 에 접근하기 위한 정책 또는 규칙을 명시해야한다.
- headless service is one that doesn't prescribe load balancing.
- StatefulSets 과 결합할 때, pod 에 접근할 수 있는 개별적인 DNS들을 준다. 이러한 방법으로 mongodb 에 개별적으로 연결되게 된다.
- `clusterIP` 가 None 인 것을 확인 할 수 있다.

**StatefulSet: overview**

- 두번째 섹션에 있는 내용이다.
- mongodb 가 실행될 때 k8s 리소스를 어떻게 쓸 것인가?
- metadata 부분에 label 을 설정, spec 부분에서 replicas 를 명시
- 하위의 spec 부분은 Pod 에 대한 내용
    - `terminationGracePeriodSeconds` : gracefully shutdown the pod when you scale down the number of replicas
    - 두개의 컨테이너 명시 : mongodb, mongodb-sidecar
        - mongod : `mountPath: /data/db` 로 데이터 저장이 연결되도록 지정
        - mongodb-sidecar :
            - configure the MongoDB replica set automatically
            - a "sidecar" is a helper container that helps the main container run its jobs and tasks.

- volumeClaimTemplates : 앞에서 생성한 StorageClass 에 대한 내용

**Deploy Headless Service and the StatefulSet**

    kubectl apply -f mongo-statefulset.yaml

Scaling the MongoDB replica set

```shell
    kubectl scale --replicas=5 statefulset mongo
    
    kubectl get pods
    
    NAME      READY     STATUS              RESTARTS   AGE
    mongo-0   2/2       Running             0          3m
    mongo-1   2/2       Running             0          2m
    mongo-2   2/2       Running             0          1m
    mongo-3   0/2       ContainerCreating   0          8s
```

## Using the MongoDB replica set

Statefulset 내의 각각의 pod 은 DNS name 을 가진다. 

- `<pod-name>.<service-name>`
- connection string URI 에서 사용할 수 있다.

```
    mongo-0.mongo
    mongo-1.mongo
    mongo-2.mongo
    
    "mongodb://mongo-0.mongo,mongo-1.mongo,mongo-2.mongo:27017/dbname_?"
```
