import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')

nonvalid_email = os.getenv('nonvalid_email')
nonvalid_password = os.getenv('nonvalid_password')

unformatted_email = os.getenv('unformatted_email')

one_character_password = os.getenv('one_character_password')
four_character_password = os.getenv('four_character_password')
five_character_password = os.getenv('five_character_password')

empty_email = os.getenv('empty_email')
empty_password = os.getenv('empty_password')

valid_reg_email = os.getenv('valid_reg_email')
valid_reg_password = os.getenv('valid_reg_password')


