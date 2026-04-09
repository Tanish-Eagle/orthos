from checker import LanguageToolChecker


def interactive_edit(text):
    checker = LanguageToolChecker()

    while True:
        matches = checker.check(text)

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
        print("q = quit")

        choice = input("> ").strip()

        if choice == "q":
            return text

        elif choice == "s":
            # skip this issue by inserting a space (simple trick)
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