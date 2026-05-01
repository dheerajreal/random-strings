import os
import pathlib
import shutil
import sys


here = pathlib.Path(__file__).parent.resolve()


class PublishCommand:
    def status(self, s: str):
        """Print things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def cleanup(self):
        try:
            self.status("Removing older builds")
            shutil.rmtree(os.path.join(here, "dist"))
        except FileNotFoundError:
            print("No older builds exist, Do nothing")

    def run(self):
        self.status("Building Source and Wheel")
        os.system("{0} -m build".format(sys.executable))

        self.status("Uploading to PyPi using Twine")
        os.system("twine upload dist/*")


if __name__ == "__main__":
    command = PublishCommand()
    command.cleanup()
    command.run()
    sys.exit()
