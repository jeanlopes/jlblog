def enum(**enums):
    return type('Enum', (), enums)

AllowComments = enum(NO=1, YES=2, LOGGED_ONLY=3)
Sex = enum(MALE = 1, FEMALE = 2)

