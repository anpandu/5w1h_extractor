import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.classifiers.bayes.NaiveBayes;
import weka.classifiers.meta.FilteredClassifier;
import weka.core.Attribute;
import weka.core.FastVector;
import weka.core.Instance;
import weka.core.Instances;

import java.io.BufferedReader;
import java.io.FileReader;

/**
 * Created by ananta on 2/14/15.
 */
public class InfoClassifier {

    String scls1;
    String sdataset;
    String sheader;
    Classifier cls;
    Instances header;
    Instances dataset;

    public InfoClassifier() throws Exception {
//        scls1 = "classifier/ibk_smote_J_s2wv.model";
        scls1 = "classifier/ibk_smote_A_s2wv.model";
        scls1 = "classifier/naivebayes_smote/ta_smote_a.model";
//        sdataset = "classifier/J3.arff";
        sheader = "classifier/A3.arff";
        sdataset = "classifier/dataset/ta_smote_a.arff";
//        sdataset = "classifier/dataset/ta_smote_a+b+c+d+e+f+g+h+i+j.arff";
//        sdataset = "classifier/dataset/taz.arff";
        cls = (Classifier) weka.core.SerializationHelper.read(scls1);

        header = new Instances(new BufferedReader(new FileReader(sheader)));
//        header.setClassIndex(dataset.numAttributes() - 1);
        dataset = new Instances(new BufferedReader(new FileReader(sdataset)));
        dataset.setClassIndex(dataset.numAttributes() - 1);
    }

    public Instance createInstance (Instances _header, Instances _dataset, String[] _attr) {
        Instance inst = _dataset.instance(0);
        for (int i = 0; i < _attr.length; i++)
            inst.setValue(i, _attr[i]);
        inst.setDataset(_header);
        return inst;
    }

    public String getLabel(Feature _f) throws Exception {
//        Instance ie = this.createInstance(dataset,
//                new String[]{ _f.getToken(),
//                        _f.getCf(),
//                        _f.getPf(),
//                        _f.getBef1().getLabel(),
//                        _f.getBef1().getPf(),
//                        _f.getBef1().getToken(),
//                        _f.getBef2().getLabel(),
//                        _f.getBef2().getCf(),
//                        _f.getBef2().getPf(),
//                        _f.getBef2().getToken()
//                }
//        );
        Instance ie = this.createInstance(dataset, dataset,
                new String[]{ _f.getToken()}
        );
        double value = cls.classifyInstance(ie);
        String prediction = dataset.classAttribute().value((int)value);
//        System.out.println("The predicted value of instance " + Integer.toString(0) + "\t: " + value + "\t: " + prediction);
        return prediction;
    }
}
