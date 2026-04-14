from checker import LanguageToolChecker


def load_dictionary(path="orthos_words.txt"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            # store everything in lowercase
            return set(line.strip().lower() for line in f if line.strip())
    except FileNotFoundError:
        return set()


def interactive_edit(text):
    checker = LanguageToolChecker()

    ignored_rules = set()
    custom_words = load_dictionary()

    while True:
        matches = checker.check(text)

        # Filter ignored rules
        matches = [m for m in matches if m["rule"]["id"] not in ignored_rules]

        # Filter custom dictionary words (ONLY for spelling issues)
        def is_ignored_word(match):
            word = text[match["offset"]: match["offset"] + match["length"]]
            word_lower = word.lower()

            issue_type = match["rule"].get("issueType", "")

            # Only ignore if it's a spelling issue
            if issue_type == "misspelling" and word_lower in custom_words:
                return True

            return False

        matches = [m for m in matches if not is_ignored_word(m)]

        if not matches:
            print("\nNo more issues found.")
            return text

        match = matches[0]

        start = match["offset"]
        end = start + match["length"]

        error_text = text[start:end]

        print("\n--- Issue Found ---")

        # Context display
        context = match["context"]["text"]
        context_offset = match["context"]["offset"]
        context_length = match["context"]["length"]

        print(context)

        pointer = " " * context_offset + "^" * context_length
        print(pointer)

        print("\nError:", error_text)
        print("Message:", match["message"])

        rule_id = match["rule"]["id"]
        print("Rule:", rule_id)

        suggestions = [r["value"] for r in match["replacements"]]

        if suggestions:
            print("\nSuggestions:")
            for i, s in enumerate(suggestions, 1):
                print(f"{i}. {s}")
        else:
            print("\n(No suggestions available)")

        print("\nOptions:")
        print("number = apply suggestion")
        print("s = skip")
        print("e = edit manually")
        print("i = ignore this rule")
        print("w = add word to dictionary")
        print("q = quit")

        choice = input("> ").strip()

        if choice == "q":
            return text

        elif choice == "i":
            ignored_rules.add(rule_id)
            print(f"Rule {rule_id} ignored for this session.")
            continue

        elif choice == "w":
            word = error_text.strip()
            word_lower = word.lower()

            # avoid duplicates
            if word_lower not in custom_words:
                custom_words.add(word_lower)

                with open("orthos_words.txt", "a", encoding="utf-8") as f:
                    f.write(word_lower + "\n")

                print(f'Word "{word}" added to dictionary.')
            else:
                print(f'Word "{word}" is already in dictionary.')

            continue

        elif choice == "s":
            text = text[:end] + " " + text[end:]
            continue

        elif choice == "e":
            replacement = input("Enter replacement: ")
            text = text[:start] + replacement + text[end:]
            continue

        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(suggestions):
                replacement = suggestions[index]
                text = text[:start] + replacement + text[end:]
            else:
                print("Invalid suggestion number.")

        else:
            print("Invalid choice.")