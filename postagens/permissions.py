from rest_framework import permissions





class IsOwnerOrReadOnly(permissions.BasePermission):

    message = 'Você não tem permissão para excluir esse POST'

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        else:

            return obj.owner.user == request.user





class comentarios(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        else:
            return obj.post.owner.user == request.user
