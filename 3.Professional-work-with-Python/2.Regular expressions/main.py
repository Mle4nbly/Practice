from pprint import pprint
import re
import csv


with open("RegularExpressions\phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  final_list = []


def formatting_numbers():
  phone_pattern = re.compile(r'(8|\+7)\s*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})(\s)*\(*(доб.)*\s*(\d+)*\)*')
  phone_substitution = r'+7(\2)\3-\4-\5\6\7\8'
  for column in contacts_list:
    column[5] = phone_pattern.sub(phone_substitution, column[5])


def formatting_names():
    name_pattern = r'([А-Я])'
    name_substitution = r' \1'
    for column in contacts_list[1:]:
      line = column[0] + column[1] + column[2]
      if len((re.sub(name_pattern, name_substitution, line).split())) == 3:
        column[0] = re.sub(name_pattern, name_substitution, line).split()[0]
        column[1] = re.sub(name_pattern, name_substitution, line).split()[1]
        column[2] = re.sub(name_pattern, name_substitution, line).split()[2]
      elif len((re.sub(name_pattern, name_substitution, line).split())) == 2:
        column[0] = re.sub(name_pattern, name_substitution, line).split()[0]
        column[1] = re.sub(name_pattern, name_substitution, line).split()[1]
        column[2] = ''
      elif len((re.sub(name_pattern, name_substitution, line).split())) == 1:
        column[0] = re.sub(name_pattern, name_substitution, line).split()[0]
        column[1] = ''
        column[2] = ''


def removing_dublicates():
    for column in contacts_list:
      firstname = column[1]
      lastname = column[0]
      for contact in contacts_list:
        firstname_dubl = contact[1]
        lastname_dubl = contact[0]
        if firstname == firstname_dubl and lastname == lastname_dubl:
          if column[1] == '':
            column[1] = contact[1]
          if column[2] == '':
            column[2] = contact[2]
          if column[3] == '':
            column[3] = contact[3]
          if column[4] == '':
            column[4] = contact[4]
          if column[5] == '':
            column[5] = contact[5]
          if column[6] == '':
            column[6] = contact[6]
          if len(column) > 7:
            del column[7:len(column)]
            
    for column in contacts_list:
      if column not in final_list:
        final_list.append(column)                


if __name__ == '__main__':
  formatting_numbers()
  formatting_names()
  removing_dublicates()
  
  with open("RegularExpressions\phonebook.csv", "w+") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_list)
    pprint(final_list)