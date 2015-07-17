#!/usr/bin/env python

import os
import sys
import weakref
from types import ModuleType
from hashlib import sha1
from jinja2 import BaseLoader, TemplateNotFound, DictLoader
from jinja2.utils import open_if_exists, internalcode
from jinja2._compat import string_types, iteritems

class DictLoader(BaseLoader):
    
    loader = DictLoader({'/Users/Lezama/Desktop/force_directed.html': open ( sys.argv[1], 'r')})

    def __init__(self, mapping):
        self.mapping = mapping

    def get_source(self, environment, template):
        if template in self.mapping:
            source = self.mapping[template]
            return source, None, lambda: source == self.mapping.get(template)
        raise TemplateNotFound(template)

    def list_templates(self):
        return sorted(self.mapping)

    
