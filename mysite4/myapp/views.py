from django.shortcuts import render
import json
from .models import Register
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def reg(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        Fname = data.get("Fname")
        Lname = data.get("Lname")
        Phone = data.get("Phone")
        Email = data.get("Email")
        Password = data.get("Password")

        Register.objects.create(
            Fname=Fname,
            Lname=Lname,      
            Phone=Phone,
            Email=Email,
            Password=Password
        )
        return JsonResponse({"message": "Registered Successfully"}, status=201)

    return JsonResponse({"Error": "POST Method Only"}, status=405)


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        Email = data.get("Email")
        Password = data.get("Password")

        # correct filter
        user_exists = Register.objects.filter(Email=Email, Password=Password).exists()

        if user_exists:
            return JsonResponse({"message": "Login Successfully"}, status=200)
        else:
            return JsonResponse({"message": "Invalid Email or Password"}, status=400)

    return JsonResponse({"Error": "POST Method Only"}, status=405)


@csrf_exempt
def get_data(request):
    if request.method == "GET":
        data = Register.objects.all()
        sample = []
        for user in data:
            sample.append({
                "Firstname": user.Fname,
                "Lastname":  user.Lname,      
                "Phone":     user.Phone,
                "Email":     user.Email,
                "Password":  user.Password,
            })
        return JsonResponse({"Details": sample}, status=200)

    return JsonResponse({"Error": "GET Method Only"}, status=405)


@csrf_exempt
def delete_data(request):
    """
    Simple delete endpoint:
    Send JSON: {"Email": "someone@example.com"}
    """
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        Email = data.get("Email")

        if not Email:
            return JsonResponse({"Error": "Email is required"}, status=400)

        deleted_count, _ = Register.objects.filter(Email=Email).delete()

        if deleted_count:
            return JsonResponse({"message": "User deleted successfully"}, status=200)
        else:
            return JsonResponse({"message": "No user found with this Email"}, status=404)

    return JsonResponse({"Error": "POST Method Only"}, status=405)

@csrf_exempt
def update_data(request):
    if request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        Id = data.get("id")

        if not Register.objects.filter(id=Id).exists():
            return JsonResponse({"message": "User not found"})

        Register.objects.filter(id=Id).update(
            Fname=data.get("Fname"),
            Lname=data.get("Lname"),
            Phone=data.get("Phone"),
            Email=data.get("Email"),
            Password=data.get("Password")
        )

        return JsonResponse({"message": "Updated successfully"})

    return JsonResponse({"Error": "PUT method only"}, status=400)