# Ansible docker_presets role

This is an [Ansible](http://www.ansible.com) role to setup a set of facts with docker images and containers.

This role provides also some useful filters to manage the presets.

## Requirements

[Ansible 2.6+](http://docs.ansible.com/ansible/latest/intro_installation.html)

## Variables

The role reads dynamically the images and containers config from directories 'defaults/images' and 'defaults/containers'.

From the previous directories the role setups dynamically some variables that contain the set of presets for images, containers and the path to the files directory in this role:

- docker_presets_images
- docker_presets_containers

## Filters

The role provides these filters to manipulate the provided presets:

- docker_presets_add_attributes: adds attributes to a set of presets
- docker_presets_randomize_names: randomize the name attribute in a set of presets
- docker_presets_remove_attributes: remove attributes from a set of presets
- docker_presets_repeat: repeat a preset a number of times

## Dependencies

N/A

## Example Playbook

This is an example playbook:

```yaml
---

- hosts: all
  roles:
    - amtega.docker_presets
  tasks:
    - set_fact:
        my_random_containers: >-
            {{ docker_presets_containers | docker_presets_randomize_names }}
        my_random_containers_with_comments: >-
            {{ my_random_containers
                | docker_presets_add_attributes(
                  {'comment': 'this is a sample'}, overwrite=true) }}                    
        my_repeated_containers: >-
            {{ docker_presets_containers | docker_presets_repeat(3) }}

    - set_fact:
        my_random_containers_without_comments: >-
            {{ my_random_containers_with_comments
                | docker_presets_remove_attributes(["comment"] }}
```

## Testing

Tests are based on docker containers. You can setup docker engine quickly using the playbook `files/setup.yml` available in the role [amtega.docker_engine](https://galaxy.ansible.com/amtega/docker_engine).

Once you have docker, you can run the tests with the following commands:

```shell
$ cd amtega.docker_presets/tests
$ ansible-playbook main.yml
```

## License

Copyright (C) 2018 AMTEGA - Xunta de Galicia

This role is free software: you can redistribute it and/or modify it under the terms of:

GNU General Public License version 3, or (at your option) any later version; or the European Union Public License, either Version 1.2 or – as soon they will be approved by the European Commission ­subsequent versions of the EUPL.

This role is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details or European Union Public License for more details.

## Author Information

- Juan Antonio Valiño García.
