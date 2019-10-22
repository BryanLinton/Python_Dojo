from config import app
from controller_functions import dojo_users, add_dojo, add_ninja

app.add_url_rule("/", view_func=dojo_users)
app.add_url_rule("/add_dojo", view_func=add_dojo, methods=["POST"])
app.add_url_rule("/add_ninja", view_func=add_ninja, methods=["POST"])