import string

alphabet = string.ascii_lowercase
upper_case_alphabet = string.ascii_uppercase

def caesar_cipher(string, shift_amount):
    string_to_list = (list(string))
    shifted_list = []
    
    for i in range(len(string_to_list)):
        if string_to_list[i] in alphabet:
            idx_letter_in_alphabet = alphabet.index(string_to_list[i])
            shifted_letter = 0

            # This IF statement make sure it loops around if count is greater than 25
            if idx_letter_in_alphabet + shift_amount > 25:
                total_shift = idx_letter_in_alphabet + shift_amount
                shifted_letter = alphabet[total_shift -len(alphabet)]
            else:
                shifted_letter = alphabet[idx_letter_in_alphabet + shift_amount]

            if string_to_list[i].isupper():
                shifted_list.append(shifted_letter.upper())
            else:
                shifted_list.append(shifted_letter)
        else:
            shifted_list.append(string_to_list[i])
            
        print(shifted_list)

caesar_cipher("hats", -5)