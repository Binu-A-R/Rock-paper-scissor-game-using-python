import random


def sys(score_s, score_u):

    s = random.randrange(1, 4)
    str_r = str(s)
    if s == 1:
        print("system's choice: Rock")
    elif s == 2:
        print("system's choice: paper")
    else:
        print("system's choice: scissor")

    #   user
    user = input("enter your choice: 1.Rock 2.paper 3.scissor")

    if user.isdigit():
        if user <= "3" and user != "0":
            if user == str_r:
                sys(score_s, score_u)

            else:
                for i in str_r:
                    for j in user:

                        if (i == "1" and j == "2") or (i == "2" and j == "3") or (i == "3" and j == "1"):
                            score_u += 1

                        elif (i == "1" and j == "3") or (i == "2" and j == "1") or (i == "3" and j == "2"):
                            score_s += 1

                occur_s = int(score_s)
                u_occur = int(score_u)

                while occur_s < 11 and u_occur < 11:
                    print("system win count:", score_s)
                    print("user win count :", score_u)
                    print("")
                    sys(score_s, score_u)

                if score_s == 11:
                    print("sys winner")

                elif score_u == 11:
                    print("user is winner")
                    print("")

        else:
            print("invalid")
            sys(score_s, score_u)

    else:
        print("invalid")
        sys(score_s, score_u)

    cont = input("do you want to play again?[y/n]:  ")
    if cont == 'y' or cont == 'Y':
        sys(0, 0)

    elif cont == 'n' or cont == 'N':
        print("exit")
        exit()
    else:
        print("invalid choice")


sys(0, 0)
