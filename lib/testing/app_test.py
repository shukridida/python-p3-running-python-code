import subprocess
import io
import sys
import runpy
from os import path

class TestAppPy:
    '''
    app.py
    '''
    def test_app_py_exists(self):
        '''
        exists in lib directory
        '''
        assert(path.exists("lib/app.py"))

    def test_app_py_runs(self):
        '''
        is executable
        '''
        runpy.run_path("lib/app.py")

    def test_prints_hello_world(self):
        '''
        prints "Hello World! Pass this test, please."
        '''
        # Capture the output of the script
        captured_out = io.BytesIO() if sys.version_info[0] == 2 else io.StringIO()
        sys.stdout = captured_out

        try:
            # Run the script
            runpy.run_path("lib/app.py")
        finally:
            sys.stdout = sys.__stdout__

        # Convert captured output to string
        captured_out_str = captured_out.getvalue().decode('utf-8') if sys.version_info[0] == 2 else captured_out.getvalue()

        # Check if the expected string is in the captured output
        assert "Hello World! Pass this test, please." in captured_out_str.strip()

if __name__ == "__main__":
    pytest.main()