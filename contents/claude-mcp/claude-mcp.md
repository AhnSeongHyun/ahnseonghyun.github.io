---
title: 'claude code mcp 정리'
author: 'ash84'
pub_date: '2026-01-27'
description: '자주 사용하는 몇개의 MCP들을 정리해봤다. '
featured_image: ''
tags: ['claude', 'mcp', 'claude code']
---

자주 사용하는 MCP 관련 정리했다. 몇개 더 추가될 예정.

## `-s` (scope) 옵션

`claude mcp add` 명령어에서 `-s` 옵션은 MCP 서버의 설정 범위를 지정한다.

| 옵션 | 설명 |
|------|------|
| `-s user` | 사용자 레벨 설정. 모든 프로젝트에서 사용 가능. `~/.claude/` 디렉토리에 저장 |
| `-s project` | 프로젝트 레벨 설정. 현재 프로젝트에서만 사용. `.claude/` 디렉토리에 저장 |

대부분의 경우 `-s user`를 사용하면 된다.


## 개발 관련

### JIRA

```shell
claude mcp add jira -s user \
  --env JIRA_HOST=https://my.atlassian.net \
  --env JIRA_USERNAME=ash84@xxx.com \
  --env JIRA_API_TOKEN={{ JIRA API TOKEN}} \
  -- npx -y @modelcontextprotocol/server-atlassian
```   

### Slack

```shell
claude mcp add slack -s user \
  -e SLACK_BOT_TOKEN={{ SLACK_BOT_TOKEN }} \
  -e SLACK_TEAM_ID={{ SLACK_TEAM_ID }} \
  -- npx -y @modelcontextprotocol/server-slack
```


## Data 관련

### Redash

```shell
claude mcp add redash -s user \
  -e REDASH_URL={{ REDASH_URL }} \
  -e REDASH_API_KEY={{ REDASH_API_KEY }} \
  -- npx -y @suthio/redash-mcp
```

### MongoDB

```shell
claude mcp add mongodb -s user \
  -e MDB_MCP_CONNECTION_STRING="{{ MONGODB_CONNECTION_STRING }}" \
  -e MDB_MCP_READ_ONLY=true \
  -- npx -y mongodb-mcp-server
```

### MySQL

```shell
claude mcp add mysql -s user \
  -e MYSQL_HOST='{{ MYSQL_HOST }}' \
  -e MYSQL_PORT='3306' \
  -e MYSQL_USER='{{ MYSQL_USER }}' \
  -e MYSQL_PASS='{{ MYSQL_PASS }}' \
  -e MYSQL_DB='{{ MYSQL_DB }}' \
  -e ALLOW_INSERT_OPERATION='false' \
  -e ALLOW_UPDATE_OPERATION='false' \
  -e ALLOW_DELETE_OPERATION='false' \
  -- /opt/homebrew/bin/node ~/workspace/mcp-server-mysql/dist/index.js 
```

- https://github.com/benborla/mcp-server-mysql
- 마지막줄에 `-- npx -y @benborber/mcp-server-mysql` 를 넣으면 되는게 잘 안되서 릴리즈를 로컬에 다운로드 받고 그걸 빌드해서 나온 dist/index.js를 사용하는 방식으로 쓰고 있음. 
