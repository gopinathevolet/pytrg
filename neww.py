
import gc

a=10
id_=id(a)
a=20
b=id(a)

def objects_by_id(id_):
    for obj in gc.get_objects():
        if id(obj) == id_:
			c=id(obj)
			print(c)
            return obj
    raise Exception("No found")
	