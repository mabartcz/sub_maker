import os

from srtranslator import SrtFile
from srtranslator.translators.deepl_api import DeeplApi
from srtranslator.translators.deepl_scrap import DeeplTranslator
from srtranslator.translators.translatepy import TranslatePy

# translator = DeeplTranslator()
translator = TranslatePy()

filepath = r"C:\Users\Martin\source\repos\sub_maker\data\out.srt"
srt = SrtFile(filepath)
srt.translate(translator, "en", "cs")

# Making the result subtitles prettier
srt.wrap_lines()

srt.save(f"{os.path.splitext(filepath)[0]}_translated.srt")

translator.quit()
