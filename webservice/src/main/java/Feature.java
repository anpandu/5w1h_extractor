/**
 * Created by ananta on 2/14/15.
 */
public class Feature {

    private String token;
    private String tokkind;
    private String ne;
    private String cf;
    private String mf;
    private String pf;
    private String idxsentence;
    private String label;
    private Feature bef1;
    private Feature bef2;

    public Feature(String token, String tokkind, String ne, String cf, String mf, String pf, String idxsentence, String label) {
        this.token = token;
        this.tokkind = tokkind;
        this.ne = ne;
        this.cf = cf;
        this.mf = mf;
        this.pf = pf;
        this.idxsentence = idxsentence;
        this.label = label;
    }

    public Feature(Feature _f) {
        this.token = _f.token;
        this.tokkind =_f. tokkind;
        this.ne = _f.ne;
        this.cf = _f.cf;
        this.mf = _f.mf;
        this.pf = _f.pf;
        this.idxsentence = _f.idxsentence;
        this.label = _f.label;
        if (_f.getBef1()!=null) this.setBef1(_f.getBef1());
        if (_f.getBef2()!=null) this.setBef1(_f.getBef2());
    }



    public String getToken() {return token;}
    public String getTokkind() {return tokkind;}
    public String getNe() {return ne;}
    public String getCf() {return cf;}
    public String getMf() {return mf;}
    public String getPf() {return pf;}
    public String getIdxsentence() {return idxsentence;}
    public String getLabel() {return label;}
    public Feature getBef1() {return bef1;}
    public Feature getBef2() {return bef2;}

    public void setToken(String token) {this.token = token;}
    public void setTokkind(String tokkind) {this.tokkind = tokkind;}
    public void setNe(String ne) {this.ne = ne;}
    public void setCf(String cf) {this.cf = cf;}
    public void setMf(String mf) {this.mf = mf;}
    public void setPf(String pf) {this.pf = pf;}
    public void setIdxsentence(String idxsentence) {this.idxsentence = idxsentence;}
    public void setLabel(String label) {this.label = label;}
    public void setBef1(Feature bef1) {this.bef1 = new Feature(bef1);}
    public void setBef2(Feature bef2) {this.bef2 = new Feature(bef2);}

    public String toCSVString0() {
        String res = "" +
                "'" + token + "'," +
                "'" + tokkind + "'," +
                "'" + ne + "'," +
                "'" + cf + "'," +
                "'" + mf + "'," +
                "'" + pf + "'," +
                "'" + idxsentence + "'," +
                "'" + label + "'";
        return res;
    }

    public String toCSVString() {
        String res = "" +
                "'" + token + "'," +
                "'" + tokkind + "'," +
                "'" + ne + "'," +
                "'" + cf + "'," +
                "'" + mf + "'," +
                "'" + pf + "'," +
                "'" + idxsentence + "'," +
                "'" + label + "'";
        if (bef1 != null) res = res + "\t|\t" + bef1.toCSVString0();
        if (bef2 != null) res = res + "\t|\t" + bef2.toCSVString0();
        return res;
    }
}
