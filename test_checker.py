import checker    # The code to test

def test_checkDogs():
    urll = "https://www.gumtree.com/search?featured_filter=false&q=&search_category=dogs&urgent_filter=false&sort=date&search_scope=false&photos_filter=false&search_location=London&tl=&distance=30"
    textToSearch = "poo"
    assert checker.checkDogCount(urll, textToSearch) == 16

def test_sendEmail():
    assert checker.sendEmail("https://www.pets4homes.co.uk/search/?type_id=3&advert_type=1&location=london&distance=30&results=10&sort=creatednew")

def tes_repeat():
    urll = "https://www.pets4homes.co.uk/search/?type_id=3&advert_type=1&location=london&distance=30&results=10&sort=creatednew"
    textToSearch = "poo"
    assert checker.repeatDogCheck(urll, textToSearch) == 16