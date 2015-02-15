/**
 * Created by ananta on 2/13/15.
 */

import static org.junit.Assert.*;
import org.junit.Test;

public class TestTokenizer {

    @Test
    public void testgetTokens() {
        String sentence1 = "hello world";
        String sentence2 = "hello world ";
        String sentence3 = "Hello world, my name is Alice (123).";
//        System.out.println(Tokenizer.getTokens(sentence3));
        assertArrayEquals(Tokenizer.getTokens(sentence1), new String[] {"hello", "world"});
        assertArrayEquals(Tokenizer.getTokens(sentence2), new String[] {"hello", "world"});
        assertArrayEquals(Tokenizer.getTokens(sentence3), new String[] {"Hello", "world", ",", "my", "name", "is", "Alice", "(", "123.0", ")", "."});
    }

    @Test
    public void testgetSentences() {
        String sentence1 = "Forum Indonesia untuk Transparansi Anggaran (Fitra) telah menduga PT Ghalia Indonesia Printing tak akan berhasil menyelesaikan tender naskah ujian nasional. Koordinator Investigasi dan Advokasi Uchok Sky Khadafi menilai proses tender perusahaaan tersebut ganjil. Ghalia menawarkan harga yang lebih tinggi, Rp 22,8 miliar. Namun kementerian Pendidikan dan Kebudayaan tetap memenangkan perusahaan tersebut. PT Ghalia Indonesia Printing adalah perusahaan yang mencetak naskah. Provinsi tersebut yakni Kalimantan Selatan, Kalimantan Timur, Sulawesi Utara, Sulawesi Tengah, Sulawesi Selatan, Sulawesi Tenggara, Bali, Nusa Tenggara Barat, Nusa Tenggara Timur, Gorontalo, dan Sulawesi Barat. Direktur Ghalia, Hamzah Lukman.";
        assertArrayEquals(Tokenizer.getSentences(sentence1), new String[]{"Forum Indonesia untuk Transparansi Anggaran (Fitra) telah menduga PT Ghalia Indonesia Printing tak akan berhasil menyelesaikan tender naskah ujian nasional.", "Koordinator Investigasi dan Advokasi Uchok Sky Khadafi menilai proses tender perusahaaan tersebut ganjil.", "Ghalia menawarkan harga yang lebih tinggi, Rp 22,8 miliar.", "Namun kementerian Pendidikan dan Kebudayaan tetap memenangkan perusahaan tersebut.", "PT Ghalia Indonesia Printing adalah perusahaan yang mencetak naskah.", "Provinsi tersebut yakni Kalimantan Selatan, Kalimantan Timur, Sulawesi Utara, Sulawesi Tengah, Sulawesi Selatan, Sulawesi Tenggara, Bali, Nusa Tenggara Barat, Nusa Tenggara Timur, Gorontalo, dan Sulawesi Barat.", "Direktur Ghalia, Hamzah Lukman."});
    }

    @Test
    public void testremoveNonASCII() {
        String sentence1 = "\u007Fhai\u001F";
        assertTrue(Tokenizer.removeNonASCII(sentence1).equals("hai"));
    }

}
