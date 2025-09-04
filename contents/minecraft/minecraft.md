---
title: '마인크래프트 docker'
author: 'ash84'
pub_date: '2025-09-05'
description: '마인크래프트 서버 띄워서 멀티플레이'
featured_image: 'image.png'
tags: ['마인크래프트', 'minecraft', 'docker', '마인크래프트 서버띄우기']
---

## 발단 

애들이 마인크래프트를 좋아하는데 iOS 기기로 둘이서 하려다보니 둘다 마이크로소프트 계정이 있으면 한쪽에서 한쪽을 초대해서 하거나 아니면 Realm 이라는것을 통해서 같이 할 수 있는것 같다. 근데 이건 유료인것 같고. 근데 내가 알기론 마인크래프트는 서버를 운영할 수 있다고 들었고 좀 더 찾아보니 java edition과 bedrock edition이 있는데 iOS/Andriod 사용자라면 bedrock edition으로 서버를 띄우면 둘이 접속해서 쓸수 있게 할 수 있을것 같았다. 

막연하게 생각만 하다가 아래의 김실장 유투브를 보게 되면서 나도 모르게 서버를 띄워서 둘이 같이 하게해주자라는 생각에 불이 붙었다. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/b3OI7TxT-Bw?si=sIqZTcIVoEoX5KUR" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

그렇지만 AWS나 그런곳에 쓰는건 귀찮았고, 내 맥북에어에 띄우고 와이파이로 애들이 접속하는 형태로 진행했다. docker로 된 것들이 있어서 아래와 같이 docker 명령어를 수행하면 마인크래프트 서버가 뜨고 ip:port를 마인크래프트 앱에서 넣으면 접속시킬수가 있다. 

```
docker rm -f mcbedrock
docker run -d --name mcbedrock \
  --platform=linux/amd64 \
  -e EULA=TRUE \
  -e TZ=Asia/Seoul \
  -e GAMEMODE=survival \
  -e ALLOW_CHEATS=false \
  -e DIFFICULTY=easy \
  -e LEVEL_NAME=ActionsAndStuff \
  -p 19132:19132/udp \
  -v ~/workspace/bedrock-data:/data \
  itzg/minecraft-bedrock-server
```

일단 애들이 굉장히 좋아했고, 둘이 할수 있으니 ㅎㅎ 와이파이가 되는 공간에서만 둘이 할 수 있다보니 집이 아닌 어디를갈때 자꾸 챙기라고 한다. 

## 추가사항

⚠️ 약간의 틀린 내용이 있을수 있습니다. 저도 마인크래프트 전문가가 아님을 먼저 말씀드립니다. 

일단 기본적으로 만들면 마인크래프트 아무것도 없는 곳이 나오는데, 아이들이 유튜브에서 마인크래프트를 접하게 되면 어느정도 구축된 세계를 플레이하는 유튜버의 플레이를 기준으로 삼게 된다. 한마디로 아빠가 만들어준 세계가 너무 시시하다. 그래서 처음에는 월드를 설치해줬다. 월드라는게 무엇이냐 하면, 스타크래프트로 치면 유즈맵세팅 같은 느낌이라고 보면된다.(맞나?) 원래 마인크래프트세계는 아무것도 없는데 여러가지 조건이나 제약이나 미리 어느정도의 세계를 구축해 놓은것이다. 

https://mcpedl.com/tag/mcworld/

이런 사이트에 가면 좀비, 오징어게임 심지어 젤다까지 다양한 월드(mcworld)가 있고 이것을 다운로드 받아서 .zip으로 바꾸고 압축을 풀고 특정 디렉토리에 두면 된다. 그리고나서 volume이 연결된 위치, 그러니까 내 로컬로 치면 `~/workspace/bedrock-data` 하위에 `worlds` 하위로 다운로드 받은 디렉토리를 위치 시키면 된다. 그리고 그 디렉토리의 이름을 LEVEL_NAME에 연결시키면 된다. 지금 보면 `ActionAndStuff` 라는 디렉토리가 `~/workspace/bedrock-data/worlds/ActionAndStuff` 위치에 있고 LevelName이 `ActionAndStuff`로 되어 있다. 이렇게 되면 서버로 접속하면 그 월드로 연결되어서 나오게 된다. 

