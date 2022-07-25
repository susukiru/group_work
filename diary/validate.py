from django.core.exceptions import ValidationError

def validate_admin(value):
    if 'admin' in value:
        raise ValidationError('adminを含んだメールアドレスはご利用できません!!')

def validate_title(value):

    if '禿' in value:

        raise ValidationError('禿を含んだタイトルはご利用いただけません')