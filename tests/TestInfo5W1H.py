from module.Info5W1H import Info5W1H

class TestInfo5W1H:

    @classmethod
    def setup_class(self):
        self.text = "Mama, just killed a man, Put a gun against his head, Pulled my trigger, now he's dead. Mama, life had just begun, but now I've gone and thrown it all away."
        self.what = ""
        self.who = ""
        self.when = ""
        self.where = ""
        self.why = ""
        self.how = ""

    def test_init(self):
        info = Info5W1H(self.what, self.who, self.when, self.where, self.why, self.how, self.text)
        assert info.text == "Mama, just killed a man, Put a gun against his head, Pulled my trigger, now he's dead. Mama, life had just begun, but now I've gone and thrown it all away."
    	assert info.sentences == ["Mama, just killed a man, Put a gun against his head, Pulled my trigger, now he's dead", "Mama, life had just begun, but now I've gone and thrown it all away"]
    	assert info.tokenized_sentences == [["Mama", ",", "just", "killed", "a", "man", ",", "Put", "a", "gun", "against", "his", "head", ",", "Pulled", "my", "trigger", ",", "now", "he's", "dead"], ["Mama", ",", "life", "had", "just", "begun", ",", "but", "now", "I've", "gone", "and", "thrown", "it", "all", "away"]]
