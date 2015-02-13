import java.util.HashMap;
import java.util.Map;
import java.util.LinkedList;


/**
 * Created by ananta on 2/13/15.
 */
public class Extractor {

    public static Map<String, String> getInfo(String _news) {
        Map res = new HashMap<>();

        System.out.println(Tokenizer.removeNonASCII("\u007Fhai\u001F"));
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

}
