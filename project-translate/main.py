from google_trans_new import google_translator
import json, requests, random, re
import sys

text = sys.argv[1]
# text = input("Write something in english: ")

translator = google_translator()
translate_text = translator.translate(text, lang_src="en", lang_tgt="pt")
print(translate_text, end="")
