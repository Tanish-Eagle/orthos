from checker import LanguageToolChecker

text = "This are bad sentence."

checker = LanguageToolChecker()

matches = checker.check(text)

for m in matches:
    print("Error:", text[m["offset"]: m["offset"] + m["length"]])
    print("Message:", m["message"])
    print("Suggestions:", [r["value"] for r in m["replacements"]])
    print()