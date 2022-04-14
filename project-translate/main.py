from google_trans_new import google_translator
import json, requests, random, re
import sys

lang = sys.argv[1]
text = sys.argv[2]
# text = input('Write something in english: ')

translator = google_translator()
if lang == "en":
    translate_text = translator.translate(text, lang_src="pt", lang_tgt="en")
elif lang == "pt":
    translate_text = translator.translate(text, lang_src="en", lang_tgt="pt")
else:
    print('Usage: <en|pt> "message to translate"')
    exit

print(translate_text, end="")
