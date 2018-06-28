def echo(*args,**kwargs):
	print(args,kwargs)
	type(args)
echo(1,2,a=5,b=4)
echo('a','b',1,2,a=2,b=5)
echo(a=10,1,2,3)
