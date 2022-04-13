from validator import validate


if validate("NDR To Excel Project/02-10-2020/IHVN_b8wSBkFN6qj_2_021020_FCT90800071.xml", "NDR To Excel Project/NDR "
                                                                                         "1.6.2.2"):
    print('Valid! :)')
else:
    print('Not valid! :(')


