from tkinter import*
from tkinter import ttk
import math,random
from tkinter import messagebox,ttk
import pymysql
import os
import time
import tempfile

class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Pay Roll Management System")
        self.root.config(bg="white")
        self.root.geometry("1360x600+0+0")
        
        
        
        title=Label(self.root,text="Employee Pay Roll Management System",font=("times new roman",30,"bold"),bg="green",fg="blue").place(x=0,y=0,relwidth=1)
        btn_emp=Button(self.root,text="All Employees",command=self.employee_frame,font=("times new roman",13),bg="darkgray",fg="black").place(x=1300,y=10,height=30,width=120)
        #==============================================VARIABLES===============================
        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_experience=StringVar()
        self.var_proof_id=StringVar()
        self.var_contact=StringVar()
        self.var_status=StringVar()
       
        
        #=====================================FRAME1============================================
        Frame1=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=60,width=740,height=620) 
        
        title2=Label(Frame1,text="Employee Deatils",font=("times new roman",20,"bold"),bg="black",fg="blue",padx=10,anchor="w").place(x=0,y=0,relwidth=1)

        lbl_code=Label(Frame1,text="Employee code",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=60)
        self.txt_code=Entry(Frame1,textvariable=self.var_emp_code,font=("times new roman",15,"bold"),bg="lightyellow",fg="black")
        self.txt_code.place(x=220,y=65,width=200)
        btn_search=Button(Frame1,text="Search",command=self.search,font=("times new roman",20),bg="darkgray",fg="black").place(x=450,y=65,height=30)
        
        #==================ROW1
        lbl_designation=Label(Frame1,text="Designation",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=120)
        txt_designation=Entry(Frame1,textvariable=self.var_designation,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=160,y=125,width=200)
        
        lbl_dob=Label(Frame1,text="D.O.J",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=400,y=120)
        txt_dob=Entry(Frame1,textvariable=self.var_dob,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=500,y=125,width=200)
        
         #==================ROW2
        lbl_Name=Label(Frame1,text="Name",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=160)
        txt_Name=Entry(Frame1,textvariable=self.var_name,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=160,y=165,width=200)
        
        lbl_doj=Label(Frame1,text="D.O.B",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=400,y=160)
        txt_doj=Entry(Frame1,textvariable=self.var_doj,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=500,y=165)
        
        #==================ROW3    HERE BOX SIZE MISTAKE THERE VIDEO 22:56 EXPERINCE BOX
        lbl_age=Label(Frame1,text="Age",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=200)
        txt_age=Entry(Frame1,textvariable=self.var_age,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=160,y=205,width=200)
        
        lbl_experience=Label(Frame1,text="Experience",font=("times new roman",15),bg="white",fg="black").place(x=400,y=200)
        txt_experience=Entry(Frame1,textvariable=self.var_experience,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=500,y=205)
        
        #==================ROW4
        lbl_gender=Label(Frame1,text="Gender",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=240)
        txt_gender=Entry(Frame1,textvariable=self.var_gender,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=160,y=245,width=200)
        
        lbl_proof=Label(Frame1,text="Proof ID",font=("times new roman",18),bg="white",fg="black").place(x=400,y=240)
        txt_proof=Entry(Frame1,textvariable=self.var_proof_id,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=500,y=245)
        
        
        #==================ROW5
        lbl_email=Label(Frame1,text="Email",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=280)
        txt_email=Entry(Frame1,textvariable=self.var_email,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=160,y=285,width=200)
        
        lbl_contact=Label(Frame1,text="Contact",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=400,y=280)
        txt_contact=Entry(Frame1,textvariable=self.var_contact,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=500,y=285)
        
        #==================ROW6
        lbl_hired=Label(Frame1,text="Hired Location",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=10,y=320)
        txt_hired=Entry(Frame1,textvariable=self.var_hr_location,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=170,y=325,width=200)
        
        lbl_status=Label(Frame1,text="Status",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=400,y=320)
        txt_status=Entry(Frame1,textvariable=self.var_status,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=500,y=325)
     

        #==================ROW6
        lbl_address=Label(Frame1,text="Address",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=10,y=380)
        self.txt_address=Text(Frame1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black")
        self.txt_address.place(x=160,y=385,width=560,height=190)
     
       
      #=======================================VARIABLES======================================
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_t_days=StringVar()
        self.var_absents=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()
        self.var_net_salary=StringVar()
      #=====================================FRAME2============================================
        Frame2=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        Frame2.place(x=760,y=60,width=760,height=310) 
       
        title2=Label(Frame2,text="Employee Salary Deatils",font=("times new roman",20,"bold"),bg="black",fg="blue",padx=10,anchor="w").place(x=0,y=0,relwidth=1)

        
        lbl_month=Label(Frame2,text="Month",font=("times new roman",18),bg="white",fg="black").place(x=10,y=60)
        txt_month=Entry(Frame2,textvariable=self.var_month,font=("times new roman",15),bg="lightyellow",fg="black").place(x=120,y=62,width=100)
        
        lbl_year=Label(Frame2,text="Year",font=("times new roman",18),bg="white",fg="black").place(x=260,y=60)
        txt_year=Entry(Frame2,textvariable=self.var_year,font=("times new roman",15),bg="lightyellow",fg="black").place(x=340,y=62,width=100)
        
        lbl_salary=Label(Frame2,text="Basic Salary",font=("times new roman",18),bg="white",fg="black").place(x=460,y=60)
        txt_salary=Entry(Frame2,textvariable=self.var_salary,font=("times new roman",15),bg="lightyellow",fg="black").place(x=600,y=62,width=100)
        
        #===============================================ROW2=========================================

        lbl_days=Label(Frame2,text="Total Days",font=("times new roman",18),bg="white",fg="black").place(x=10,y=120)
        txt_days=Entry(Frame2,textvariable=self.var_t_days,font=("times new roman",15),bg="lightyellow",fg="black").place(x=160,y=125,width=160)
        
        lbl_absent=Label(Frame2,text="Absent",font=("times new roman",18),bg="white",fg="black").place(x=400,y=120)
        txt_absent=Entry(Frame2,textvariable=self.var_absents,font=("times new roman",15),bg="lightyellow",fg="black").place(x=560,y=125,width=160)
        
        #===============================================ROW3=========================================

        
        lbl_medicals=Label(Frame2,text="Medicals",font=("times new roman",18),bg="white",fg="black").place(x=10,y=160)
        txt_medicals=Entry(Frame2,textvariable=self.var_medical,font=("times new roman",15),bg="lightyellow",fg="black").place(x=160,y=165,width=160)
        
        lbl_pf=Label(Frame2,text="Provident Fund",font=("times new roman",18),bg="white",fg="black").place(x=400,y=160)
        txt_pf=Entry(Frame2,textvariable=self.var_pf,font=("times new roman",15),bg="lightyellow",fg="black").place(x=560,y=165,width=160)
        
         #===============================================ROW4=========================================

        lbl_convence=Label(Frame2,text="Convence",font=("times new roman",18),bg="white",fg="black").place(x=10,y=200)
        txt_convence=Entry(Frame2,textvariable=self.var_convence,font=("times new roman",15),bg="lightyellow",fg="black").place(x=160,y=205,width=160)
        
        lbl_netsalary=Label(Frame2,text="Net Salary",font=("times new roman",18),bg="white",fg="black").place(x=400,y=200)
        txt_netsalary=Entry(Frame2,textvariable=self.var_net_salary,font=("times new roman",15),bg="lightyellow",fg="black").place(x=560,y=205,width=160)
        
        #=============================BUTTONS=========================================
        self.btn_calculate=Button(Frame2,text="Calculate",command=self.calculate,font=("times new roman",20),bg="orange",fg="black")
        self.btn_calculate.place(x=20,y=260,width=130,height=30)
        
        self.btn_save=Button(Frame2,text="Save",command=self.add,font=("times new roman",20),bg="green",fg="black")
        self.btn_save.place(x=160,y=260,width=130,height=30)
        
        self.btn_clear=Button(Frame2,text="Clear",command=self.clear,font=("times new roman",20),bg="gray",fg="black")
        self.btn_clear.place(x=300,y=260,width=130,height=30)
        
        self.btn_Update=Button(Frame2,text="Update",state=DISABLED,command=self.update,font=("times new roman",20),bg="blue",fg="black")
        self.btn_Update.place(x=440,y=260,height=30,width=130)
        
        self.btn_Delete=Button(Frame2,text="Delete",state=DISABLED,command=self.delete,font=("times new roman",20),bg="red",fg="black")
        self.btn_Delete.place(x=590,y=260,height=30,width=130)
        
        
        #=====================================FRAME3============================================
        Frame3=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        Frame3.place(x=760,y=360,width=760,height=310) 
        
        #==========================CALCULATOR FRAME===================================
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)
        
        Calc_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        Calc_Frame.place(x=2,y=2,width=220,height=292)
        
        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''
            
        def clear_cal():
            self.var_txt.set('')
            self.var_operator=''
            
        
        txt_result=Entry(Calc_Frame,bg="red",textvariable=self.var_txt,font=("times new roman",20,"bold"),justify=RIGHT).place(x=0,y=0,relwidth=1,height=40)
        
        btn_7=Button(Calc_Frame,text='7',command=lambda:btn_click(7),font=("times new roman",15,"bold")).place(x=0,y=55,width=60,height=60)
        btn_8=Button(Calc_Frame,text='8',command=lambda:btn_click(8),font=("times new roman",15,"bold")).place(x=51,y=55,width=60,height=60)
        btn_9=Button(Calc_Frame,text='9',command=lambda:btn_click(9),font=("times new roman",15,"bold")).place(x=101,y=55,width=60,height=60)
        btn_d=Button(Calc_Frame,text='/',command=lambda:btn_click('/'),font=("times new roman",15,"bold")).place(x=153,y=55,width=60,height=60)

        
        btn_6=Button(Calc_Frame,text='6',command=lambda:btn_click(6),font=("times new roman",15,"bold")).place(x=0,y=105,width=60,height=60)
        btn_5=Button(Calc_Frame,text='5',command=lambda:btn_click(5),font=("times new roman",15,"bold")).place(x=51,y=105,width=60,height=60)
        btn_4=Button(Calc_Frame,text='4',command=lambda:btn_click(4),font=("times new roman",15,"bold")).place(x=101,y=105,width=60,height=60)
        btn_m=Button(Calc_Frame,text='*',command=lambda:btn_click('*'),font=("times new roman",15,"bold")).place(x=153,y=105,width=60,height=60)


        btn_3=Button(Calc_Frame,text='3',command=lambda:btn_click(3),font=("times new roman",15,"bold"),justify=CENTER).place(x=0,y=155,width=60,height=60)
        btn_2=Button(Calc_Frame,text='2',command=lambda:btn_click(2),font=("times new roman",15,"bold")).place(x=51,y=155,width=60,height=60)
        btn_1=Button(Calc_Frame,text='1',command=lambda:btn_click(1),font=("times new roman",15,"bold")).place(x=101,y=155,width=60,height=60)
        btn_m=Button(Calc_Frame,text='-',command=lambda:btn_click('-'),font=("times new roman",15,"bold")).place(x=153,y=155,width=60,height=60)
        
        btn_z=Button(Calc_Frame,text='0',command=lambda:btn_click(0),font=("times new roman",15,"bold")).place(x=0,y=205,width=60,height=60)
        btn_dot=Button(Calc_Frame,text='C',command=clear_cal,font=("times new roman",15,"bold")).place(x=51,y=205,width=60,height=60)
        btn_p=Button(Calc_Frame,text='+',command=lambda:btn_click('+'),font=("times new roman",15,"bold")).place(x=101,y=205,width=60,height=60)
        btn_e=Button(Calc_Frame,text='=',command=result,font=("times new roman",15,"bold")).place(x=153,y=205,width=60,height=60)



        #===========================================SALARY FRAME=======================================
        sal_frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_frame.place(x=230,y=2,width=500,height=290)
        
        title_sal=Label(sal_frame,text="Salary Reciept",font=("times new roman",20,"bold"),bg="gray",fg="black",padx=30,anchor="w").place(x=0,y=0,relwidth=1)
        
        sal_frame2=Frame(sal_frame,bg="white",bd=2,relief=RIDGE)
        sal_frame2.place(x=0,y=30,relwidth=1,height=220)
        
        self.sample=f'''\t Company Name,Phone Zone\n\tAddress: phoone zone,floor
----------------------------------------------------------
Employee ID\t\t:
Salary Of\t\t: MM-YYYY
Generated On\t\t:DD-MM-YY
-------------------------------------------------------------
Total Days\t\t:DD
Total Present\t\t:DD
Total Absent\t\t:DD
Convence\t\t:Rs.-----
Medical\t\t:Rs.-----
PF\t\t:Rs.-----
Gross Payment\t\t:Rs.-----
Net salay\t\t:Rs.---------

--------------------------------------------------------------
this is computer generated slip,not
required any signature
'''
        
        scroll_y=Scrollbar(sal_frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)
        
        self.txt_salary_reciept=Text(sal_frame2,font=("times new roman",15),bg="lightyellow",yscrollcommand=scroll_y.set)
        self.txt_salary_reciept.pack(fill=BOTH,expand=1)
        
        scroll_y.config(command=self.txt_salary_reciept.yview)
        self.txt_salary_reciept.insert(END,self.sample)
        
        self.btn_print=Button(sal_frame,text="Print",state=DISABLED,command=self.print,font=("times new roman",20),bg="lightblue",fg="black")
        self.btn_print.place(x=340,y=252,width=120,height=30)
        
        self.check_connection()
    #==============================ALLL FUNCTION ARE START HERE
     #==============================================FRAME1 VARIABLES===============================
     
     #=============================================SEARCH FUNCTION===================================================
    def search(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","invalid employee id plz try another employee id",parent=self.root)
            else:
                self.var_emp_code.set('')
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_hr_location.set(row[6])
                self.var_doj.set(row[7])
                self.var_dob.set(row[8])
                self.var_experience.set(row[9])
                self.var_proof_id.set(row[10])
                self.var_contact.set(row[11])
                self.var_status.set(row[12])
                self.txt_address.delete('1.0',END)
                self.txt_address.insert(END,row[13])
                
                self.var_month.set(row[14])
                self.var_year.set(row[15])
                self.var_salary.set(row[16])
                self.var_t_days.set(row[17])
                self.var_absents.set(row[18])
                self.var_medical.set(row[19])
                self.var_pf.set(row[20])
                self.var_convence.set(row[21])
                self.var_net_salary.set(row[22])
                file_=open('Salary_reciept'+str(row[23]),'r')
                self.txt_salary_reciept.delete('1.0',END)
                for i in file_:
                    self.txt_salary_reciept.insert(END,i)
                file_.close()
                self.btn_save.config(state=DISABLED)
                self.btn_Update.config(state=NORMAL)
                self.btn_Delete.config(state=NORMAL)
                #self.txt_code.config(state='readonly')
                self.btn_print.config(state=NORMAL)
                
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to{str(ex)}")
                #==========================================CLEAR FUNCTION==========================================
    def clear(self):
        self.btn_save.config(state=NORMAL)
        self.btn_Update.config(state=DISABLED)
        self.btn_Delete.config(state=DISABLED)
        #self.txt_code.config(state=NORMAL)
        self.btn_print.config(state=DISABLED)
        
        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_hr_location.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_experience.set('')
        self.var_proof_id.set('')
        self.var_contact.set('')
        self.var_status.set('')
        self.txt_address.delete('1.0',END)
        
                
        self.var_month.set('')
        self.var_year.set('')
        self.var_salary.set('')
        self.var_t_days.set('')
        self.var_absents.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_net_salary.set('')
        self.txt_salary_reciept.delete('1.0',END)
        self.txt_salary_reciept.insert(END,self.sample)
        
        
    #============================================================DELETE FUNCTION=======================================
    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror("Error","Plz insert correct employee id required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid employee id plz try another employee id",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete")
                    print(op)
                    if op==True:
                        cur.execute("delete from emp_salary where e_id=%s",(self.var_emp_code.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","employee record deleted successfully",parent=self.root)
                        self.clear()
                        
            except Exception as ex:
                    messagebox.showerror("Error",f"Error due to{str(ex)}")
     #=========================================================ADD OR SAVE FUNCTION============================================       
    def add(self):
        if self.var_emp_code.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","Employee Details Are Required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","this employee ID has already availabe in record with another id",parent=self.root)
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (
                                self.var_emp_code.get(),
                                self.var_designation.get(),
                                self.var_name.get(),
                                self.var_age.get(),
                                self.var_gender.get(),
                                self.var_email.get(),
                                self.var_hr_location.get(),
                                self.var_doj.get(),
                                self.var_dob.get(),
                                self.var_experience.get(),
                                self.var_proof_id.get(),
                                self.var_contact.get(),
                                self.var_status.get(),
                                self.txt_address.get('1.0',END),
                                self.var_month.get(),
                                self.var_year.get(),
                                self.var_salary.get(),
                                self.var_t_days.get(),
                                self.var_absents.get(),
                                self.var_medical.get(),
                                self.var_pf.get(),
                                self.var_convence.get(),
                                self.var_net_salary.get(),
                                self.var_emp_code.get()+".txt"
                                
                                
                            ))
                con.commit()
                con.close()
                file_=open('Salary_reciept'+str(self.var_emp_code.get())+".txt",'w')
                file_.write(self.txt_salary_reciept.get('1.0',END))
                file_.close()
                messagebox.showinfo("Success","Record Added Successfullly")
                self.btn_print.config(state=NORMAL)
                
                
                #print("connection")
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to{str(ex)}")
    #=========================================================UPDATE FUNCTION======================================================================
    def update(self):
        if self.var_emp_code.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","Employee Details Are Required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","this employee ID is invalid,plz try another employee id",parent=self.root)
                else:
                    cur.execute("UPDATE emp_salary SET designation=%s,name=%s,age=%s,gender=%s,email=%s,hr_location=%s,doj=%s,dob=%s,experience=%s,proof_id=%s,contact=%s,status=%s,address=%s,month=%s,year=%s,basic_salary=%s,t_days=%s,absent_days=%s,medical=%s,pf=%s,convence=%s,net_salary=%s',salary_reciept=%s WHERE e_id=%s",
                            (
                                
                                self.var_designation.get(),
                                self.var_name.get(),
                                self.var_age.get(),
                                self.var_gender.get(),
                                self.var_email.get(),
                                self.var_hr_location.get(),
                                self.var_doj.get(),
                                self.var_dob.get(),
                                self.var_experience.get(),
                                self.var_proof_id.get(),
                                self.var_contact.get(),
                                self.var_status.get(),
                                self.txt_address.get('1.0',END),
                                self.var_month.get(),
                                self.var_year.get(),
                                self.var_salary.get(),
                                self.var_t_days.get(),
                                self.var_absents.get(),
                                self.var_medical.get(),
                                self.var_pf.get(),
                                self.var_convence.get(),
                                self.var_net_salary.get(),
                                self.var_emp_code.get()+".txt",
                                self.var_emp_code.get(),
                                
                                
                            ))
                con.commit()
                con.close()
                file_=open('Salary_reciept'+str(self.var_emp_code.get())+".txt",'w')
                file_.write(self.txt_salary_reciept.get('1.0',END))
                file_.close()
                messagebox.showinfo("Success","Record Updated Successfullly")
                
                
                #print("connection")
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to{str(ex)}")
    #=======================================================================CALCULATE FUNCTION ======================================================   
    def calculate(self):
        #if self.var_month.get()=='' or self.var_year.get()=='' or self.var_salary.get()=='' or self.var_t_days.get()=='' or self.var_absents.get()=='' or self.var_emp_code.get()=='' or self.var_name.get()=='' or self.var_status.get():
            #messagebox.showerror("Error","All Field Are Requireds")
    
        #else:
        per_day=int(self.var_salary.get())/int(self.var_t_days.get())
        work_day=int(self.var_t_days.get())-int(self.var_absents.get())
        sal_=per_day*work_day
        deduct=int(self.var_medical.get())+int(self.var_pf.get())
        addition=int(self.var_convence.get())
        net_sal=sal_-deduct+addition
        self.var_net_salary.set(str(round(net_sal,2)))
        
        #===============================SALARY RECIEPT=====================
        
        new_sample=f'''\t Company Name,Phone Zone\n\tAddress: phoone zone,floor
----------------------------------------------------------
Employee ID\t\t:{self.var_emp_code.get()}
Salary Of\t\t: {self.var_month.get()}-{self.var_year.get()}
Generated On\t\t:{str(time.strftime("%d-%m-%Y"))}
-------------------------------------------------------------
Total Days\t\t:{self.var_t_days.get()}
Total Present\t\t:{str(int(self.var_t_days.get())-int(self.var_absents.get()))}
Total Absent\t\t:{self.var_absents.get()}
Convence\t\t:Rs.---{self.var_convence.get()}
Medical\t\t:Rs.-----{self.var_medical.get()}
PF\t\t:Rs.-----{self.var_pf.get()}
Gross Payment\t\t:Rs.-----{self.var_salary.get()}
Net salay\t\t:Rs.---------{self.var_net_salary.get()}

--------------------------------------------------------------
this is computer generated slip,not
required any signature
'''
        self.txt_salary_reciept.delete('1.0',END)
        self.txt_salary_reciept.insert(END,new_sample)
        
           
    #=========================================CONNECTION CHECK FUNCTION===========================================
    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            #print(rows)
            
            #print("connection")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
            
    def show(self):  
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            #print(rows)
            self.employee_tree.delete(*self.employee_tree.children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()
            #print("connection")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
            
    def employee_frame(self):
        self.root2=Toplevel(self.root)
        self.root2.title("Employee Pay Roll Management System")
        self.root2.config(bg="white")
        self.root2.geometry("1000x500+120+100")
        
        
        
        title=Label(self.root2,text="All Employee Details",font=("times new roman",30,"bold"),bg="black",fg="red").pack(side=TOP,fill=X)
        self.root2.focus_force()
        
        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)
        
        self.employee_tree=ttk.Treeview(self.root2,columns=('e_id', 'designation', 'name', 'age', 'gender', 'email', 'hr_location', 'doj', 'dob', 'experience', 'proof_id', 'contact', 'status', 'address', 'month', 'year', 'basic_salary', 't_days', 'absent_days', 'medical', 'pf', 'convence', 'net_salary', 'salary_reciept'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('e_id',text='EID')
        self.employee_tree.heading('designation',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('hr_location',text='Hr_Location')
        self.employee_tree.heading('doj',text='Doj')
        self.employee_tree.heading('dob',text='Dob')
        self.employee_tree.heading('experience',text='Experience')
        self.employee_tree.heading('proof_id',text='Proof')
        self.employee_tree.heading('contact',text='Contact')
        self.employee_tree.heading('status',text='Status')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('basic_salary',text='Basic Salary')
        self.employee_tree.heading('t_days',text='Total Days')
        self.employee_tree.heading('absent_days',text='Absent_Days')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('pf',text='PF')
        self.employee_tree.heading('convence',text='Convence')
        self.employee_tree.heading('net_salary',text='Salary')
        self.employee_tree.heading('salary_reciept',text='Salary Receipt')
        
        self.employee_tree['show']='headings'
        
        self.employee_tree.column('e_id',width=100)
        self.employee_tree.column('designation',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('hr_location',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('proof_id',width=100)
        self.employee_tree.column('contact',width=100)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('address',width=200)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('basic_salary',width=100)
        self.employee_tree.column('t_days',width=100)
        self.employee_tree.column('absent_days',width=100)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence',width=100)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salary_reciept',width=100)
        
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        
        self.show()
        
    
        
        
        self.root2.mainloop()
        
    def print(self):
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_reciept.get('1.0',END))
        os.startfile(file_,'print')
        #btn_emp=Button(self.root,text="All Employees",font=("times new roman",13),bg="darkgray",fg="black").place(x=1300,y=10,height=30,width=120)
        
        
        
        
      
        
        
        
       
        
        
        
        
        
       
        
        
root=Tk()
obj=EmployeeSystem(root)
root.mainloop()