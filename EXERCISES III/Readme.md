stack=["Lecture A", "Lecture B", "Lecture C"]
stack.append("LectureA")
stack.append("LectureB")
stack.append("LectureC")
stack.pop()
stack.pop()
print("Top element is:", stack[-1])
print("Top element is:", stack[-1])
stack = []
stack.append("StepA")
stack.append("StepB")
stack.append("StepC")

stack.pop()
stack.pop()
stack.pop()
stack = []
stack.extend(["X", "Y", "Z"])
stack.pop()
stack.pop()
stack.append("w")

append(x)	=Adds item x to the top of the stack
pop()	=Removes and returns the top item
extend([...])=	Adds multiple items at once
stack[-1]	Accesses the top item without removing it
