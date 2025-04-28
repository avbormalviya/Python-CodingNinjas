# Problem statement

""" Given two string scratch_KNN.py and t, write a function to check if scratch_KNN.py contains all characters of t (in the same order as they
are in string t).

Return true or false.
Do it recursively. """


# solution


def is_substring(s, t):
    # Base case: if `t` is empty, it is a substring
    if not len(t):
        return True

    # Base case: if `scratch_KNN.py` is shorter than `t`, `t` cannot be a substring
    if len(s) < len(t):
        return False

    # If the first character matches, check the rest of `t` in `scratch_KNN.py`
    if s[0] == t[0]:
        if is_substring(s[1:], t[1:]):  # Recursively check the rest
            return True

    # Otherwise, move to the next character in `scratch_KNN.py` and restart the check
    return is_substring(s[1:], t)


# Input strings
s = input()
t = input()

# Check if t is a substring of scratch_KNN.py
print(is_substring(s, t))
