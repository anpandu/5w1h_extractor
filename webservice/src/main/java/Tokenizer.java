import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by ananta on 2/13/15.
 */
public class Tokenizer {

    public static LinkedList<String> getSentences(String _text) {
        // split ". "
        LinkedList<String> res = new LinkedList(Arrays.asList(_text.split("\\.\\s")));
        // split " - "
        LinkedList<String> res2 = new LinkedList();
        for (int i = 0; i < res.size(); i++) {
            String[] temp_arr = res.get(i).split("\\s-\\s");
            for (int j = 0; j < temp_arr.length; j++)
                res2.add(temp_arr[j]);
        }
        res2.add("");
        res2.add("");
        res2.add("");
        // hilangin null
        while (res2.contains("")) res2.remove("");
        // tambah "." di akhir
        for (int i = 0; i < res2.size(); i++) res2.set(i, res2.get(i)+".");
        // hilangin kelebihan "."
        String lastSentence = res2.getLast();
        if (lastSentence.charAt(lastSentence.length()-1)=='.')
            res2.set(res2.size()-1, lastSentence.substring(0, lastSentence.length()-1));
        // print
        System.out.println(res2.size());
        for (int i = 0; i < res2.size(); i++) {
            System.out.println(res2.get(i));
        }
        return res2;
    }
}
