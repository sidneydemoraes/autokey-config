# Enter script code

retCode, dice_formula = dialog.input_dialog(title='Dice Roller', message='Digite a fórmula')

if retCode > 0:
    dialog.info_dialog(title='Unknown Error!', message=f"Rolagem cancelada. Ret code {retcode}, mensagem {dice_formula}.")
    exit()

dice_formula = dice_formula.lower().replace(' ', '')

TITLE_FORMULA_ERROR = 'Dice Formula Error!'
FORMULA_EXAMPLE = '2d10+5'

index_of_d = dice_formula.find('d')
if index_of_d < 0:
    dialog.info_dialog(title=TITLE_FORMULA_ERROR, message=f"Fórmula inválida. A fórmula deve ser similar a este exemplo: {FORMULA_EXAMPLE}")
    exit()

number_of_dice = dice_formula[:index_of_d]
try:
    number_of_dice = int(number_of_dice)
except ValueError:
    dialog.info_dialog(title=TITLE_FORMULA_ERROR, message=f"Fórmula inválida. Antes da letra 'd' deve ser inserido um número. Você inseriu {number_of_dice}.")
    exit()

import re
match_of_modifier = re.search(r"[+-]", dice_formula)
if match_of_modifier:
    index_of_modifier = match_of_modifier.start()
    modifier = match_of_modifier.group(0)
    modifier_amount = dice_formula[index_of_modifier +1 :]
    try:
        modifier_amount = int(modifier_amount)
    except ValueError:
        dialog.info_dialog(title=TITLE_FORMULA_ERROR, message=f"Fórmula inválida. O modificador deve ser um número. Você inseriu {modifier_amount}.")
        exit()
    if modifier == '-':
        modifier_amount = -modifier_amount
    number_of_sides = dice_formula[index_of_d +1 : index_of_modifier]
else:
    modifier_amount = 0
    number_of_sides = dice_formula[index_of_d +1 :]

try:
    number_of_sides = int(number_of_sides)
except ValueError:
    dialog.info_dialog(title=TITLE_FORMULA_ERROR, message=f"Fórmula inválida. Depois da letra 'd' deve ser inserido um número. Você inseriu {number_of_sides}.")
    exit()

all_rolls = []
import random
for roll in range(number_of_dice):
    all_rolls.append(random.randint(1, number_of_sides))

individual_rolls = '[' + ', '.join(list(map(str, all_rolls))) + ']'
total_roll = sum(all_rolls) + modifier_amount
dialog.info_dialog(title=f"Resultado:", message=f"Total: {total_roll}\r\n{individual_rolls}\r\nFórmula: {dice_formula}")

