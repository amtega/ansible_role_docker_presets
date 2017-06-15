# Ansible docker_presets role

This is an [Ansible](http://www.ansible.com) role to setup a set of facts with docker images and containers.

This role provides also some useful filters to manage the presets.

## Requirements

- Ansible >= 2.0

## Role Variables

The role reads dynamically the images and containers config from directories 'defaults/images' and 'defaults/containers'.

From the previous directories the role setups dynamically two variables that contain the set of presets for images and containers. The variables are, respectively, these ones:

- docker_presets_images
- docker_presets_containers

## Role Filters

The role provides these filters to manipulate the provided presets:

- docker_presets_add_attributes: adds attributes to a set of presets
- docker_presets_randomize_names: randomize the name attribute in a set of presets

## Dependencies

N/A

## Example Playbook

This is an example playbook:

```yaml
---

- hosts: all
  roles:
    - docker_presets
  tasks:
    - set_fact:
        my_random_containers: >-
            {{ docker_presets_containers | docker_presets_randomize_names }}
        my_random_containers_with_comments: >-
            {{ my_random_containers
                | docker_presets_add_attributes(
                  {'comment': 'this is a sample'}) }}
```

## Testing

You can run the tests with the following commands:

```shell
$ cd docker_presets/test
$ ansible-playbook main.yml
```

## License

Not defined.

## Author Information

- Juan Antonio Valiño García ([juanval@edu.xunta.es](mailto:juanval@edu.xunta.es)). Amtega - Xunta de Galicia