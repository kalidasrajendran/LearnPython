from translate import Translator


def translate_line(data, language):
    translator = Translator(to_lang=language)
    translations = translator.translate(data)

    return translations


try:
    filepath = 'D:\\1_Learning\\C_C++\\Repo\\2021_10_18\\LearnCPlusPlus\\Python\\File_IO\\test.txt'
    filewrite = 'D:\\1_Learning\\C_C++\\Repo\\2021_10_18\\LearnCPlusPlus\\Python\\File_IO\\translated.txt'
    myfile = open(filepath, 'r')
    writefile = open(filewrite, 'w')

    for line in myfile:
        result = translate_line(line, 'de')
        writefile.writelines(result + '\n')
        print('original', line, ' translated: ', result)

except FileNotFoundError as err:
    print('file not found', err)
except IOError as err:
    print('IO error occured', err)