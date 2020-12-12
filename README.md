Ansible Role: snapraid
======================

[![Build Status][build_badge]][build_link]
[![Ansible Galaxy][galaxy_badge]][galaxy_link]

Install and configure SnapRAID — A backup program for disk arrays

Requirements
------------

None.

Role Variables
--------------

See [defaults/main.yml](defaults/main.yml).

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: server
  roles:
    - role: sprat.snapraid
```

License
-------

MIT

Author Information
------------------

This role was created in 2020 by [Sylvain Prat](https://github.com/sprat).


[build_badge]:  https://img.shields.io/github/workflow/status/sprat/ansible-role-snapraid/CI
[build_link]:   https://github.com/sprat/ansible-role-snapraid/actions?query=workflow:CI
[galaxy_badge]: https://img.shields.io/ansible/role/51519
[galaxy_link]:  https://galaxy.ansible.com/sprat/snapraid
