import os
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
import datetime
from numpy import roll
import qrcode
import qrcode.image.svg
from io import BytesIO
from attendance.models import QR, Data, Attendance, Room
import pandas as pd
from pathlib import Path
# Create your views here.

BASE_DIR = Path(__file__).resolve().parent.parent

def handleLogin(request):

    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('staff')
        else:
            return redirect('student')
    else:
        if request.method == 'POST':
            username = request.POST['user_name']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")

                if request.user.is_staff:
                    return redirect('staff')

                else: return redirect('student')
            else: return redirect('login')
        else: return render(request, 'attendance/login.html')

def handleRegister(request):

    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('staff')
        else:
            return redirect('student')

    elif request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['passwd']
        c_password = request.POST['confirm_passwd']

        roll_no = request.POST['roll_no']
        
        l = [f.name for f in Attendance._meta.get_fields()]
        l.remove('id')
        l.remove('class_date')
        l.remove('code')

        r = [r.split("_", 1)[1] for r in l]
        # Check for errorneous input
        if len(username) > 15 or len(username) < 6:
            messages.error(request, "User name must be greater than 6 characters and less than 15 character.")
            return render(request, 'attendance/register.html')

        if not username.isalnum():
            messages.error(request, "Username must only contain letters and numbers.")
            return render(request, 'attendance/register.html')
                
        if password != c_password:
            messages.error(request, "Password do not match.")
            return render(request, 'attendance/register.html')

        if roll_no == 0:
            # Create user
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()

            messages.success(request, "Your Profile has been created.")

            return redirect('login')

        elif roll_no in r:
            # Create user

            data = Data.objects.all()
            l = []
            for item in data:
                l.append(item.roll_no)
            
            if roll_no in l:
                return HttpResponse("You have already registered!!!")

            else:
                myuser = User.objects.create_user(username, email, password)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()
                name = fname + lname
                data = Data(username=username, name=name, roll_no=roll_no, email=email)
                data.save()
                messages.success(request, "Your Profile has been created.")

                return redirect('login')

        else:
            return HttpResponse("Roll No. not Supported.")

    else:
        return render(request, 'attendance/register.html')

def generate_df():
    l = [f.name for f in Attendance._meta.get_fields()]
    l.remove('id')
    l.remove('class_date')
    l.remove('code')
            
    list_roll = [r.split("_", 1)[1] for r in l]

    list_dates = []
    
    att = Attendance.objects.values()
    
    dict_data = {}
    list_data = []

    for i in att:
        del i['code']
        del i['id']

        list_dates.append(str(i['class_date']))

        # del i['class_date']

        dict_data[str(i['class_date'])] = list(i.values())[1:]
        

    for key in dict_data:
        list_data.append(dict_data[key])

    df = pd.DataFrame(dict_data, index=list_roll)
    return df


@ staff_member_required
def staff(request):

    room = Room.objects.get(id=1)
    room.door = 'close'
    room.save()
    return render(request, 'attendance/staff.html')

@ login_required
def view_attendance(request):
    df = generate_df()
    return HttpResponse(df.to_html())

@ login_required
def download_attendance(request):
    df = generate_df()
    file_name = "attendance.xlsx"
    with BytesIO() as b:
        # Use the StringIO object as the filehandle.
        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        # Set up the Http response.
        response = HttpResponse(
            b.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % file_name
        return response

@ staff_member_required
def update_attendance(request):
    if request.method == 'POST':
        att_date = request.POST['att_date']
        roll_no = request.POST['roll_no']
        no_classes = request.POST['no_classes']

        student_id = f"student_{roll_no}"
        r = 0
        att_dict = Attendance.objects.values()
        l = list(att_dict)
        # print(l)

        for i in l:
            # print(i)
            # print("id is ", i['id'])
            if str(i['class_date']) == att_date:
                r += l.index(i)
                # print("index is ", r)
            else: pass
        
        # print("index is ", r)
        dict = l[r]

        dict[student_id] = no_classes
        # print(dict)
        att = Attendance.objects.get(class_date=att_date)
        # print(att.class_date)
        att.__dict__.update(dict)
        att.save()

        print("Attendance Updated Successfully.")
        messages.success(request, "Attendance Updated Successfully.")
        return redirect('staff')

@ staff_member_required
def generate_qr(request):
    room = Room.objects.get(id=1)
    room.door = 'open'
    room.save()

    context = {}
    if request.method == 'POST':
        n_classes = request.POST['nclass']
        stime = request.POST['stime']

        ct = datetime.datetime.now()
        ts = int(ct.timestamp())
        cdate = datetime.date.today()

        qr = QR(code=ts, no_classes= n_classes, ctime=stime, cdate=cdate)
        
        qr.save()
        
        att = Attendance(code=ts, class_date = cdate)
        att.save()
        print(Attendance.objects.last().student_363)

        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(ts, image_factory=factory, box_size=60)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()
        return render(request, 'attendance/qr.html', context=context)

    else: return render(request, 'attendance/generate_qr.html')

@ login_required
def student(request):
    data = Data.objects.get(username = request.user.username)
    roll_no = data.roll_no
    fname = request.user.first_name
    lname = request.user.last_name

    room = Room.objects.get(id=1)
    door = room.door

    if door == 'open':
        params = {'roll_no':roll_no, 'fname':fname, 'lname':lname}
        return render(request, 'attendance/student.html', params)

    else: return HttpResponse(f"Dear {fname} {lname}, Attendance is not taking place. <br> <a href='view_attendance'>View Attendance</a>")

@ login_required
def markPresent(request):
    
    if request.method == 'POST':
        uploaded_code = request.POST.get('attendanceId', None)
        roll_no = request.POST.get('roll_no', None)

        attendance_code = QR.objects.last().code
        no_classes = QR.objects.last().no_classes

        if uploaded_code == attendance_code:

            student_id = f"student_{roll_no}"    
            # print(uploaded_code, "\n", roll_no, "\n", attendance_code)
            # print("Student Id : ", student_id )

            l = [f.name for f in Attendance._meta.get_fields()]
            l.remove('id')
            l.remove('class_date')
            l.remove('code')
            # print("list worked successfully..")
            # print(l)
            r = [r.split("_", 1)[1] for r in l]
            # print("Splitting Successfull")
            # print(r)

            # print("Provided Roll No. Type = ", type(roll_no))
            # print(type(r[0]))

            att_dict = Attendance.objects.values()
            # print("Att_dict created Successfully...")

            if roll_no in r:

                updated_dict = att_dict.values()[len(Attendance.objects.values())-1]

                # print("Disctionary Updated Successfully...")
                updated_dict[student_id] = no_classes

                print("Attendence value updated", updated_dict[student_id])

                att_query = Attendance.objects.get(code=attendance_code)
                att_query.__dict__.update(updated_dict)
                # print("Attendence Query Successfull...")
                att_query.save()

        return HttpResponse(f"Attendance Marked Successfully. <br> <b> Student Roll No. {roll_no} </b> <br> <a href='view_attendance'>View Attendance</a>")
