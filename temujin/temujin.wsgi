#!/usr/bin/python
import sys
import logging
#logging.basicConfig(stream=sys.sdterr)
sys.path.insert(0, '/var/www/jphacks_server/temujin')

from temujin import app as application
