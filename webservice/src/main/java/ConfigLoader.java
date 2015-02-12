/**
 * Created by ananta on 2/12/15.
 */

import org.apache.commons.configuration.CompositeConfiguration;
import org.apache.commons.configuration.Configuration;
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;

import java.io.File;

public class ConfigLoader {

    public final static CompositeConfiguration config = new CompositeConfiguration();
    public static int latestIdx = 0;

    static {
        try {
            config.addConfiguration(new PropertiesConfiguration(new File("config/default.config")));
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static Configuration getConfig() throws ConfigurationException {
        return config.getConfiguration(latestIdx);
    }

    public static void loadProperties(String _path) throws ConfigurationException {
        ConfigLoader.latestIdx += 1;
        config.addConfiguration(new PropertiesConfiguration(new File(_path)));
    }
}