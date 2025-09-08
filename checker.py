# checker.py
# This file contains all the hidden test logic.
# The students will not see this file's contents.

from IPython.display import display, Markdown

class _Checker:
    """
    A class to hold all the checking functions. It uses the `locals()`
    dictionary from the notebook to inspect the student's variables.
    """
    def _display_feedback(self, correct, message):
        """Standardized feedback display."""
        if correct:
            display(Markdown(f"✅ **Correct!** {message}"))
        else:
            display(Markdown(f"❌ **Not quite right.** {message}"))

    def check_q1(self, local_vars):
        """Checks the answer for Question 1."""
        try:
            assert 'first_name' in local_vars, "The variable `first_name` does not exist. Check for typos."
            first_name = local_vars['first_name']
            assert isinstance(first_name, str), f"The variable `first_name` should be a string, but it is a `{type(first_name).__name__}`."
            assert first_name == "Ada", f"Expected the value `'Ada'`, but got `'{first_name}'`."
            self._display_feedback(True, "Great job creating the variable.")
        except AssertionError as e:
            self._display_feedback(False, str(e))

    def check_q2(self, local_vars):
        """Checks the answer for Question 2."""
        try:
            assert 'primes' in local_vars, "The variable `primes` does not exist."
            primes = local_vars['primes']
            assert isinstance(primes, list), f"`primes` should be a list, but it's a `{type(primes).__name__}`."
            assert len(primes) == 5, f"The list should have 5 items, but yours has {len(primes)}."
            assert primes[-1] == 11, f"The last item in the list should be 11, but it is `{primes[-1]}`."
            self._display_feedback(True, "The list is perfect.")
        except AssertionError as e:
            self._display_feedback(False, str(e))

    def check_q3(self, local_vars):
        """Checks the answer for Question 3."""
        try:
            assert 'user_info' in local_vars, "The dictionary `user_info` does not exist."
            user_info = local_vars['user_info']
            assert isinstance(user_info, dict), f"`user_info` should be a dictionary, but it's a `{type(user_info).__name__}`."
            assert 'city' in user_info, "The dictionary is missing the key `'city'`."
            city = user_info['city']
            assert city.lower() == 'berlin', f"The value for `'city'` should be `'Berlin'`, but it was `'{city}'`."
            self._display_feedback(True, "You correctly retrieved the value from the dictionary.")
        except AssertionError as e:
            self._display_feedback(False, str(e))
        except Exception as e:
             self._display_feedback(False, f"An unexpected error occurred: {e}")


# Create a single, importable instance of the checker.
checker = _Checker()
