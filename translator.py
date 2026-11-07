from deep_translator import MyMemoryTranslator
print("===== LANGUAGE TRANSLATOR =====")

languages = {
    1: ("English", "en-IN"),
    2: ("Hindi", "hi-IN"),
    3: ("Kannada", "kn-IN"),
    4: ("French", "fr-FR"),
    5: ("Spanish", "es-ES")
}

while True:
    text = input("\nEnter the text to translate: ")

    print("\nAvailable languages:")
    for number, (name, code) in languages.items():
        print(f"{number}. {name}")

    try:
        source_num = int(input("\nEnter source language number: "))
        target_num = int(input("Enter target language number: "))

        if source_num not in languages or target_num not in languages:
            print("Invalid language number.")
            continue

        source = languages[source_num][1]
        target = languages[target_num][1]

        print("\nTranslating...")

        translated = MyMemoryTranslator(
            source=source,
            target=target
        ).translate(text)

        print("\nTranslated Text:")
        print(translated)

    except Exception as e:
        print("\nTranslation failed.")
        print("Error:", e)

    again = input("\nTranslate another sentence? (y/n): ")

    if again.lower() != "y":
        print("\nThank you for using the Language Translator!")
        break