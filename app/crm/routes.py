import typing


if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application"):
    from app.crm.views import AddUserView
    from app.crm.views import ListUserView
    from app.crm.views import GetUserView
    from app.crm.views import GetUserDeleteView

    app.router.add_view("/add_user", AddUserView)
    app.router.add_view("/list_users", ListUserView)
    app.router.add_view("/get_users", GetUserView)
    app.router.add_view("/delete_users", GetUserDeleteView)