처음에 나는 인식을 서버라는건 말 그대로 서버라고 생각을 했고, 월드는 서버안에 여러개의 월드가 있어서 선택해서 들어갈 수 있는 형태라고 생각을 했다. 그래서 여러 월드를 깔아놓고 애들이 맘껏 놀게 해야지라고 생각했는데 그게 아니였다. 

잘 놀다가 갑자기 이게 아니라고 하면서 모드(mods)를 설치해달라고 한다. ㅠ 고객님들은 만족할줄을 모른다. 이건 또 뭔가 싶다. 
어려운점이 뭐냐하면 대부분의 마인크래프트 유튜버들은 Java Edition 즉, PC에서 이걸하는데 약간 bedrock edition과 다른점도 있고 꽤 오래된 영상이들을 보게 되면 지금 시점에 어떻게 적용해야할지 막막하다. 

찾아보니 모드(mods)는 단순하게 생각하면 부분적인 커스터마이징이라고 보면 된다. 예를 들어, 월드는 그대로인데, 특정 아이템만 더 추가를 하고 싶다. 총을 추가하고 싶다라던가 괴물을 더 추가하고 싶다라고 할때 이 모드를 다운로드 받아서 설치하면 된다. 

https://www.minecraftmods.com/

모드는 2가지 종류가 있느것 같은데 하나는 resource 다른 하나는 behavior. 그래서 둘다 있는 경우도 있고 하나만 있는 경우도 있는데
다운로드 받으면 나의 docker volume이 연결된 기본 디렉토리 `~/workspace/bedrock-data` 하위에 2개의 디렉토리를 만든다. 

- behavior_packs
- resource_packs 

이 2개의 디렉토리 중 하나에 압축을 푼다. 그리고 나서 압축을 푼 디렉토리 안에 들어가면 manifeset.json 이라는 파일이 있는게 그것을 열면 이런 형식으로 나와있다. 

```
{
    "format_version": 2,
    "header": {
        "description":"It gives your world a more dynamic and lively feel by adding several new animations, particles, and other stuff! (Work in progress).",
        "name": "Actions & Stuff §8(1.0.2)",
        "uuid": "22b87fae-158c-4663-aa29-a3d70acbf0b3",
        "version": [1, 0, 2],
        "min_engine_version": [ 1, 20, 80 ]
    },
    "modules": [
        {
            "description": "ACT",
            "type": "resources",
            "uuid": "19c0aaaf-dfcb-4de9-9184-eb1ba17cd774",
            "version": [1, 0, 2]
        }
    ]
}
```

중요한건 `header.uuid`, `header.version` 인데, 이 정보를 지금 만든 월드 안에 넣어야 한다. 어떻게 넣냐하면 
본인이 만든 월드 디렉토리, 여기서는  `~/workspace/bedrock-data/worlds/ActionAndStuff` 이 디렉토리 하위로 가면 2개의 파일이 있다.(없으면 만든다)

- world_resource_packs.json
- world_behavior_packs.json

이 파일에 아까 저 `header.uuid`, `header.version`을 넣는다. 형식을 보면 json array 형식이다. 즉 하나의 월드안에 여러가지 모드(mods)를 원하는 만큼 추가 및 삭제가 가능하다는 것이다.

```
[
  {
    "pack_id": "22b87fae-158c-4663-aa29-a3d70acbf0b3",
    "version": [1, 0, 2]
  }
]
```

이렇게 연동을 하면 서버 접속을 할때 월드와 그에 딸린 모드들을 같이 로드가 된 세계를 플레이할 수 있다. 

--- 

생각보다 재밌었던 경험이었고, 무엇보다도 개발자, 컴퓨터 잘하는 아빠로써 체면을 살렸던 순간이었던것 같다. 그리고 월드/모드 시스템을 간접적으로 경험하면서 이런식으로 구성했구나를 이해하는 재미가 있었다. 결국 하나의 월드 안에 여러가지 모드들을 넣으면서 자신들만의 세계를 구축할 수 있는 시스템이 마인크래프트라는것을 서버 셋업을 하면서 알게 되었다. 가장 어려운건 bedrock edition에 대한 자료가 많지 않아서 찾는게 일이었고, 항상 모든 검색어 끝에 bedrock을 붙이면 그나마 금방 찾을수 있을듯. 


1-2일 정도만에 웹사이트를 통해서 알게된 내용들이라 틀린 내용들도 있을거라서, 만약 틀린 내용이 있다면 `me@ash84.io`로 보내주세요. 



