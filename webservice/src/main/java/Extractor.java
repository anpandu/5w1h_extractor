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
        for (Feature f : fs) {System.out.println(f.toCSVString());}

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
        LinkedList<Feature> bef0features = new LinkedList();
        LinkedList<Feature> bef1features = new LinkedList();
        LinkedList<Feature> bef2features = new LinkedList();
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
            Feature fff = new Feature(item[0], item[1], item[2], item[3], item[4], item[5], "1", "BEGIN");
            bef0features.add(fff);
        }
        Feature beginFeature = new Feature("?", "BEGIN", "BEGIN", "?", "?", "?", "0", "BEGIN");
        for (int i = 0; i < bef0features.size(); i++) {
            Feature feature = new Feature(bef0features.get(i));
            if (i<1)
                feature.setBef1(beginFeature);
            else
                feature.setBef1(bef1features.get(i-1));
            // set class/label here!
            bef1features.add(feature);
        }
        for (int i = 0; i < bef0features.size(); i++) {
            Feature feature = new Feature(bef1features.get(i));
            if (i<2)
                feature.setBef2(beginFeature);
            else
                feature.setBef2(bef2features.get(i-2));
            // set class/label here!
            bef2features.add(feature);
        }
        LinkedList<Feature> res = new LinkedList(bef2features);
        return res;
    }

}
