/**
 * Created by ananta on 2/12/15.
 */
//import org.apache.commons.configuration.Configuration;
import org.eclipse.jetty.server.handler.AbstractHandler;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.ServletException;
import org.eclipse.jetty.server.Request;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.LinkedList;
import java.util.Map;
import org.json.JSONObject;

/**
 * Created by ananta on 8/15/14.
 */

public class WebserviceHandler extends AbstractHandler
{

    public void handle(String target, Request baseRequest, HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException
    {
        response.setStatus(HttpServletResponse.SC_OK);
        baseRequest.setHandled(true);

        PrintWriter pri = response.getWriter();
        String pathInfo = request.getPathInfo();
        Map<String, String[]> parameterMap = request.getParameterMap();

        System.out.println("webservice success");
        System.out.println(pathInfo);
        System.out.println(parameterMap);

        if (pathInfo.equals("/extract")) {
            Map<String, String> res = null;
            try {
                res = Extractor.getInfo(parameterMap.get("text")[0]);
            } catch (Exception e) {
                e.printStackTrace();
            }
            JSONObject jsonResult = new JSONObject();

            jsonResult.put("news", res.get("news"));
            jsonResult.put("what", "");
            jsonResult.put("who", "");
            jsonResult.put("when", "");
            jsonResult.put("where", "");
            jsonResult.put("why", "");
            jsonResult.put("how", "");

            pri.println(jsonResult.toString());
        }

    }
}
