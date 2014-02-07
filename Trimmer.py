import sublime
import sublime_plugin
import re


class TrimmerEvents(sublime_plugin.EventListener):
    '''An EventListener class to utilize Sublime's events.'''

    def on_pre_save(self, view):
        '''
        When the file is being saved, check if we're configured to
        run any of these commands on the file.
        '''

        run_on_save = sublime.load_settings('Trimmer.sublime-settings').get('run_on_save')

        if run_on_save in ["trimmer", "trim_leading_whitespace", "trim_leading_trailing_whitespace", "delete_empty_lines"]:
            view.run_command(run_on_save)


class DeleteEmptyLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        reobj = re.compile("^[ \t]*$\r?\n", re.MULTILINE)
        selections = self.get_selections()

        for sel in selections:
            trimmed = reobj.sub("", self.view.substr(sel))
            self.view.replace(edit, sel, trimmed)

        sublime.status_message("Trimmer: empty lines deleted.")

    def get_selections(self):
        selections = self.view.sel()

        has_selections = False
        for sel in selections:
            if sel.empty() is False:
                has_selections = True

        if not has_selections:
            full_region = sublime.Region(0, self.view.size())
            selections.add(full_region)

        return selections


class TrimLeadingWhitespaceCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        reobj = re.compile("^[ \t]+", re.MULTILINE)
        selections = self.get_selections()

        for sel in selections:
            trimmed = reobj.sub("", self.view.substr(sel))
            self.view.replace(edit, sel, trimmed)

        sublime.status_message("Trimmer: leading whitespace removed.")

    def get_selections(self):
        selections = self.view.sel()

        has_selections = False
        for sel in selections:
            if sel.empty() is False:
                has_selections = True

        if not has_selections:
            full_region = sublime.Region(0, self.view.size())
            selections.add(full_region)

        return selections


class TrimLeadingTrailingWhitespace(sublime_plugin.TextCommand):

    def run(self, edit):
        reobj = re.compile("^[ \t]+|[\t ]+$", re.MULTILINE)
        selections = self.get_selections()

        for sel in selections:
            trimmed = reobj.sub("", self.view.substr(sel))
            self.view.replace(edit, sel, trimmed)

        sublime.status_message(
            "Trimmer: leading and trailing whitespace removed.")

    def get_selections(self):
        selections = self.view.sel()

        has_selections = False
        for sel in selections:
            if sel.empty() is False:
                has_selections = True

        if not has_selections:
            full_region = sublime.Region(0, self.view.size())
            selections.add(full_region)

        return selections


class TrimmerCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view

        matched_regions = view.find_all("[\t ]+$")
        matched_regions.reverse()

        for r in matched_regions:
            view.erase(edit, r)

        sublime.status_message("Trimmer: trailing whitespace removed.")
