import argparse

import pywebio

from pywebio.input import input, FLOAT,TEXT
from pywebio.output import put_text,put_error,put_html,put_image








alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
  , 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
  , 'u', 'v', 'w', 'x', 'y', 'z',]


def caesar():
 img = open('image/caesar.png','rb').read()
 put_image(src=img)
 method = input('DECODE OR ENCODE').lower()
 text = input('TYPE YOUR TEXT')
 shift_entry = input('ENTER THE SHIFT NUMBER')
 if text == '' or method == '' or shift_entry == '':
     put_error('Do not leave any field empty')
 else:

  try:
     shift_amount = [int(chars) for chars in shift_entry]
  except:
     put_error('Enter a valid shift number')
  else:
    start_text = text.lower()

    shift = shift_amount[0] % 26
    end_text = ""
    if method == "decode":
     shift_amount[0] *= -1
    for char in start_text:


       if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount[0]
        end_text += alphabet[new_position]

       else:
        end_text += char
    put_html(f'<h1 style ="text-align:center">Your {method}d text is 👇\n{end_text}</h1>')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=7700)
    args =parser.parse_args()
    pywebio.start_server(caesar,port=args.port)




























































