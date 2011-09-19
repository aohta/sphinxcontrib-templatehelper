#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sphinx.application import ExtensionError

def add_fileinfo(app, pagename, templatename, context, doctree):
    if not app.config.templatehelper_enabled:
        return

    if len(pagename.split('/')) > 1:
      context['basename'] = pagename.split('/')[-1]
      context['pardir'] = pagename.split('/')[-2]
    else:
      context['basename'] = pagename
      context['pardir'] = '.'

def setup(app):
    app.add_config_value('templatehelper_id', '', 'html')
    app.add_config_value('templatehelper_enabled', True, 'html')
    app.connect('html-page-context', add_fileinfo)
    return app
