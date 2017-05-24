# docker_presets

This is an [Ansible](http://www.ansible.com) role to setup a set of presets for docker images and containers.

## Requirements

- Ansible >= 2.0

## Role Variables

The role setups dynamically two variables that contain a set of presets for images and containers. The variables are, respectively, these ones:

- docker_presets_images
- docker_presets_containers

## Dependencies

N/A

## Example Playbook

This is an example playbook:

```yaml
---

- hosts: all
  roles:
    - docker_presets
```

## Testing

Test are based on docker containers. You can run the tests with the following commands:

```shell
$ cd docker_presets/test
$ ansible-playbook main.yml
```

## License

Not defined.

## Author Information

- Juan Antonio Valiño García ([juanval@edu.xunta.es](mailto:juanval@edu.xunta.es)). Amtega - Xunta de Galicia
