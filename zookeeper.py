{% for usr in 'sday','mday','kday' %}
{{ usr }}:
  user:
    - present
    - fullname: {{ usr }}
    - home: True
    - shell: /bin/bash
    # group names for sudo very by platform
    - optional_groups:
      - admin
      - ubuntu
      - wheel
  ssh_auth:
    - present
    - user: {{ usr }} 
    - source: salt://users/keys/{{ usr }}_id_rsa.pub
    - require:
      - user: {{ usr }}
{% endfor %} 






{% for host in 'ma1-smd-lapp119.corp.scoday.com','ma1-smd-lapp121.corp.scoday.com','ma1-smd-lapp121.corp.scoday.com'}
{{ host }}:
  host:
    - present
    - 
