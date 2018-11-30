from unittest import TestCase, main
import logging

#logging.basicConfig(name='arquivo.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.basicConfig(filename='arquivo.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def palindrome(palavra):
    logging.info('estou na funcao')
    return True if palavra[::-1] == palavra else False

class Teste(TestCase):
    def test_palin(self):
        logging.warning('comecou')
        self.assertEqual(palindrome('ovo'),True)
        self.assertEqual(palindrome('daniel'), False)
        self.assertEqual(palindrome('osso'),True)
        self.assertEqual(palindrome('reviver'),True)
        self.assertEqual(palindrome('python'),False)
        logging.info('terminou')

if __name__ == "__main__":
    logging.info('estou na main')
    main()
        