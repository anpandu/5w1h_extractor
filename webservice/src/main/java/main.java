/**
 * Created by ananta on 2/12/15.
 */


import java.util.LinkedList;
import org.apache.commons.configuration.Configuration;
import org.apache.commons.configuration.ConfigurationException;
import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.server.Request;
import org.eclipse.jetty.server.handler.AbstractHandler;
import sun.tools.jar.CommandLine;

public class main {

    private static Configuration config = null;

    public static void main(String[] args) {

        try {
            config = ConfigLoader.getConfig();
            startServer(config);
        }
        catch (ConfigurationException e) {
            e.printStackTrace();
            System.exit(1);
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    private static void startServer (Configuration _config) throws Exception {
        int port = Integer.valueOf(_config.getString("server.port"));
        Server server = new Server(port);
        server.setHandler(new WebserviceHandler());
        server.start();
        server.join();
    }
}
