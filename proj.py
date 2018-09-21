import sys

C_NAME = 'localhost'
C_PORT = 58000+24

l = len(sys.argv)

if l not in [1,3,5]:
  print('Invalid entry')
  sys.exit()
elif l == 3:
  if sys.argv[1] == '-n':
    C_NAME = sys.argv[2]
  elif sys.argv[1] == '-p':
    C_PORT = sys.argv[2]
  else:
    print('Invalid entry')
    sys.exit()
elif l == 5:
  if sys.argv[1] == '-n' and sys.argv[3] == '-p':
    C_NAME = sys.argv[2]
    C_PORT = sys.argv[4]
  elif sys.argv[1] == '-p' and sys.argv[3] == '-n':
    C_NAME = sys.argv[4]
    C_PORT = sys.argv[2]
  else:
    print('Invalid entry')
    sys.exit()
print(len(sys.argv), "\nC_NAME: ", C_NAME, "\nC_PORT: ", C_PORT)
