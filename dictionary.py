mydic2={'student1':{
    "name":"dilsha",
    "age":23,
    'mark':{
        'maths':128,
        'eng':124


    }
},
'student2':{
    "name":"abey",
    "age":24,
    'mark':{
        'maths':130,
        'eng':126
    }
}
} 
# To print all item
print(mydic2)
# To get student1
print(mydic2['student1'])
# To get student2
print(mydic2.get('student2'))
# To get mark of student1
print(mydic2.get('student1').get('mark'))
# length of dictionary
print(len(mydic2))
# To update mark of student1
mydic2.get('student1').get('mark').update({'eng':150})
print(mydic2['student1'])
# To add 
mydic2=({'student3':{
    "name":"abhi",
    'age':23,
    'mark':{
        'maths':128,
        'eng':124
    }
}})
print(mydic2.get('student3'))
print(mydic2)


