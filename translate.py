from deep_translator import GoogleTranslator
translated = GoogleTranslator(source='auto', target='czech').translate_file('save.txt')
print(translated)
