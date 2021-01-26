import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_nollaa_virheelliset_parametrit(self):
        self.varasto2 = Varasto(0, -1)
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)
        self.assertAlmostEqual(self.varasto2.saldo, 0)
    
    def test_konstruktori_alku_saldo_mahtuu(self):
        self.varasto2 = Varasto(1000, 123)
        self.assertAlmostEqual(self.varasto2.saldo, 123)

    def test_konstruktori_alku_saldo_ei_mahdu(self):
        self.varasto2 = Varasto(123, 1000)
        self.assertAlmostEqual(self.varasto2.saldo, 123)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_negatiivisella_marralla_ei_tee_mitaan(self):       
        saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, saldo)
        
    def test_lisays_maara_mahtuu(self):
        self.varasto2 = Varasto(123)
       
        saldo = self.varasto2.saldo
        self.varasto2.lisaa_varastoon(123)
        self.assertAlmostEqual(self.varasto2.saldo, 123)

    def test_lisays_maara_ei_mahdu(self):
        self.varasto2 = Varasto(123)
       
        saldo = self.varasto2.saldo
        self.varasto2.lisaa_varastoon(1337)
        self.assertAlmostEqual(self.varasto2.saldo, 123)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_ottaminen_negatiivisella_maaralla_ei_tee_mitaan(self):
        self.varasto.lisaa_varastoon(8)
        
        saldo = self.varasto.saldo
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, saldo)


    def test_ottaminen_maara_suurempi_kuin_saldo(self):
        self.varasto2 = Varasto(123)
       
        saldo = self.varasto2.saldo
        self.varasto2.ota_varastosta(1337)
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_toString_palauttaa_oikein(self):
        self.assertEqual(
                    self.varasto.__str__(),
                    f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}"
                ) 
