from synthetic_tree_viewer.util import (
    fetch_current_TNRS_context_names,
    get_currently_deployed_opentree_branch,
    get_domain_banner_text,
    get_domain_banner_hovertext,
)
import logging

_LOG = logging.getLogger(__name__)


def create_tree_view_dict(rset):
    cdob = get_currently_deployed_opentree_branch()
    subdomain = rset.get("opentree.subdomain", "devtree")
    dbt = get_domain_banner_text(subdomain)
    dbht = get_domain_banner_hovertext(subdomain)
    ctns = fetch_current_TNRS_context_names(rset)

    tvd = {
        # NB - Duplicate keys will be resolved in favor of the values below!
        "project_name": "synthetic tree viewer",
        #'session': request.session,
        # "response": request.response,
        # "registry": request.registry,
        "currently_deployed_opentree_branch": cdob,
        # NB - some values will be filled in (or modified) below
        "nodeID": "",
        "nodeName": "",
        "viewport": "",
        "taxonSearchContextNames": ctns,
        "nudgingToLatestSyntheticTree": False,
        "forcedByURL": False,
        "incomingDomSource": "none",
        "domain_banner_text": dbt,
        "domain_banner_hovertext": dbht,
    }
    rset["extra_tree_view_dict"] = tvd
    return tvd
