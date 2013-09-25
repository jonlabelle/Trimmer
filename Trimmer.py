import sublime
import sublime_plugin
import re


class TrimmerCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view

        settings = sublime.load_settings("Trimmer.sublime-settings")
        save_after_trim = settings.get('save_after_trim', False)
        trim_eof = settings.get('trim_eof', False)

        trailing_white_space = view.find_all("[\t ]+$")
        trailing_white_space.reverse()

        for r in trailing_white_space:
            view.erase(edit, r)

        if trim_eof is True:
            self.trim_eof_whitespace(edit, view)

        if save_after_trim is True:
            sublime.set_timeout(lambda: self.save(view), 10)
        else:
            sublime.status_message('Trimmer: trailing whitespace removed.')

    def trim_eof_whitespace(self, edit, view):
        if view.size() > 0:
            eofc = "\n" if view.settings().get(
                "ensure_newline_at_eof_on_save") is True else ""
            region = sublime.Region(0, view.size())

            edited_text = re.sub(
                r"(?m)[\s]*$(?![\w\W])", eofc, view.substr(region))
            view.replace(edit, region, edited_text)

    def save(self, view):
        if view.file_name() is None:
            view.run_command('prompt_save_as')
        else:
            view.run_command('save')

        sublime.status_message(
            'Trimmer: trailing whitespace removed and file saved.')
