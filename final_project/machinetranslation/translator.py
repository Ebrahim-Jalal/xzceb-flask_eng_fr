'''
Installing required libraries
'''
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('IesKMeQrUy-KmbLKaGpC9dwnJwEZVq34l9rZdneP0hSO')
language_translator = LanguageTranslatorV3(
    version='2021-09-22',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')


def english_to_french(english_text):
    '''
    Translation from English to French
    '''
    if english_text ==  None:
        return None
    else:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr'
        ).get_result()
        return translation['translations'][0]['translation']

def french_to_english(french_text):
    '''
    Translation from French to English
    '''
    if french_text ==  None:
        return None
    else:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en'
        ).get_result()
        return translation['translations'][0]['translation']
