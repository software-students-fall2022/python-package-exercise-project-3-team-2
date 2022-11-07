from cmath import isinf
from bs4 import BeautifulSoup
import pytest
from thisday import thisday

class Tests:
    # function tests go here
    # 
    # convention is as follows...
    # test_<function name>(self, [<args>])
    # 
    # for example:
    # test_parse_data(self, data)

    # test file outline slides
    # https://github.com/nyu-software-engineering/course-materials/blob/master/slides/software-testing.md
    

    # test just to make sure that the test file works
    def test_sanity_check(self):
        expected = True
        actual = True
        assert actual == expected, 'Expected True to equal True'

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
    
    def test_connect(self):
        assert isinstance(thisday.connect("history"), BeautifulSoup), "did not return BeautifulSoup object"
        assert isinstance(thisday.connect("film-tv"), BeautifulSoup), "did not return BeautifulSoup object"
        assert isinstance(thisday.connect("sport"), BeautifulSoup), "did not return BeautifulSoup object"
        assert isinstance(thisday.connect("music"), BeautifulSoup), "did not return BeautifulSoup object"


    def test_get_events(self):
        assert isinstance(thisday.get_events(thisday.connect("history")), list), "did not return list of events"
        assert isinstance(thisday.get_events(thisday.connect("film-tv")), list), "did not return list of events"
        assert isinstance(thisday.get_events(thisday.connect("sport")), list), "did not return list of events"
        assert isinstance(thisday.get_events(thisday.connect("music")), list), "did not return list of events"
        assert len(thisday.get_events(thisday.connect("history")))!=0, "list of events is empty"
        assert len(thisday.get_events(thisday.connect("film-tv")))!=0, "list of events is empty"
        assert len(thisday.get_events(thisday.connect("sport")))!=0, "list of events is empty"
        assert len(thisday.get_events(thisday.connect("music")))!=0, "list of events is empty"


    def test_show_valid(self):
        assert thisday.show(['one', 'two', 'three'])=='one\ntwo\nthree', "output is formatted incorrectly with strings"
        assert thisday.show([1, 2, 3])=='1\n2\n3', "output is formatted incorrectly with integers"

    def test_show_invalid(self):
        assert thisday.show('one')==0, "given non-list input should return 0"
        assert thisday.show({'key1':'value1', 'key2':'value2'})==0, "given non-list input should return 0"
        assert thisday.show({1, 2, 3})==0, "given non-list input should return 0"

    def test_show_datatype(self):
        assert type(thisday.show(['on', 'this', 'day'])) == list
        assert type(thisday.show([1, 2, 3])) == list