import sys 

def str_operation(strn, num):
    a = num * strn
    print(a)

str_operation(sys.argv[1], int(sys.argv[2])) #pour selectionner le premier et deuxieme argument depuis la command line. On cast en int la 2eme valeure
