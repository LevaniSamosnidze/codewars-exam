# 6) Convert Pascal Case string into snake_case (4 ქულა)

# You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

# Examples:
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7 Test"        -->  "app7_test"
# 1                 -->  "1"

def onvert_ascal_ase_string_into_snake(s):
    s = str(s)
    for i in s:
        if i.isupper():
            s1 = s.replace(i, f"_{i.lower()}")

    return s1

print(onvert_ascal_ase_string_into_snake('TestController'))