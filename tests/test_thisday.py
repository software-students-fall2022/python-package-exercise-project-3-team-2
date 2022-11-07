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
    
    def test_connect():
        assert thisday.connect("history")== isinstance(BeautifulSoup), "did not return BeautifulSoup object"
        assert thisday.connect("film-tv")== isinstance(BeautifulSoup), "did not return BeautifulSoup object"
        assert thisday.connect("sport")== isinstance(BeautifulSoup), "did not return BeautifulSoup object"
        assert thisday.connect("music")== isinstance(BeautifulSoup), "did not return BeautifulSoup object"


    def test_get_events():
        assert thisday.get_events(thisday.connect("history"))== isinstance(list), "did not return list of events"
        assert thisday.get_events(thisday.connect("film-tv"))== isinstance(list), "did not return list of events"
        assert thisday.get_events(thisday.connect("sport"))== isinstance(list), "did not return list of events"
        assert thisday.get_events(thisday.connect("music"))== isinstance(list), "did not return list of events"
        assert len(thisday.get_events(thisday.connect("history")))!=0, "list of events is empty"
        assert len(thisday.get_events(thisday.connect("film-tv")))!=0, "list of events is empty"
        assert len(thisday.get_events(thisday.connect("sport")))!=0, "list of events is empty"
        assert len(thisday.get_events(thisday.connect("music")))!=0, "list of events is empty"