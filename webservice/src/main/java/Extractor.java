import java.util.HashMap;
import java.util.Map;

/**
 * Created by ananta on 2/13/15.
 */
public class Extractor {

    public static Map<String, String>  getInfo(String _news) {
        Map res = new HashMap<>();
        res.put("news", _news);
        res.put("what", "");
        res.put("who", "");
        res.put("when", "");
        res.put("where", "");
        res.put("why", "");
        res.put("how", "");
        return res;
    }

}
