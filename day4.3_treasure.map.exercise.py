row1=["📀","📀","📀"]
row2=["📀","📀","📀"]
row3=["📀","📀","📀"]
map=[row1,row2,row3]
print(f"    1     2     3\n1{row1}\n2{row2}\n3{row3}")
position=input("enter thw position of your choosen loction in the 3*3 map shown(enter the horizontal no. then the vertical no.): ")
horiz=int(position[0])
vert=int(position[1])
selected_row=map[vert-1]#here we selected the row we wanted
selected_row[horiz-1]="x"#hwere we select the coloum we wanted
print(f"    1     2     3\n1{row1}\n2{row2}\n3{row3}")

#or
map[vert-1][horiz-1]="💰"
print(f"    1     2     3\n1{row1}\n2{row2}\n3{row3}")