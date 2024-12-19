import Testcase2

def test_case_2():
    dr = Testcase2.Singleton() 
    assert Testcase2.Home_page.get_page_home(dr)
    assert Testcase2.Home_page.get_menu(dr)
    assert Testcase2.Games_page.get_scroll(dr)
    assert Testcase2.Games_page.get_steam_lunux(dr)

    assert Testcase2.Games_page.get_LAN(dr)
    assert Testcase2.Games_page.get_action(dr)
    
    Data_game_in_list = Testcase2.Games_page.get_data_first_game(dr)

    assert Testcase2.Games_page.get_page_first_game(dr)

    Data_game_in_page = Testcase2.First_game_page.get_data_first_game_in_page(dr)

    assert Data_game_in_list == Data_game_in_page
    dr.close_driver()
