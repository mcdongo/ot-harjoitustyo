import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(90)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_kortin_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(9)
        self.assertEqual(str(self.maksukortti), "saldo: 0.01")

    def test_kortin_saldo_ei_muutu_jos_rahaa_ei_ole_riittavasti(self):
        self.maksukortti.ota_rahaa(150)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_metodi_palauttaa_true_jos_rahat_riittavat(self):
        value = self.maksukortti.ota_rahaa(5)
        self.assertEqual(value, True)

    def test_metodi_palauttaa_false_jos_rahat_eivat_riita(self):
        value = self.maksukortti.ota_rahaa(15)
        self.assertEqual(value, False)