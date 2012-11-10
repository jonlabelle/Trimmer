import sublime
import sublime_plugin


class TrimmerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        save_after_trim = sublime.load_settings("Trimmer.sublime-settings").get('save_after_trim', False)

        trailing_white_space = view.find_all("[\t ]+$")
        trailing_white_space.reverse()

        for r in trailing_white_space:
            view.erase(edit, r)

        if save_after_trim is True:
            sublime.set_timeout(lambda: self.save(view), 10)

    def save(self, view):
        if view.file_name() is None:
            view.run_command('prompt_save_as')
        else:
            view.run_command('save')
        sublime.status_message('Trimmer: Removed trailing whitespace and saved.')
