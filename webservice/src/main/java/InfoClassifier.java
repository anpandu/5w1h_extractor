import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.classifiers.bayes.NaiveBayes;
import weka.classifiers.meta.FilteredClassifier;
import weka.core.Attribute;
import weka.core.FastVector;
import weka.core.Instance;
import weka.core.Instances;
import weka.filters.Filter;
import weka.filters.MultiFilter;

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
    Filter fil;

    public InfoClassifier() throws Exception {
//        scls1 = "classifier/ibk_smote_A_s2wv.model";
//        scls1 = "classifier/ibk_smote_J_s2wv.model";
//        scls1 = "classifier/naivebayes_smote/ta_smote_a.model";


//        sheader = "classifier/A4.arff";
        sdataset = "classifier/dataset2/ta_smote_a+b+c+d.arff";
        scls1 = "classifier/exp_model2/ibk_smote/ta_a+b+c+d.model";

        // success
//        sdataset = "classifier/dataset/ta_smote_a.arff";
//        scls1 = "classifier/nb_smote_A_s2wv.model";


        cls = (Classifier) weka.core.SerializationHelper.read(scls1);

//        fil = new MultiFilter();

//        header = new Instances(new BufferedReader(new FileReader(sheader)));
//        header.setClassIndex(dataset.numAttributes() - 1);
        dataset = new Instances(new BufferedReader(new FileReader(sdataset)));
        dataset.setClassIndex(dataset.numAttributes() - 1);
    }

//    public Instance createI (Instances _header, Instances _dataset, String[] _attr) {
//
//        FastVector fvbef1class = new FastVector(14);
//        fvbef1class.addElement("BEGIN");
//        fvbef1class.addElement("beg_what");
//        fvbef1class.addElement("in_what");
//        fvbef1class.addElement("beg_who");
//        fvbef1class.addElement("in_who");
//        fvbef1class.addElement("beg_when");
//        fvbef1class.addElement("in_when");
//        fvbef1class.addElement("beg_where");
//        fvbef1class.addElement("in_where");
//        fvbef1class.addElement("beg_why");
//        fvbef1class.addElement("in_why");
//        fvbef1class.addElement("beg_how");
//        fvbef1class.addElement("in_how");
//        fvbef1class.addElement("other");
//        Attribute Attribute1 = new Attribute("bef1class", fvbef1class);
//
//        Attribute Attribute2 = new Attribute("idxsentence");
//
//        // Declare the class attribute along with its values
//        FastVector fvClassVal = new FastVector(13);
//        fvClassVal.addElement("beg_what");
//        fvClassVal.addElement("in_what");
//        fvClassVal.addElement("beg_who");
//        fvClassVal.addElement("in_who");
//        fvClassVal.addElement("beg_when");
//        fvClassVal.addElement("in_when");
//        fvClassVal.addElement("beg_where");
//        fvClassVal.addElement("in_where");
//        fvClassVal.addElement("beg_why");
//        fvClassVal.addElement("in_why");
//        fvClassVal.addElement("beg_how");
//        fvClassVal.addElement("in_how");
//        fvClassVal.addElement("other");
//        Attribute ClassAttribute = new Attribute("class", fvClassVal);
//
//        // Declare the feature vector
//        FastVector fvWekaAttributes = new FastVector(4);
//        fvWekaAttributes.addElement(Attribute1);
//        fvWekaAttributes.addElement(Attribute2);
////        fvWekaAttributes.addElement(Attribute3);
//        fvWekaAttributes.addElement(ClassAttribute);
//
//        // Create an empty training set
//        Instances isTrainingSet = new Instances("Rel", fvWekaAttributes, 10);
//        // Set class index
//        isTrainingSet.setClassIndex(3);
//
//        // Create the instance
//        Instance inst = new Instance(3);
////        System.out.println("");
////        System.out.println(fvWekaAttributes);
////        System.out.println("");
//        inst.setDataset(isTrainingSet);
//        inst.setValue(0, _attr[0]);
//        inst.setValue(1, Integer.valueOf(_attr[1]));
//        inst.setValue(2, _attr[2]);
//        return inst;
//    }

    public Instance createInstance (Instances _header, Instances _dataset, String[] _attr) {
        Instance inst = _dataset.instance(0);
//        System.out.println("+"+_attr[4]+"+");
//        System.out.println("|"+_attr[0]+"|");
//        System.out.println("|"+_attr[1]+"|");
//        System.out.println("|"+_attr[2]+"|");
//        System.out.println("|"+_attr[3]+"|");
//        System.out.println("");
        inst.setDataset(_header);
        inst.setValue(0, Integer.valueOf(_attr[0]));
        inst.setValue(1, _attr[1]);
        inst.setValue(2, _attr[2]);
        inst.setValue(3, _attr[3]);
        return inst;
    }

    public String getLabel(Feature _f) throws Exception {
//        Instance ie = this.createInstance(dataset, dataset,
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
                new String[]{
                        _f.getIdxsentence(),
                        _f.getNe(),
                        _f.getBef1().getLabel(),
                        _f.getBef1().getPf(),_f.getToken()
                }
        );
//        Instance ie = this.createInstance(dataset, dataset,
//                new String[]{ _f.getToken()}
//        );
        double value = cls.classifyInstance(ie);
        String prediction = dataset.classAttribute().value((int)value);
//        System.out.println("The predicted value of instance " + Integer.toString(0) + "\t: " + value + "\t: " + prediction);
        return prediction;
    }
}
