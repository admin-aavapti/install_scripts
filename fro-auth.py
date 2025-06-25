import pluggy
from tutor import hooks
from tutormfe.hooks import MFE_APPS
import os

@MFE_APPS.add()
def _add_custom_authoring_mfe(mfes):
    git_token = os.environ.get("GIT_TOKEN", "")
    mfes["authoring"] = {
        "repository": f"https://admin-aavapti:{GH_PAT}@github.com/admin-aavapti/frontend-app-authoring.git",
        "port": "9876",
        "version": "sumac.2",
    }
    return mfes
