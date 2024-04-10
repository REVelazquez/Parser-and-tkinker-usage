from scanner import Scanner
def main ():
    exam =input('Introduce a boolean valor: ')
    exam=exam.lower()
    s = Scanner(exam)
    tokens = s.scanAll()
    print(tokens)

if __name__ == '__main__':
    main()