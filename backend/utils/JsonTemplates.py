import collections.abc
import json
import os
import re
from string import Template

class JsonTemplates:

    # -----------------------------------------------------------------------
    def __init__(self):
        self.__template = None
        self.__var_regex = re.compile("\{\{\ [a-zA-Z0-9_]+\ \}\}")
        self.__arr_regex = re.compile("\{\%\ [a-zA-Z0-9_]+\ \%\}")
        self.__cln_regex = re.compile("[a-zA-Z0-9_]+")
        self.__version__ = "0.1.0"

    # -----------------------------------------------------------------------
    def is_dict(self, obj):
        return isinstance(obj, collections.abc.Mapping)

    # -----------------------------------------------------------------------
    def is_iterable(self, obj):
        try:
            iter(obj)
            return True
        except:
            return False

    # -----------------------------------------------------------------------
    def clean_key(self, key):
        mtch = self.__cln_regex.search(key)
        if mtch is None:
            return (False, "{} is not valid!".format(key))
        else:
            return (True, mtch.group(0))

    # -----------------------------------------------------------------------
    def loads(self, json_str):
        try:
            self.__template = json.loads(json_str)
        except Exception as ex:
            return (False, "Unable to parse json! {}".format(ex))

        return (True, self.__template)

    # -----------------------------------------------------------------------
    def load_dict(self, json):

        self.__template = json

        return (True, self.__template)

    # -----------------------------------------------------------------------
    def load(self, json_path):
        if os.path.isfile(json_path) and json_path.lower().endswith("json"):
            try:
                with open(json_path) as json_in:
                    self.__template = json.load(json_in)
            except Exception as ex:
                return (False, "Unable to parse json! {}".format(ex))
        else:
            return (False, "{} is not JSON file")
        return (True, self.__template)

    # -----------------------------------------------------------------------
    def __evalulate_value(self, value, replace_dict):
        not_found_error = "{} not found in replacement dictionary {}"
        if self.__var_regex.fullmatch(str(value)):
            replace_key = self.clean_key(value)
            if not replace_key[0]:
                return (False, False, replace_key[1])
            replace_key = replace_key[1]
            if replace_key in replace_dict:
                return (True, True, replace_dict[replace_key])
            else:
                return (False, False, not_found_error.format(replace_key, replace_dict))
        elif self.__arr_regex.fullmatch(str(value)):
            replace_key = self.clean_key(value)
            if not replace_key[0]:
                return (False, False, replace_key[1])
            replace_key = replace_key[1]

            if replace_key in replace_dict:
                if self.is_iterable(replace_dict[replace_key]):
                    return (True, True, replace_dict[replace_key])
                else:
                    return (False, False, "{} value must be iterable".format(replace_key))
            else:

                return (False, False, not_found_error.format(replace_key, replace_dict))

        else:
            return (True, False, value)

    # -----------------------------------------------------------------------
    def __scan_nodes(self, nodes, replace_dict):
        for k, v in nodes.items():
            if self.is_dict(v):
                nodes[k] = self.__scan_nodes(v, replace_dict)
            else:
                if isinstance(nodes[k], str):
                    try:
                        t = Template(nodes[k])
                        new_string = t.safe_substitute(**replace_dict)
                        nodes[k] = new_string
                    except Exception as ex:
                        print(ex)
        return nodes

    # -----------------------------------------------------------------------
    def generate(self, replace_dict):
        try:
            result = self.__scan_nodes(dict(self.__template), replace_dict)
        except Exception as ex:
            return (False, "Error: {}".format(ex))
        return (True, result)


def render_json(json_to_render, ctx):
    json_tmp = JsonTemplates()
    res = json_tmp.load_dict(json_to_render)
    if res[0]:
        new_dict = json_tmp.generate(ctx)
        if new_dict[0]:
            return new_dict[1]
    else:
        return json_to_render
