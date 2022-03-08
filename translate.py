import sys
s = open(sys.argv[1], "r", encoding = "utf-8" )
f = open(sys.argv[2], "w")
textak = s.read()

from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='auto',target='czech')

text_to_translate = textak

translated_text = translator.translate(text_to_translate)

print(translated_text)

f.write(translated_text)
