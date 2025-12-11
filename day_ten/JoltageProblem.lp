\* The_joltage_problem *\
Minimize
Total_button_pushes: Butn_BUTTON_0 + Butn_BUTTON_1 + Butn_BUTTON_2
 + Butn_BUTTON_3 + Butn_BUTTON_4 + Butn_BUTTON_5
Subject To
Joltage_value_0:_34: Butn_BUTTON_0 + Butn_BUTTON_2 + Butn_BUTTON_3 = 34
Joltage_value_1:_34: Butn_BUTTON_1 + Butn_BUTTON_3 + Butn_BUTTON_4 = 34
Joltage_value_2:_38: Butn_BUTTON_1 + Butn_BUTTON_2 + Butn_BUTTON_5 = 38
Joltage_value_3:_32: Butn_BUTTON_3 + Butn_BUTTON_5 = 32
Bounds
 0 <= Butn_BUTTON_0
 0 <= Butn_BUTTON_1
 0 <= Butn_BUTTON_2
 0 <= Butn_BUTTON_3
 0 <= Butn_BUTTON_4
 0 <= Butn_BUTTON_5
Generals
Butn_BUTTON_0
Butn_BUTTON_1
Butn_BUTTON_2
Butn_BUTTON_3
Butn_BUTTON_4
Butn_BUTTON_5
End
