from pyxform.tests_v1.pyxform_test_case import PyxformTestCase
from pyxform.xls2json import RSA_is_valid
from base64 import b64decode

try:
    from unittest import mock
except ImportError:
    import mock


class RSATest(PyxformTestCase):
    """
    Checks For RSA public key validity in xls2json module
    """

    def test_RSA_with_bad_64_encodings(self):
        """
        Public_key should be a valid b64 decodable string
        """
        key5 = """MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwOHPJWD9zc8JPBZj/UtC
dHiY7I4HWt61UG1XRaGvvwUkC/y8P5Kk6dRnf3yMTBHQoisT2vU2ODWVaU5elndk
hiKiWdhufp1d86FWGYz/i+VOmdoV+0zoyPzk+vTEG8bpiY7/UcDYY0CsrRmaMei1
15xZwQpSMpayqMjemvwGDyhy2B3Yize4yaxyLFG53wMrHEczzsYz8FuRfuKUleE/
6jFc3uXZET4LJ7S76n1XU+bE+mhhoZ+tVERgaVH38l0SZljBITwHeqQ9WQckkmDf
bRHBG7TQm+Afnx0s5E2bGIT5jB5cj9YaX6BqZSeodpafQjpXEJg6uufxF1Ni3Btv
4wIDAQ
"""
        self.assertFalse(RSA_is_valid(key5))

    def test_RSA_with_bad_RSA_structure(self):
        """
        Public_key should parse into a RSA structure without Errors
        and decodes to b64 without error to be termed valid
        """
        key6 = """MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwOHPJWD9zc8JPBZj/UtC
dHiY7I4HWt61UG1XRaGvvwUkC/y8P5Kk6dRnf3yMTBHQoisT2vU2ODWVaU5elndk
hiKiWdhufp1d86FWGYz/i+VOmdoV+0zoyPzk+vTEG8bpiY7/UcDYY0CsrRmaMei1
15xZwQpSMpayqMjemvwGDyhy2B3Yize4yaxyLFG53wMrHEczzsYz8FuRfuKUleE/
6jFc3uXZET4LJ7S76n1XU+bE+mhhoZ+tVERgaVH38l0SZljBITwHeqQ9WQckkmDf
bRHBG7TodpafQjpXEJgQm+Afnx0s5E2bGIT5jB5cj9YaX6BqZSe6uufxF1Ni3Btv
AQAB4wID
"""
        try:
            decoded_key = b64decode(key6)
        except:
            self.fail()
        self.assertFalse(RSA_is_valid(key6))

    def test_RSA_with_valid_keys(self):
        """
        Should return True for valid public_keys
        """
        key1 = """MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwOHPJWD9zc8JPBZj/UtC
dHiY7I4HWt61UG1XRaGvvwUkC/y8P5Kk6dRnf3yMTBHQoisT2vU2ODWVaU5elndk
hiKiWdhufp1d86FWGYz/i+VOmdoV+0zoyPzk+vTEG8bpiY7/UcDYY0CsrRmaMei1
15xZwQpSMpayqMjemvwGDyhy2B3Yize4yaxyLFG53wMrHEczzsYz8FuRfuKUleE/
6jFc3uXZET4LJ7S76n1XU+bE+mhhoZ+tVERgaVH38l0SZljBITwHeqQ9WQckkmDf
bRHBG7TQm+Afnx0s5E2bGIT5jB5cj9YaX6BqZSeodpafQjpXEJg6uufxF1Ni3Btv
4wIDAQAB
"""
        key2 = """MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyibGC058iXS8cscsHdPL
CgVrFx/t6WcXiwUkylerKZO4zvTA/N4CEJwdySCdyHs6AMmbcnUN1/kijZer4xAR
bIa+mO+NuDh33K4qRyIPx8iR/qZxgt0psnooUZV22Ye0dflPXp9PlS0LnyCQjang
Iim/iquKkXdCwCmPeSaXHQttfW4cNVbq0wvg8HHeNYlvTvxbRq0/CVImGwx2jROY
hHH96hAnRfeiMAc6zCxBMNuR1dIp/7XheWc/lN3fCK9SMul7PWUvydtdv6uThScA
0bxsP/w2msnuZyZjWmMm96Kg0SVwaFzLxCKkLzifbprvyC7yDAlW2yjjUROhGCOO
swIDAQAB
"""
        key3 = """MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA6XQzbTUWUxUkBitjc+89
CvvSD4G0apg/qACy9o8Z20UpZlnl07h7U2VaoyiC/i5eVEQEKne4T3vZtuTp5AIn
beIzD5GirXJRozUzU2nCYwpSJqSJF+EUQgLdpa0XONY2MhJo5/h4/TPhF/4GaeIE
VUP5p+2wOWVN9nkPeFyAC9eeA83Pa642kgsxUbbZvqRX9dJ61iqzA89JeG8g/tmd
T6Nv2p0q5Pe0hScnzH9vWU55U6SKlCeRyJ9nH0DJRse6vC9MiUiqNAQKO2Opn6KK
gu8+ZIyat9qLv9YfWDvs00kgjt/VVuumLELtxe84HUocMQq7TrJiJ3KkpwIVr7q4
UwIDAQAB
"""
        for key in [key1, key2, key3]:
            self.assertTrue(RSA_is_valid(key))

    @mock.patch("pyxform.xls2json.RSA_is_valid")
    def test_RSA_is_called(self, RSA_func_mock):
        """
        Uses the RSA_is_valid function
        """
        md = """
                | survey |        |         |                |                                                         |
                |        | type   | name    | label          | constraint                                              |
                |        | text   | Part_ID | Participant ID | pulldata('ID', 'ParticipantID', 'ParticipantIDValue',.) |
                """
        survey = self.md_to_pyxform_survey(md_raw=md)
        self.assertTrue(RSA_func_mock.called_once_with(None))
