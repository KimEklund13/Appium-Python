class ActivityIndicators:

    # Activity Indicators
    _activity_indicator_title_xpath = "//XCUIElementTypeNavigationBar[@name='Activity Indicators']"
    _gray_spinner_xpath = "(//XCUIElementTypeActivityIndicator[@name='In progress'])[1]"
    _gray_label_xpath = "(//XCUIElementTypeOther[@name='GRAY'])[1]"
    _tinted_label_xpath = "(//XCUIElementTypeOther[@name='TINTED'])[1]"
    _tinted_spinner_xpath = "(//XCUIElementTypeActivityIndicator[@name='In progress])[2]"