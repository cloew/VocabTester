from .auth import auth
from .legacy_password_util import LegacyPasswordUtil
from .Controllers import CreateUserEnrollment, GetUserEnrollments
from ..helpers.admin_json_factory import toJson

from kao_flask import Routes, Endpoint
from kao_flask.ext.sqlalchemy import RecordValueProvider

nativeLanguageProvider = RecordValueProvider({'nativeLanguage': lambda value: ('native_language_id', value['id'])})
util = LegacyPasswordUtil()

routes = Routes(Endpoint('/api/login', post=auth.LoginController(toJson, legacyUtils=[util])),
                Endpoint('/api/users', post=auth.RegisterController(toJson, recordValueProvider=nativeLanguageProvider)),
                Endpoint('/api/users/current', get=auth.CurrentUserController(toJson), put=auth.UpdateUserController(toJson, recordValueProvider=nativeLanguageProvider)),
                Endpoint('/api/users/current/enrollments', get=GetUserEnrollments(), post=CreateUserEnrollment()))