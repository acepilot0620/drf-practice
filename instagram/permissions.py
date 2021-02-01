from rest_framework import permissions

class Is_AuthorOrReadonly(permissions.BasePermission):
    # 인증이 되어야만 목록조회/ 포스팅 등록
    def has_permission(self, request, view):
        return request.user and  request.user.is_authenticated

    # 작성자에 한해 Record에 대한 수정 삭제 허용
    def has_object_permission(self, request, view, obj):
        # 조회 요청 (GET, HEAD, OPTIONS)에 대해서는 인증 여부 없이 허용
        if request.method in permissions.SAFE_METHODS:
            return True
        # PUT, DELETE 요청에 대해, 작성자 일때만 요청허용
        return obj.author == request.user

