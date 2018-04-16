# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from datetime import datetime
from random import randint, seed

def docker_presets_add_attributes(presets, attributes, overwrite=False):
    """Add attributes to a set of presets.

    Args:
        presets (list of dicts): presets to add the new attributes.
        attributes (dict): attributes to add.
        overwrite (bool): tells if attribute must be overwriten if present

    Returns:
        list of dicts: presets with attributes added in.
    """
    for preset in presets:
        for attribute in attributes:
            if attribute not in preset or overwrite:
                preset[attribute] = attributes[attribute]

    return presets

def docker_presets_randomize_names(presets):
    """Randomize the name attribute in a set of presets.

    Args:
        presets (list of dicts): the presets to randomize.

    Returns:
        list of dicts passed with the name randomized.
    """
    for preset in presets:
        if "name" in preset:
            basename = preset["name"]
        else:
            basename = "container"

        seed(datetime.now())
        preset["name"] = "{}-{}".format(basename, randint(0, 99999999))

    return presets

def docker_presets_remove_attributes(presets, attributes):
    """Remove attributes from a set of presets.

    Args:
        presets (list of dicts): presets to remove the attributes.
        attributes (list): attributes to remove.

    Returns:
        list of dicts: presets with attributes removed.
    """
    for preset in presets:
        for attribute in attributes:
            preset.pop(attribute, None)

    return presets

def docker_presets_repeat(presets, n):
    """Repeat a preset list.

    Args:
        presets (list of dicts): the presets to repeat.
        n (int): number of times to repeat the preset.

    Returns:
        list of dicts passed repeated n times.
    """
    result = list()
    for n in range(0, n):
        for preset in presets:
            result = result + [preset.copy()]

    return result

class FilterModule(object):
    """Ansible docker_presets filters."""

    def filters(self):
        return {
            'docker_presets_add_attributes': docker_presets_add_attributes,
            'docker_presets_randomize_names': docker_presets_randomize_names,
            'docker_presets_remove_attributes':
                docker_presets_remove_attributes,
            'docker_presets_repeat': docker_presets_repeat
        }
