# -*- coding: cp1250 -*-
import easygui
smak = easygui.buttonbox ("Jaki jest tw�j ulubiony smak lod�w?",
                          choices = ['Waniliowe','Czekoladowe','Truskawkowe'])
# -*- coding: cp1250 -*-
easygui.msgbox ("Wybra�e� " + smak)
