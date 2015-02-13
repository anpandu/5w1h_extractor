import org.apache.commons.lang.StringUtils;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by ananta on 2/13/15.
 */
public class Tokenizer {

    public static String[] getTokens(String _text) {
        String text = _text;
        // bebersih
        text = text.replace(",\"", ", \"");
        text = text.replace("\"-", "\" -");
        // split
        String[] res = text.split(" ");
        // split non-alnum first char of token
        LinkedList<String> rawtokens = new LinkedList(Arrays.asList(res));
        boolean again = true;
        while (again) {
            LinkedList<String> rawtokens2 = new LinkedList();
            for (String rawtoken : rawtokens) {
                if (rawtoken.length()>1) {
                    if (!StringUtils.isAlphanumeric(rawtoken.substring(0,1))) {
                        rawtokens2.add(rawtoken.substring(0,1));
                        rawtokens2.add(rawtoken.substring(1));
                    } else
                        rawtokens2.add(rawtoken);
                } else
                    rawtokens2.add(rawtoken);
            }
            rawtokens = new LinkedList(rawtokens2);
            again = false;
            for (String rawtoken : rawtokens)
                if (rawtoken.length()>1)
                    again = again || !StringUtils.isAlphanumeric(rawtoken.substring(0,1));
        }
        // split non-alnum last char of token
        again = true;
        while (again) {
            LinkedList<String> rawtokens2 = new LinkedList();
            for (String rawtoken : rawtokens) {
                if (rawtoken.length()>1) {
                    if (!StringUtils.isAlphanumeric(rawtoken.substring(rawtoken.length()-1))) {
                        rawtokens2.add(rawtoken.substring(0,rawtoken.length()-1));
                        rawtokens2.add(rawtoken.substring(rawtoken.length()-1));
                    } else
                        rawtokens2.add(rawtoken);
                } else
                    rawtokens2.add(rawtoken);
            }
            rawtokens = new LinkedList(rawtokens2);
            again = false;
            for (String rawtoken : rawtokens)
                if (rawtoken.length()>1)
                    again = again || !StringUtils.isAlphanumeric(rawtoken.substring(rawtoken.length()-1));
        }
        while (rawtokens.contains("")) rawtokens.remove("");
        res = rawtokens.toArray(new String[rawtokens.size()]);
        return res;
    }

    public static String[] getSentences(String _text) {
        // split ". "
        LinkedList<String> res = new LinkedList(Arrays.asList(_text.split("\\.\\s")));
        // split " - "
        LinkedList<String> res2 = new LinkedList();
        for (int i = 0; i < res.size(); i++) {
            String[] temp_arr = res.get(i).split("\\s-\\s");
            for (int j = 0; j < temp_arr.length; j++)
                res2.add(temp_arr[j]);
        }
        // hilangin null
        while (res2.contains("")) res2.remove("");
        // tambah "." di akhir
        for (int i = 0; i < res2.size(); i++) res2.set(i, res2.get(i)+".");
        // hilangin kelebihan "."
        String lastSentence = res2.getLast();
        if (lastSentence.charAt(lastSentence.length()-1)=='.')
            res2.set(res2.size()-1, lastSentence.substring(0, lastSentence.length()-1));
        String[] res3 = res2.toArray(new String[res2.size()]);
        return res3;
    }
}
