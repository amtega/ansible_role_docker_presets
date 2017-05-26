# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from random import randint

def docker_presets_add_attributes(presets, attributes):
    """Add attributes to a set of presets.

    Args:
        presets (list of dicts): presets to add the new attributes.
        attributes (dict): attributes to add.

    Returns:
        list of dicts: presets with attributes added in.
    """
    for preset in presets:
        for attribute in attributes:
            preset[attribute] = attributes[attribute]

    return presets

def docker_presets_randomize_names(presets):
    """Randomize the name attribute in a set of presets.

    Args:
        presets (list of dicts): the presets to randomize.

    Returns:
        list of dicts: passed with the name randomized.
    """
    for preset in presets:
        if "name" in preset:
            basename = preset["name"]

        preset["name"] = "{}_{}".format(basename[-22:], randint(0, 99999999))

    return presets

class FilterModule(object):
    """Ansible docker_presets filters."""

    def filters(self):
        return {
            'docker_presets_add_attributes': docker_presets_add_attributes,
            'docker_presets_randomize_names': docker_presets_randomize_names
        }
