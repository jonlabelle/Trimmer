import sublime
import sublime_plugin


class TrimmerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        trailing_white_space = self.view.find_all("[\t ]+$")
        trailing_white_space.reverse()

        edit = self.view.begin_edit()

        for r in trailing_white_space:
            self.view.erase(edit, r)

        self.view.end_edit(edit)

        # save
        if self.view.file_name() is None:
            self.view.run_command('prompt_save_as')
        else:
            self.view.run_command('save')

        sublime.status_message('Trimmer: Remove trailing whitespace and save.')