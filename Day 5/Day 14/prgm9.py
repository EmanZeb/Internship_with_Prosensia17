def match_pattern(string, pattern):

  pattern_regex = "^" + "".join(f"[{char.lower()}{char.upper()}]" if char.isalpha() else r"\d" for char in pattern) + "$"
  return bool(re.match(pattern_regex, string))

# Exmp used
string = "a1B2"
pattern = "a1b2"
result = match_pattern(string, pattern)
print(result)  