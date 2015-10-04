#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import urwid

b1 = urwid.Button(u"Paquets")
b2 = urwid.Button(u"Ajouter")
b3 = urwid.Button(u"Sync")

txt = urwid.Text(u"Ducon")

def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    txt.set_text(repr(key))

list1 = urwid.ListBox([b1, b2, b3, txt])
loop = urwid.MainLoop(list1, unhandled_input=show_or_exit)
loop.run()

