from translate import Translator
translator = Translator(to_lang='ja')

try:
    with open('C:\Users\Gaurav\OneDrive\Desktop\python\all new python\happy.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
except:
    print('check your file path')
        
 
