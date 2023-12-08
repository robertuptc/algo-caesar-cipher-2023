import string

alphabet = string.ascii_lowercase
upper_case_alphabet = string.ascii_uppercase

def caesar_cipher(string, shift_amount):
    string_to_list = (list(string))
    shifted_list = []
    checking_for_caps = ''

    for i in range(len(string_to_list)):
        # checking if the letter is uppercase or not
        if string_to_list[i].isupper():
            checking_for_caps = True
        else:
            checking_for_caps = False

        # converting each letter to lower case before runing the checks through the for loop
        string_to_list[i] = (string_to_list[i]).lower()

        if string_to_list[i] in alphabet:
            idx_letter_in_alphabet = alphabet.index(string_to_list[i])
            shifted_letter = 0

            # This IF statement make sure it loops around if count is greater than 25
            if idx_letter_in_alphabet + shift_amount > 25:
                total_shift = idx_letter_in_alphabet + shift_amount
                shifted_letter = alphabet[total_shift -len(alphabet)]
            else:
                shifted_letter = alphabet[idx_letter_in_alphabet + shift_amount]

            if checking_for_caps:
                shifted_list.append(shifted_letter.upper())
            else:
                shifted_list.append(shifted_letter)

        else:
            shifted_list.append(string_to_list[i])
    final_string = ''.join(shifted_list)
    return final_string

caesar_cipher("Boy! What a string!", -5)