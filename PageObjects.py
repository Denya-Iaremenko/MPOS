
class PageObject(object):

    login_filed = "//UIAApplication[1]/UIAWindow[1]/UIATableCell[1]/UIATextField[1]"
    password_field = "//UIAApplication[1]/UIAWindow[1]/UIATableCell[2]/UIATextField[1]"
    login_btn = "//UIAApplication[1]/UIAWindow[1]/UIAButton[1]"
    login_error = "//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIAScrollView[1]/UIAStaticText[1]"
    login_error_text = "//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIAScrollView[1]/UIAStaticText[2]"
    ok_btn = "//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[1]/UIAButton[1]"
    clear_password_btn = "//UIAApplication[1]/UIAWindow[1]/UIATableCell[1]/UIATextField[2]/UIAButton[1]"
    secure_password_field = "//UIAApplication[1]/UIAWindow[1]/UIATableCell[2]/UIASecureTextField[1]"