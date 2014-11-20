from module.tokenizer import Tokenizer 

class TestTokenizer:

    @classmethod
    def setup_class(self):
        self.paragraph1 = 'Forum Indonesia untuk Transparansi Anggaran (Fitra) telah menduga PT Ghalia Indonesia Printing tak akan berhasil menyelesaikan tender naskah ujian nasional. Koordinator Investigasi dan Advokasi Uchok Sky Khadafi menilai proses tender perusahaaan tersebut ganjil. Ghalia menawarkan harga yang lebih tinggi, Rp 22,8 miliar. Namun kementerian Pendidikan dan Kebudayaan tetap memenangkan perusahaan tersebut. PT Ghalia Indonesia Printing adalah perusahaan yang mencetak naskah. Provinsi tersebut yakni Kalimantan Selatan, Kalimantan Timur, Sulawesi Utara, Sulawesi Tengah, Sulawesi Selatan, Sulawesi Tenggara, Bali, Nusa Tenggara Barat, Nusa Tenggara Timur, Gorontalo, dan Sulawesi Barat. Direktur Ghalia, Hamzah Lukman.'

    def test_getTokens(self):
    	sentence1 = "hello world"
    	sentence2 = "hello world "
    	sentence3 = "Hello world, my name is Alice (123)."
        assert Tokenizer.getTokens(sentence1) == ['hello', 'world']
        assert Tokenizer.getTokens(sentence2) == ['hello', 'world']
        assert Tokenizer.getTokens(sentence3) == ['Hello', 'world', ',', 'my', 'name', 'is', 'Alice', '(', '123', ')', '.']

    def test_getTerms(self):
    	pterms = ['Forum Indonesia', 'untuk', 'Transparansi Anggaran', '(', 'Fitra', ')', 'telah', 'menduga', 'PT Ghalia Indonesia Printing', 'tak', 'akan', 'berhasil', 'menyelesaikan', 'tender', 'naskah', 'ujian', 'nasional', '.', 'Koordinator Investigasi', 'dan', 'Advokasi Uchok Sky Khadafi', 'menilai', 'proses', 'tender', 'perusahaaan', 'tersebut', 'ganjil', '.', 'Ghalia', 'menawarkan', 'harga', 'yang', 'lebih', 'tinggi', ',', 'Rp', '22,8', 'miliar', '.', 'Namun', 'kementerian', 'Pendidikan', 'dan', 'Kebudayaan', 'tetap', 'memenangkan', 'perusahaan', 'tersebut', '.', 'PT Ghalia Indonesia Printing', 'adalah', 'perusahaan', 'yang', 'mencetak', 'naskah', '.', 'Provinsi', 'tersebut', 'yakni', 'Kalimantan Selatan', ',', 'Kalimantan Timur', ',', 'Sulawesi Utara', ',', 'Sulawesi Tengah', ',', 'Sulawesi Selatan', ',', 'Sulawesi Tenggara', ',', 'Bali', ',', 'Nusa Tenggara Barat', ',', 'Nusa Tenggara Timur', ',', 'Gorontalo', ',', 'dan', 'Sulawesi Barat', '.', 'Direktur Ghalia', ',', 'Hamzah Lukman', '.']
        assert Tokenizer.getTerms(self.paragraph1) == pterms

    def test_getSentences(self):
    	psentences = ['Forum Indonesia untuk Transparansi Anggaran (Fitra) telah menduga PT Ghalia Indonesia Printing tak akan berhasil menyelesaikan tender naskah ujian nasional', 'Koordinator Investigasi dan Advokasi Uchok Sky Khadafi menilai proses tender perusahaaan tersebut ganjil', 'Ghalia menawarkan harga yang lebih tinggi, Rp 22,8 miliar', 'Namun kementerian Pendidikan dan Kebudayaan tetap memenangkan perusahaan tersebut', 'PT Ghalia Indonesia Printing adalah perusahaan yang mencetak naskah', 'Provinsi tersebut yakni Kalimantan Selatan, Kalimantan Timur, Sulawesi Utara, Sulawesi Tengah, Sulawesi Selatan, Sulawesi Tenggara, Bali, Nusa Tenggara Barat, Nusa Tenggara Timur, Gorontalo, dan Sulawesi Barat', 'Direktur Ghalia, Hamzah Lukman']
        assert Tokenizer.getSentences(self.paragraph1) == psentences

    def test_removeNonAscii(self):
    	sentence1 = u"\u007Fhai\u001F"
        assert Tokenizer.removeNonAscii(sentence1) == "hai"