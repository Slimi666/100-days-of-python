print('''                          9$$
                          M$$$>
                          '$$$$&
                           $$$$$B
                           $$$$$$$.
                          :$$$$$$$$k
$$$:                      X$$$$$$$$$N..:dN
9$$$$W                    @$$$$$$$$$$$$$$$>
 R$$$$$$W              'W$$$$$$$$$R```"R$$$N>
  R$$$$$$$$$b.       d$$$$$$$$$$$$>     . ^*$$k
   R$$$$$$$$$$$$u  x$$$$****$$$$$$&    4$$N.'*$$L
    4$$$$$$$$$$$$$$$$"        '"*$$B   '$$$$K.'R$K
     '$$$$$$$$$$$$R         :@NW  `$$x  '#$$$$k `$B
      '$$$$$$$$$$~          X$$$$N  '$N    M$$E  ?$N.uebc
       '$$$$$$$$>            $$$$$$    Rk    '  .W$$$$$$$$&
        M$$$$$$R             '$$$$$$L   #N    x@$$$$$$$$$$$$>
        '$$$$$$~                 $$$$L      d$$$$$$$$$$$$$$$E
         4$$$$$                  9$$$E     W$$$$$$$$$$$$$$$$E
         '$$$$$>                  '#$"  :$$$$$$$$$$$$$$$$$$$
          9$$$$B                        $$$$$$$$$$$$$$$$$$R
          X$$$$$$u                    d$"M$$$$$$$$$$$$$$$R
          "$$$$$$$$u                d$#  '$$$$$$$$$$$$$$"
          X$$$$$$$$$$$e..     ..ud$*"     '$$$$$$$$$$$)..uoe@$$$
          X$$$$$$$$$$$$$$$$$**F"~                 '$$RF"""""~
          9$$$$$$$$$$$F``                         W$&......x:.
         J$$$$$$$$$$"                            9$$$****$$$$*
        '$$**$$$$$$                             W$$
             '$$$$&                    :$>    d$$$$$$:
         :xd@$F"`#$$W:                ##"  d$$$$$$$$$$$$Wu.
    :d@$$$""     xW$$$$$$Wx>         xuW$$$$$$$$$$$$$$$$$$$$$W>
  '$$$*"     .d$$*"     ""#*$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
         xe$$*"          .uoe$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
      :W$$*F         x@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
      '`          x@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$k
                :@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                 "R$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$              :
                   ?$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$E             W$
                   '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F           :$$$
                   '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$E            $$$$
                     `*$$R``#R$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$          :$$$$$
                            so$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$N       :@$$$$$$
                            d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Nu. x$$$$$$$$$
                           '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                           X$$$$$$$$$$$$$"R$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                      .WWW@$$$$$$$$$$$$$E  )$$$$$$$$$$$$*$$$$$$$$$$$$$$$$$$$$$$
                   .W$$$$$$$$$$$$$$$$$$$E  $$$$$$$$$$$$$ #$$$$$$$$$$$$$$$$$$$$$
                  :$$$$$$$$$$$$$$$$$$$$$$::$$$$$$$$$$$$$k 'R$$$$$$$$$$$$$$$$$$R
                 :$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$k: `R$$$$$$$$$$$$$$#
                 "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$k '"R$$$$$$$R"`
                  M$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
                'R$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&
                  `#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$E
                     `#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$R
                             #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*
                                "$$$$$$$$$$$$$$$$$$$$$$$"
                                 '`$$$$$$$$$$$$$$$*F"`
''')
print('''Welcome to Tresure Island
Your mission is to find the treasure''')

direction = input("Left or right?\n").lower()

if direction == "left":
    transport = input("Przeżyłeś. Swim or boat?\n").lower()
    if transport == "boat":
        doors = input("Trafiasz do domu. Które drzwi? Red, yellow, blue?\n").lower()
        if doors == "red":
            print("Spaliłeś się. Game over")
        elif doors == "blue":
            print("Napadł cię szatan. Game over")
        else:
            print("Znalazłeś księżniczkę. Wygrałeś. W teorii.")

    else:
        print("Zjadły cię pływające bestie. Game over")

else:
    print("Zjadły cię bestie. Game over")