strName = "Nguyen Xuan Tien"
print(strName)
dictStudents = {
  	"1" : {
	    "name" : "Nguyen Van A",
	    "age" : 25,
	    "dept":"Vietel"
  		},
  	"2" : {
	    "name" : "Nguyen Van B",
	    "age" : 25,
	    "dept":"Vietel"
  		},
  	"3" : {
	    "name" : "Nguyen Van C",
	    "age" : 25,
	    "dept":"Vietel",
	    },
   	"4" : {
	    "name" : "Nguyen Van D",
	    "age" : 25,
	    "dept":"Vietel",
	    },
   	"5" : {
	    "name" : "Nguyen Van E",
	    "age" : 25,
	    "dept":"Vietel",
	    }
}

print(dictStudents["1"])

for x in dictStudents:
	print("-----------------")
	print("Name: " + dictStudents[x]['name'])
	print("Age : " + str(dictStudents[x]['age']))
	print("Dept: " + dictStudents[x]['dept'])

