import pluggy
from tutor import hooks
from tutormfe.hooks import MFE_APPS
import os

@MFE_APPS.add()
def _add_custom_authoring_mfe(mfes):
    gh_pat = os.environ.get("GH_PAT")
    mfes["authoring"] = {
        "repository": f"https://admin-aavapti:{gh_pat}@github.com/admin-aavapti/frontend-app-authoring.git",
        "port": "9876",
        "version": "sumac.2",
    }
    return mfes
