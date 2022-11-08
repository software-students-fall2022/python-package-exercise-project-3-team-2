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

    def test_process_input(self):
        assert thisday.process_input("film-tv")=="film-tv","film-tv doesn't run correctly"
        assert thisday.process_input("history")=="history","history doesn't run correctly"
        assert thisday.process_input("sport")=="sport","sport doesn't run correctly"
        assert thisday.process_input("music")=="music","music doesn't run correctly"
        assert thisday.process_input("foo")==0,"other cases doesn't run correctly"
    
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