from bs4 import BeautifulSoup
from thisday import thisday

class Tests:
    # # test just to make sure that the test file works
    # def test_sanity_check(self):
    #     expected = True
    #     actual = True
    #     assert actual == expected, 'Expected True to equal True'

    ################# run #################
    def test_run_valid(self):
        error_msgs = ['Please use one of the following options: film-tv, history, sport, music', 'Error in getting URL', 'Error getting data from page']
        assert thisday.run(['', "film-tv"]) not in error_msgs,"film-tv doesn't run correctly"
        assert thisday.run(['', "history"]) not in error_msgs,"history doesn't run correctly"
        assert thisday.run(['', "sport"]) not in error_msgs,"sport doesn't run correctly"
        assert thisday.run(['', "music"]) not in error_msgs,"music doesn't run correctly"

    def test_run_invalid(self):
        error_msgs = ['Please use one of the following options: film-tv, history, sport, music', 'Error in getting URL', 'Error getting data from page']
        assert thisday.run(['', "foo"]) in error_msgs,"invalid input doesn't return correct message"
        assert thisday.run(['', "games"]) in error_msgs,"invalid input doesn't return correct message"
        assert thisday.run(['', "two", "three"]) in error_msgs,"invalid input doesn't return correct message"
        assert thisday.run(['', "film"]) in error_msgs,"invalid input doesn't return correct message"

    def test_run_datatype(self):
        assert type(thisday.run(['', 'film-tv'])) == str, 'run output is not a string on valid input'
        assert type(thisday.run(['', 'test'])) == str, 'run output is not a string on invalid input'


    ################# process_input #################
    def test_process_input_valid(self):
        assert thisday.process_input("film-tv")=="film-tv","film-tv doesn't run correctly"
        assert thisday.process_input("history")=="history","history doesn't run correctly"
        assert thisday.process_input("sport")=="sport","sport doesn't run correctly"
        assert thisday.process_input("music")=="music","music doesn't run correctly"
    
    def test_process_input_invalid(self):
        assert thisday.process_input("foo")==0,"other cases doesn't run correctly"
        assert thisday.process_input("F1lm-Tv")==0,"other cases doesn't run correctly"
    
    def test_process_input_datatype(self):
        assert isinstance(thisday.process_input("sport"),str),"Didn't return string type"
        assert isinstance(thisday.process_input("foo"),int),"Didn't return integer type" 
    
    ################# connect #################
    def test_connect_valid(self):
        assert thisday.connect("history")!=0, "is not allowing valid input"
        assert thisday.connect("film-tv")!=0, "is not allowing valid input"
        assert thisday.connect("music")!=0, "is not allowing valid input"
        assert thisday.connect("sport")!=0, "is not allowing valid input"

    def test_connect_invalid(self):
        assert thisday.connect("random-topic")==0, "is allowing invalid input"

    def test_connect_returntype(self):
        assert isinstance(thisday.connect("history"), BeautifulSoup), "did not return BeautifulSoup object"
        assert isinstance(thisday.connect("film-tv"), BeautifulSoup), "did not return BeautifulSoup object"
        assert isinstance(thisday.connect("sport"), BeautifulSoup), "did not return BeautifulSoup object"
        assert isinstance(thisday.connect("music"), BeautifulSoup), "did not return BeautifulSoup object"

    ################# get_events #################
    def test_get_events_valid(self):
        assert thisday.get_events(thisday.connect("history"))!=0, "is not taking valid input"

    def test_get_events_invalid(self):
        assert thisday.get_events("random-input")==0, "is taking invalid input"

    def test_get_events_returntype(self):
        assert isinstance(thisday.get_events(thisday.connect("history")), list), "did not return list of events"
        assert isinstance(thisday.get_events(thisday.connect("film-tv")), list), "did not return list of events"
        assert isinstance(thisday.get_events(thisday.connect("sport")), list), "did not return list of events"
        assert isinstance(thisday.get_events(thisday.connect("music")), list), "did not return list of events"

    def test_get_events_listcontent(self):   
        assert len(thisday.get_events(thisday.connect("history")))!=0, "list of events is empty"
        assert len(thisday.get_events(thisday.connect("film-tv")))!=0, "list of events is empty"
        assert len(thisday.get_events(thisday.connect("sport")))!=0, "list of events is empty"
        assert len(thisday.get_events(thisday.connect("music")))!=0, "list of events is empty"

    ################# show #################
    def test_show_valid(self):
        assert thisday.show(['one', 'two', 'three'])=='one\ntwo\nthree', "output is formatted incorrectly with strings"
        assert thisday.show([1, 2, 3])=='1\n2\n3', "output is formatted incorrectly with integers"

    def test_show_invalid(self):
        assert thisday.show('one')==0, "given non-list input should return 0"
        assert thisday.show({'key1':'value1', 'key2':'value2'})==0, "given non-list input should return 0"
        assert thisday.show({1, 2, 3})==0, "given non-list input should return 0"

    def test_show_datatype(self):
        assert type(thisday.show(['on', 'this', 'day'])) == str
        assert type(thisday.show([1, 2, 3])) == str