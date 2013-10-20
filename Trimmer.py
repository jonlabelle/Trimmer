import sublime
import sublime_plugin
import re


class DeleteEmptyLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        reobj = re.compile("^[ \t]*$\r?\n", re.MULTILINE)
        selections = self.get_selections()

        for sel in selections:
            trimmed = reobj.sub("", self.view.substr(sel))
            self.view.replace(edit, sel, trimmed)

        sublime.status_message(
            'Trimmer: empty lines deleted.')

    def get_selections(self):
        selections = self.view.sel()

        # check for selections
        has_selections = False
        for sel in selections:
            if sel.empty() is False:
                has_selections = True

        # if no selections, use the file as selection
        if not has_selections:
            full_region = sublime.Region(0, self.view.size())
            selections.add(full_region)

        return selections


class TrimLeadingWhitespaceCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        reobj = re.compile("^[ \t]+", re.MULTILINE)
        selections = self.get_selections()

        for sel in selections:
            edited_text = reobj.sub("", self.view.substr(sel))
            self.view.replace(edit, sel, edited_text)

        sublime.status_message('Trimmer: leading whitespace trimmed.')

    def get_selections(self):
        selections = self.view.sel()

        # check for selections
        has_selections = False
        for region in selections:
            if region.empty() is False:
                has_selections = True

        # if no selections, use the file as selection
        if not has_selections:
            full_region = sublime.Region(0, self.view.size())
            selections.add(full_region)

        return selections


class TrimmerCommand(sublime_plugin.TextCommand):

    """Trim whitespace at the end of each line."""

    def run(self, edit):
        view = self.view

        trim = view.find_all("[\t ]+$")
        trim.reverse()

        for r in trim:
            view.erase(edit, r)

        sublime.status_message('Trimmer: trailing whitespace removed.')
