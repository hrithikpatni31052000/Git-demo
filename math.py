#Add implementation
def add(x,y):
	if y>x:
		return error
	else:
		return x+y

# added subtract implementation
def substract(x,y):
	if y>x:
		return error
	else:
		return x-y

#added multiply header
def multiply(x,y):
	if x==0:
		return error
	else:
		return x*y

#added divide header
def divide(x,y):
	if y==0:
		return Divide_by_0_error
	else:
		return x/y
