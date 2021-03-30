import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_aloitus(self):
        self.assertEqual(str(self.kassapaate), "saldo: 1000.0, lounaita myyty 0")

    def test_vaihtoraha_oikein_kateisella_edullinen_kun_riittava_maksu(self):
        value = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(value,10)

    def test_kateisella_makoisa_kun_riittava_maksu(self):
        value = self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(value,10)

    def test_kassapaate_rahamaara_oikein_kateisella_edullinen_kun_riittava_maksu(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(str(self.kassapaate), "saldo: 1002.4, lounaita myyty 1")

    def test_kassapaate_rahamaara_oikein_kateisella_maukas_kun_riittava_maksu(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.kassapaate), "saldo: 1004.0, lounaita myyty 1")

    def test_vaihtoraha_oikein_kateisella_edullinen_kun_ei_riittava_maksu(self):
        value = self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(value,230)

    def test_vaihtoraha_oikein_kateisella_maksullinen_kun_ei_riittava_maksu(self):
        value = self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(value,390)

    def test_kassapaate_rahamaara_oikein_kateisella_edullinen_kun_ei_riittava_maksu(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(str(self.kassapaate), "saldo: 1000.0, lounaita myyty 0")

    def test_korttiosto_toimii_edullisella_lounaalla_kun_riittavasti_saldoa(self):
        value = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(value, True)

    def test_korttiosto_toimii_maukkaalla_lounaalla_kun_riittavasti_saldoa(self):
        value = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(value, True)

    def test_korttiosto_edullinen_lounas_kortilla_riittavasti_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate), "saldo: 1000.0, lounaita myyty 1")

    def test_korttiosto_maukas_lounas_kortilla_riittavasti_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate), "saldo: 1000.0, lounaita myyty 1")

    def test_korttiosto_edullinen_lounas_kortilla_ei_riittavasti(self):
        kortti = Maksukortti(10)
        value = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(value, False)

    def test_korttiosto_maukas_lounas_kortilla_ei_riittavasti(self):
        kortti = Maksukortti(10)
        value = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(value, False)

    def test_kortin_saldo_muuttuu_edullinen_lounas(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")

    def test_kortin_saldo_muuttuu_maukas_lounas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")

    def test_kassan_rahamaara_muuttuu_kortille_ladatessa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 300)
        self.assertEqual(str(self.kassapaate), "saldo: 1003.0, lounaita myyty 0")

    def test_kortin_saldo_muuttuu_kortille_ladatessa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 300)
        self.assertEqual(str(self.maksukortti), "saldo: 13.0")

    def test_kortille_lataa_negatiivinen_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")