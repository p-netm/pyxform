from pyxform.utils import is_rsa_public_key_valid
from pyxform.tests_v1.pyxform_test_case import PyxformTestCase
from base64 import b64decode

try:
    from unittest import mock
except ImportError:
    import mock


class RSATest(PyxformTestCase):
    """
    Checks For RSA public key validity in xls2json module
    """

    def test_RSA_with_bad_base64_encodings(self):
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
        self.assertFalse(is_rsa_public_key_valid(key5))

    def test_RSA_with_bad_base64_encodings_non_space_string(self):
        """
        Public_key should be a valid b64 decodable string
        """
        key5 = """MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwOHPJWD9zc8JPBZj/UtCdHiY7I4HWt61UG1XRaGvvwUkC/y8P5Kk6dRnf3yMTBHQoisT2vU2ODWVaU5elndkhiKiWdhufp1d86FWGYz/i+VOmdoV+0zoyPzk+vTEG8bpiY7/UcDYY0CsrRmaMei115xZwQpSMpayqMjemvwGDyhy2B3Yize4yaxyLFG53wMrHEczzsYz8FuRfuKUleE/6jFc3uXZET4LJ7S76n1XU+bE+mhhoZ+tVERgaVH38l0SZljBITwHeqQ9WQckkmDfbRHBG7TQm+Afnx0s5E2bGIT5jB5cj9YaX6BqZSeodpafQjpXEJg6uufxF1Ni3Btv4wIDAQ"""
        self.assertFalse(is_rsa_public_key_valid(key5))

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
            b64decode(key6)
        except:
            self.fail()
        self.assertFalse(is_rsa_public_key_valid(key6))

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
        self.assertTrue(is_rsa_public_key_valid(key1))

    @mock.patch("pyxform.utils.is_rsa_public_key_valid")
    def test_RSA_is_called(self, RSA_func_mock):
        """
        Uses the RSA_is_valid function
        """
        md = """
                | survey |        |         |                |                                                         |
                |        | type   | name    | label          | constraint                                              |
                |        | text   | Part_ID | Participant ID | pulldata('ID', 'ParticipantID', 'ParticipantIDValue',.) |
                """
        self.md_to_pyxform_survey(md_raw=md)
        self.assertTrue(RSA_func_mock.called_once_with(None))
