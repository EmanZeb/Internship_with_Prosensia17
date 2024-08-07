def greet(language_code):
    if language_code == 'en':
        print("Hello")
    elif language_code == 'es':
        print("Hola")
    elif language_code == 'fr':
        print("Bonjour")
    else:
        print("Unknown language code")
greet('en')
greet('es')
greet('fr')
greet('de')