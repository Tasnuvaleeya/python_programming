while True:
    try:
        number = int(input("Please Enter Your Fav Number\n"))
        print(18/number)
        break
    except ValueError:
        print("Make Sure You Just Enter a Number!")
    except ZeroDivisionError:
        print("Don't pick 0 as number")
    except:
        break
    finally:
        print("Finally executed no matter what exception may raise")
