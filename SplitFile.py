#!/usr/bin/python

"Splits the currently open view into two separate panes."

__author__ = 'Brian Hunter'
__email__  = 'brian.hunter@gmail.com'

import sublime_plugin

class SplitFileCommand(sublime_plugin.WindowCommand):
    def run(self):
        my_buffer = self.window.active_view().buffer_id()
        first_group = self.window.active_group()
        self.window.run_command("set_layout", {"cells": [[0, 0, 1, 1]], "cols": [0.0, 1.0], "rows": [0.0, 1.0]})
        self.window.run_command("clone_file")
        self.window.run_command("new_pane")
        self.window.focus_group(first_group)
        
        buffers = self.window.views_in_group(self.window.active_group())
        final_view = None
        for buff in buffers:
            if buff.buffer_id() == my_buffer:
                if final_view is None:
                    final_view = buff
                else:
                    self.window.focus_view(buff)
                    self.window.run_command("close")
        self.window.focus_view(final_view)
