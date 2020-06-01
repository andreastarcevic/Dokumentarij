import unittest
from dokumentarij import DokumentarijModel, DokumentarijView, DokumentarijController

class DokumentarijTestCase(unittest.TestCase):

    def test_if_someone_in_shownames(self):
        game_test = DokumentarijController(DokumentarijModel(), DokumentarijView())
        number_of_students = len(names)
        self.assertGreater(number_of_students, 0, "U bazi imena studenata nije nitko na popisu")

    def test_getnewname(self):
        game_test = DokumentarijController(DokumentarijModel(), DokumentarijView())
        new_name = game_test.view.create_names()
        self.assertEqual(str(new_name), "Dodaju se imena studenata u listu")


if __name__ == "__main__":
    unittest.main()
