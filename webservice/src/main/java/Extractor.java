import org.apache.commons.lang.StringUtils;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.LinkedList;


/**
 * Created by ananta on 2/13/15.
 */
public class Extractor {

    public static Map<String, String> getInfo(String _news) throws Exception {
        Map res = new HashMap<>();

        String news = Tokenizer.funcAdaptINANLP(_news);
        news = Tokenizer.funcAdaptINANLP2(news);
        String sentence = StringUtils.join(Tokenizer.getTokens(news), " ");
        sentence = Tokenizer.removeNonASCII(sentence);
        System.out.println(sentence);
        LinkedList<Feature> fs = Extractor.getFeatures(sentence);
        for (Feature f : fs) {System.out.println(f.toCSVString());}

        System.out.println("");

        String[] infos = Extractor.getInfosFromFeatures(fs);

        res.put("news", _news);
        res.put("what", infos[0]);
        res.put("who", infos[1]);
        res.put("when", infos[2]);
        res.put("where", infos[3]);
        res.put("why", infos[4]);
        res.put("how", infos[5]);

        System.out.println("");
        return res;
    }

    public static String[] getInfosFromFeatures (LinkedList<Feature> _fs) {
        String[] infos = new String[6];
        String[] begs = new String[] {"beg_what", "beg_who", "beg_when", "beg_where", "beg_why", "beg_how"};
        String[] ins = new String[] {"in_what", "in_who", "in_when", "in_where", "in_why", "in_how"};
        for (int i = 0; i < infos.length; i++) {
            String info = "";
            boolean begin = false;
            boolean hitother = false;
            for (Feature f : _fs) {
//                System.out.print(f.getToken());
                if (f.getLabel().equals(begs[i])&&!hitother) {
                    begin = true;
                    info += (begin) ? (" " + f.getToken()) : f.getToken();
//                    System.out.print(" begin");
                } else
                if ((f.getLabel().equals(ins[i]))&&(begin)&&(!hitother)) {
                    info += (" " + f.getToken());
//                    System.out.print(" in");
                } else {
                    if (begin) {
                        hitother = true;
//                        System.out.print(" hitother");
                    }
                }
//                System.out.println("");
            }
            infos[i] = info;
        }
        String[] res = infos;
        return res;
    }

    public static LinkedList<Feature> getFeatures (String _sentence) throws Exception {
        LinkedList<Feature> bef0features = new LinkedList();
        LinkedList<Feature> bef1features = new LinkedList();

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
        InfoClassifier ic = new InfoClassifier();

        for (int i = 0; i < bef0features.size(); i++) {
            Feature feature = new Feature(bef0features.get(i));
            if (i<1) {
                feature.setBef1(beginFeature);
                feature.setBef2(beginFeature);
            } else if (i<2) {
                feature.setBef1(beginFeature);
                feature.setBef2(bef1features.get(i-1));
            } else {
                feature.setBef1(bef1features.get(i-1));
                feature.setBef2(bef1features.get(i-2));
            }
            feature.setLabel(ic.getLabel(feature));
            bef1features.add(feature);
        }
        LinkedList<Feature> res = new LinkedList(bef1features);
        return res;
    }

}
