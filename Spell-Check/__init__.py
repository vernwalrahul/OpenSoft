import spellcheck
import spellcheck1
import spellcheck2
import sys

def main():
    # spellchk = SpellCheck('/usr/share/dict/words')
    if sys.argv[1] == '0':
        spellchk = spellcheck.SpellCheck('MedWords.csv')
        spellchk.run('0')
    elif sys.argv[1] == '1':
        spellchk = spellcheck1.SpellCheck('MedWords.csv')
        spellchk.run('0')
    elif sys.argv[1] == '2':
        spellchk = spellcheck2.SpellCheck('MedWords.csv')
        spellchk.run('0')
if __name__ == "__main__":
    main()
