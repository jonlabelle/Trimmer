import sublime
import sublime_plugin


class TrimmerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view

        trailing_white_space = view.find_all("[\t ]+$")
        trailing_white_space.reverse()

        edit = view.begin_edit()

        for r in trailing_white_space:
            view.erase(edit, r)

        view.end_edit(edit)

        sublime.set_timeout(lambda: self.save(), 100)

    def save(self):
        if self.view.file_name() is None:
            self.view.run_command('prompt_save_as')
        else:
            self.view.run_command('save')
            
        sublime.status_message('Trimmer: Remove trailing whitespace and save.')