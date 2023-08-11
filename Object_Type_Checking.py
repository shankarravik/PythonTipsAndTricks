
var = 'Class'
match var:
    case str():
        print('str')
    case bool():
        print('bool')
    case float():
        print('float')
    case int():
        print('int')
    case dict():
        print('dict')
    case list():
        print('list')
    case None:
        print('None')
    case _:
        print('Unknown')