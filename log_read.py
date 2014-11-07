with open("breeze_logs/CAL_LOG.log") as f:
    lines = f.readlines()
    for line in lines:
    	print float(line.split(" ")[3]) * 1000


'''
x= []
with open("breeze_logs/CAL_LOG.log") as f:
    lines = f.readlines()
    for line in lines:
    	x.append( float(line.split(" ")[3]) * 1000 )
'''