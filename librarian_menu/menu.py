"""
menu.py: main menu plugin

Copyright 2014-2015, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""

from bottle import request
from bottle_utils import html
from bottle_utils.i18n import i18n_url


class MenuItem(object):
    label = ''
    group = None
    icon_class = ''
    alt_icon_class = ''
    route = None
    default_classes = ('navicon',)
    name = None

    def is_alt_icon_visible(self):
        return False

    def is_visible(self):
        return True

    def get_path(self):
        return i18n_url(self.route)

    def render(self):
        if not self.is_visible():
            return ''
        if self.is_alt_icon_visible():
            icon_class = self.alt_icon_class
        else:
            icon_class = self.icon_class
        if icon_class:
            icon = html.SPAN(_class="icon")
        else:
            icon = ''

        item_class = ' '.join(
            tuple(self.default_classes) + (icon_class,)).strip()
        return html.link_other(
            ' '.join([icon + html.SPAN(self.label, _class="label")]),
            self.get_path(), request.original_path,
            lambda s, _class: html.SPAN(s, _class='active ' + item_class),
            _class=item_class)

    def __str__(self):
        return self.render()

    def __unicode__(self):
        return self.render()
