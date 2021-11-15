from crudapp.api.serializers import AccountSerializer
from crudapp.models import Account
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# CREATE
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def api_account_create(request):
    # user = User.objects.get(username='admin')
    user = request.user

    account = Account(creator=user)
    serializer = AccountSerializer(account, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# READ
@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def api_account_read(request, acc_id):
    try:
        account = Account.objects.get(pk=acc_id)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AccountSerializer(account)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def api_account_read_all(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)


# UPDATE
@api_view(['PUT', ])
@permission_classes((IsAuthenticated, ))
def api_account_update(request, acc_id):
    try:
        account = Account.objects.get(pk=acc_id)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if account.creator != user:
        return Response({'status': "You don't have permissions for this operation."})

    serializer = AccountSerializer(account, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data['status'] = 'Update completed'
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DELETE
@api_view(['DELETE', ])
@permission_classes((IsAuthenticated, ))
def api_account_delete(request, acc_id):
    try:
        account = Account.objects.get(pk=acc_id)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if account.creator != user:
        return Response({'status': "You don't have permissions for this operation."})

    deletion = account.delete()
    data = {}
    if deletion:
        data['status'] = 'Delete completed'
    else:
        data['status'] = 'Delete failed'
    
    return Response(data=data)


