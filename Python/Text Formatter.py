def format_text(text, max_length):
    char_count = 0
    output_text = ""

    for letter in text:
        # check if space is first character
        if letter == " " and char_count == 0:
            pass

        # check if space is last character
        elif letter == " " and char_count == max_length - 1:
            output_text += "\n"
            char_count = 0

        # add character
        else:
            output_text += letter
            char_count += 1
        
        if (char_count >= max_length) and letter == " ":
            output_text += "\n"
            char_count = 0

    return output_text
