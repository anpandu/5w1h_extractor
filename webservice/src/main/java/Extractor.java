import org.apache.commons.lang.StringUtils;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.LinkedList;


/**
 * Created by ananta on 2/13/15.
 */
public class Extractor {

    public static Map<String, String> getInfo(String _news) {
        Map res = new HashMap<>();

        String sentence = StringUtils.join(Tokenizer.getTokens(_news), " ");
        System.out.println(sentence);
        LinkedList<Feature> fs = Extractor.getFeatures(sentence);

        res.put("news", _news);
        res.put("what", "");
        res.put("who", "");
        res.put("when", "");
        res.put("where", "");
        res.put("why", "");
        res.put("how", "");

        System.out.println("");
        return res;
    }

    public static LinkedList<Feature> getFeatures (String _sentence) {
        LinkedList<Feature> res = new LinkedList();
        IndonesianNETagger inner = new IndonesianNETagger();
        String sentence = _sentence;
        inner.setSentence(sentence);
        inner.extractNamedEntity(sentence);

        ArrayList<String> tokens = inner.getToken();
        ArrayList<String> tokkinds = inner.getTokenKind();
        ArrayList<String> nes = inner.getNE();
        ArrayList<String> cfs = inner.getContextualFeature();
        ArrayList<String> mfs = inner.getMorphologicalFeature();
        ArrayList<String> pfs = inner.getPOSFeature();

        for (int i = 0; i < tokens.size(); i++) {
            String[] item = new String[6];
            item[0] = tokens.get(i);
            item[1] = tokkinds.get(i);
            item[2] = nes.get(i);
            item[3] = cfs.get(i);
            item[4] = mfs.get(i);
            item[5] = pfs.get(i);
            Feature fff = new Feature(item[0], item[1], item[2], item[3], item[4], item[5], "1");
            res.add(fff);
            // System.out.println(fff.toString());
        }
        return res;
    }

}
