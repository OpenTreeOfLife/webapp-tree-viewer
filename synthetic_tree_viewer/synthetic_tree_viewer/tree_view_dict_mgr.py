from synthetic_tree_viewer.util import (
    fetch_current_TNRS_context_names,
    get_currently_deployed_opentree_branch,
    get_domain_banner_text,
    get_domain_banner_hovertext,
)


def create_tree_view_dict(rset):
    cdob = get_currently_deployed_opentree_branch()
    subdomain = rset.get("opentree.subdomain", "devtree")
    dbt = get_domain_banner_text(subdomain)
    dbht = get_domain_banner_hovertext(subdomain)
    tvd = {
        # NB - Duplicate keys will be resolved in favor of the values below!
        # "conf": get_conf(request),  # needed for the footer diagnostics
        "project_name": "synthetic tree viewer",
        #'session': request.session,
        # "response": request.response,
        # "registry": request.registry,
        "currently_deployed_opentree_branch": cdob,
        # NB - some values will be filled in (or modified) below
        "nodeID": "",
        "nodeName": "",
        "viewport": "",
        "taxonSearchContextNames": None,
        "nudgingToLatestSyntheticTree": False,
        "forcedByURL": False,
        "incomingDomSource": "none",
        "domain_banner_text": dbt,
        "domain_banner_hovertext": dbht,
    }
    rset["extra_tree_view_dict"] = tvd
    return tvd


def update_tree_view_dict(rset, tvd):
    """Updates tvd if some of the online values are unset."""
    key = "taxonSearchContextNames"
    val = tvd.get(key)
    if val is None:
        tvd[key] = fetch_current_TNRS_context_names(rset)
    return tvd
