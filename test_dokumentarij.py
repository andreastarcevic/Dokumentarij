import unittest
from dokumentarij import Dokumentarij

class DokumentarijTestCase(unittest.TestCase):

    def test_if_someone_in_shownames(self):
        game_test = Dokumentarij()
        names = game_test.show_names()
        self.assertEqual(str(names), "U bazi se nalaze imena studenata")

    def test_getnewname(self):
        game_test = Dokumentarij()
        new_name = game_test.create_names()
        self.assertEqual(str(new_name), "Dodaju se imena studenata u listu")


if __name__ == "__main__":
    unittest.main()