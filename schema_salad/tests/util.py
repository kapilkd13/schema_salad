from pkg_resources import Requirement, resource_filename, ResolutionError  # type: ignore
from typing import Optional, Text
import os

def get_data(filename):  # type: (Text) -> Optional[Text]
    filename=os.path.normpath(filename)
    filepath = None
    try:
        filepath = resource_filename(
            Requirement.parse("schema-salad"), filename)
    except ResolutionError:
        pass
    if not filepath or not os.path.isfile(filepath):
        filepath = os.path.join(os.path.dirname(__file__), os.pardir, filename)
    # if filepath[0] != "/":
    #     filepath="/" + filepath  # for windows path which don't have / in its path
    return filepath
