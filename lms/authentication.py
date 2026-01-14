import jwt
from django.utils import timezone
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError


class SafeJWTAuthentication(JWTAuthentication):
    refresh_endpoint = "/api/token/refresh/"

    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        try:
            validated_token = self.get_validated_token(raw_token)
        except TokenError as exc:
            if self._is_expired(raw_token):
                raise AuthenticationFailed(
                    detail=
                        {
                            "error": "token_expired",
                            "message": "Token has expired",
                            "refresh_endpoint": self.refresh_endpoint,
                        },
                    code="token_expired",
                ) from exc
            raise AuthenticationFailed(
                detail={"error": "invalid_token", "message": "Token is invalid"},
                code="invalid_token",
            ) from exc

        return self.get_user(validated_token), validated_token

    def _is_expired(self, raw_token: bytes) -> bool:
        try:
            payload = jwt.decode(raw_token, options={"verify_signature": False})
        except jwt.DecodeError:
            return False
        exp = payload.get("exp")
        if exp is None:
            return False
        return timezone.now().timestamp() > exp

