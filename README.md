Ansible Role: snapraid
======================

[![Ansible Galaxy][galaxy_image]][galaxy_link]
[![Build Status][travis_image]][travis_link]

Install and configure SnapRAID — A backup program for disk arrays

Requirements
------------

None.

Role Variables
--------------

See `defaults/main.yml`.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: sprat.snapraid
```

License
-------

MIT

Author Information
------------------

This role was created in 2020 by [Sylvain Prat](https://github.com/sprat).


[travis_image]:  https://travis-ci.com/sprat/ansible-role-snapraid.svg?branch=master
[travis_link]:   https://travis-ci.com/sprat/ansible-role-snapraid
[galaxy_image]:  https://img.shields.io/badge/galaxy-sprat.snapraid-660198.svg?style=flat
[galaxy_link]:   https://galaxy.ansible.com/sprat/snapraid
