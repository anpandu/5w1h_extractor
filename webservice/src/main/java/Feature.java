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

    public Feature(String token, String tokkind, String ne, String cf, String mf, String pf, String idxsentence) {
        this.token = token;
        this.tokkind = tokkind;
        this.ne = ne;
        this.cf = cf;
        this.mf = mf;
        this.pf = pf;
        this.idxsentence = idxsentence;
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public String getTokkind() {
        return tokkind;
    }

    public void setTokkind(String tokkind) {
        this.tokkind = tokkind;
    }

    public String getNe() {
        return ne;
    }

    public void setNe(String ne) {
        this.ne = ne;
    }

    public String getCf() {
        return cf;
    }

    public void setCf(String cf) {
        this.cf = cf;
    }

    public String getMf() {
        return mf;
    }

    public void setMf(String mf) {
        this.mf = mf;
    }

    public String getPf() {
        return pf;
    }

    public void setPf(String pf) {
        this.pf = pf;
    }

    public String getIdxsentence() {
        return idxsentence;
    }

    public void setIdxsentence(String idxsentence) {
        this.idxsentence = idxsentence;
    }

    @Override
    public String toString() {
        return "Feature{" +
                "token='" + token + '\'' +
                ", tokkind='" + tokkind + '\'' +
                ", ne='" + ne + '\'' +
                ", cf='" + cf + '\'' +
                ", mf='" + mf + '\'' +
                ", pf='" + pf + '\'' +
                ", idxsentence='" + idxsentence + '\'' +
                '}';
    }
}
