#!/usr/bin/env python

import os
import sys
import weakref
from types import ModuleType
from hashlib import sha1
from jinja2 import BaseLoader, TemplateNotFound, DictLoader
from jinja2.utils import open_if_exists, internalcode
from jinja2._compat import string_types, iteritems

    
loader = DictLoader({'~/pubmed-mining/force_directed.html': open ( sys.argv[1], 'r')})

    
