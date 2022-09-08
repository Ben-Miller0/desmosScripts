from pickle import APPEND

#left(t\left(x_{1}\right)+\left(1-t\right)\left(x_{2}\right),t\left(y_{1}\right)+\left(1-t\right)\left(y_{2}\right)\right)

PointsCount = int(input())

PointListX = ["x_{1}"]
PointListY = ["y_{1}"]

PointListCounter = 1

while PointListCounter <= PointsCount:
    PointListCounter += 1
    PointListX.append("x_{"+str(PointListCounter)+"}")
    PointListY.append("y_{"+str(PointListCounter)+"}")

PointListX[0] = "left(t\left("+PointListX[0]+"}\right)+\left(1-t\right)\left("+PointListX[1]+"\right),t\left("+PointListY[0]+"\right)+\left(1-t\right)\left("+PointListY[1]+"\right)\right)"

PointX = PointListX[0]
PointY = PointListY[0]

print("\left("+PointX+","+PointY+"/right)")

print(PointListX)
print(PointListY)

print(PointListX[0])


github test
#                         ___
#                      .-'   `'.
#                     /         \
#                     |         ;
#                     |         |           ___.--,
#            _.._     |0) = (0) |    _.---'`__.-( (_.
#     __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `""`
#    ( ,.--'`   ',__ /./;   ;, '.__.'`    __
#    _`) )  .---.__.' / |   |\   \__..--""  """--.,_
#   `---' .'.''-._.-'`_./  /\ '.  \ _.--''````'''--._`-.__.'
#         | |  .' _.-' |  |  \  \  '.               `----`
#          \ \/ .'     \  \   '. '-._)
#           \/ /        \  \    `=.__`'-.
#           / /\         `) )    / / `"".`\
#     , _.-'.'\ \        / /    ( (     / /
#      `--'`   ) )    .-'.'      '.'.  | (
#             (/`    ( (`          ) )  '-