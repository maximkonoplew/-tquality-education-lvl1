import Testcase1

def test_case_1():
    dr = Testcase1.Singleton()
    assert Testcase1.Home_page.get_page_home(dr)
    assert Testcase1.Home_page.get_about(dr)
    assert Testcase1.Player_page.player_comparison(dr)
    assert Testcase1.Player_page.get_back_page_home(dr)
    dr.close_driver()


