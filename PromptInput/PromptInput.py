import argparse,sys
class PromptInput(argparse.ArgumentParser):
	def add_argument(self, *args, prompt=True, secure=False, count = 0, required = False,**kwargs):
		print(sys.argv)
		if(count>0):
			if(required): # Need to do anything if the argument is req otherwise lib can itself add the default value.
				if(len(sys.argv) <= count):
					print("hi1")
					sys.argv.insert(count,input(kwargs['help']))
				elif(sys.argv[count]==''):
					sys.argv.pop(count)
					# print("hi" )
					sys.argv.insert(count,input(kwargs['help']))
			else:
				if(len(sys.argv) <= count):
					sys.argv.insert(count,str(kwargs['default']))
				elif(sys.argv[count]==''):
					sys.argv.pop(count)
					print("hi")
					sys.argv.insert(count,str(kwargs['default']))

		super().add_argument(*args,**kwargs)


# parser = PromptInput()

# # # count is passed with every argument to specify the position of a particular argument. It is used to 
# # # later prompt the help for the correct input.

# # # required -->  It is only passed if the argument is required and there is no default value present and 
# # # you want the user to input it, if left blank with command
# parser.add_argument(
#         'var1',  type=str, nargs='?',
#         help='Enter var 1',default = 11,count = 1,required = True)


# parser.add_argument(
# 	        'var2',  type=str, nargs='?',
# 	        help='Enter var 2', default = 'b',count = 2,required = False)

# args = parser.parse_args()
# print(type(args.var1))
# print(args.var1,args.var2)