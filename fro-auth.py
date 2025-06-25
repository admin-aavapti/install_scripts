import pluggy
from tutor import hooks
from tutormfe.hooks import MFE_APPS
import os

@MFE_APPS.add()
def _add_custom_authoring_mfe(mfes):
    mfes["authoring"] = {
        "repository": f"https://github.com/admin-aavapti/frontend-app-authoring.git",
        "port": "9876",
        "version": "sumac.2",
    }
    return mfes
