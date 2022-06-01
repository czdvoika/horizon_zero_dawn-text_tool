import sys
s = open(sys.argv[1], "r", encoding = "utf-8" )
f = open(sys.argv[2], "w")
i = 1


while i <22:
 textak = s.readline()

 from deep_translator import GoogleTranslator
 translator = GoogleTranslator(source='slovak',target='czech')

 text_to_translate = textak

 translated_text = translator.translate(text_to_translate)

 print(translated_text)

 f.write(translated_text)
 f.write("\n")
 i += 1
