---
title: 'python LDAP, ldap3 연동'
author: 'ash84'
pub_date: '2019-10-19'
description: 'LDAP 자체는 정보를 제공하는 시스템이라서 로그인, 토큰이라는 개념이 없어서 id, password 를 넣어서 정보를 조회하고, 조회가 되면 로그인이 되었다는 것으로 인식해서 이를 연동하는 시스템에서 자체적으로 토큰을 발급해야 한다. python 에서 LDAP 을 연동하는 방식은 python-ldap, ldap3 라이브러리를 사용하는 것인데, 아래와 같이 ldap3를 사용하면 된다. 

```shell
    pip install ldap3
```

```python
    from ldap3 import Server, ALL,'
featured_image: ''
tags: ['Python', 'LDAP']
---

LDAP 자체는 정보를 제공하는 시스템이라서 로그인, 토큰이라는 개념이 없어서 id, password 를 넣어서 정보를 조회하고, 조회가 되면 로그인이 되었다는 것으로 인식해서 이를 연동하는 시스템에서 자체적으로 토큰을 발급해야 한다. python 에서 LDAP 을 연동하는 방식은 python-ldap, ldap3 라이브러리를 사용하는 것인데, 아래와 같이 ldap3를 사용하면 된다. 

```shell
    pip install ldap3
```

```python
    from ldap3 import Server, ALL, Connection
    
    
    def get_ldap(user_id, password):
        address = 'ldap.site.com'
        dn = f'uid={user_id},ou=People,dc=site,dc=com'
        server = Server(address, get_info=ALL)
        conn = Connection(server, dn, password, auto_bind=True)
    
        conn.search('dc=rainist,dc=com', '(&(uid=ash84))', attributes=['sn', 'cn', 'givenName', 'mail', 'mobile', 'uid'])
        print(conn.entries)
    
    
    get_ldap('ash84', 'xxxx')
```

```shell
    [DN: uid=ash84,ou=People,dc=site,dc=com - STATUS: Read - READ TIME: 2019-10-18T11:31:27.636801
        cn: ash84
        givenName: ash84
        mail: ash84@xxx.com
        mobile: 01012341234
        sn: Ahn
        uid: ash84
    , DN: cn=ash84,uid=ash84,ou=People,dc=site,dc=com - STATUS: Read - READ TIME: 2019-10-18T11:31:27.637020
        cn: ash84
        uid: ash84
```
