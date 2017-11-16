# -*- coding: cp1250 -*-
import easygui
smak = easygui.buttonbox ("Jaki jest twój ulubiony smak lodów?",
                          choices = ['Waniliowe','Czekoladowe','Truskawkowe'])
# -*- coding: cp1250 -*-
easygui.msgbox ("Wybrałeś " + smak)
